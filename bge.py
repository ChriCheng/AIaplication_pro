from sentence_transformers import SentenceTransformer, InputExample, losses, evaluation
from torch.utils.data import DataLoader
import os
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

import json

# ====== 1. 加载模型 ======

model_name = "bge-large-zh-v1.5-csts-finetuned"
model = SentenceTransformer(model_name)

# ====== 2. 加载训练数据 ======
train_path = "CSTS_BGE/train.jsonl"
dev_path = "CSTS_BGE/dev.jsonl"

def load_jsonl(path):
    data = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            obj = json.loads(line)
            s1, s2, label = obj["sentence1"], obj["sentence2"], float(obj["label"])
            data.append(InputExample(texts=[s1, s2], label=label))
    return data

train_samples = load_jsonl(train_path)
dev_samples = load_jsonl(dev_path)

# ====== 3. 构造 DataLoader ======
train_dataloader = DataLoader(train_samples, shuffle=True, batch_size=16)
train_loss = losses.CosineSimilarityLoss(model)

# ====== 4. 构造验证器（可选） ======
dev_evaluator = evaluation.EmbeddingSimilarityEvaluator.from_input_examples(
    dev_samples, name="csts-dev"
)

# ====== 5. 开始微调 ======
model.fit(
    train_objectives=[(train_dataloader, train_loss)],
    evaluator=dev_evaluator,
    epochs=3,                     # 训练轮数，可调整
    warmup_steps=100,
    output_path="bge-large-zh-v1.5-csts-finetuned",
    evaluation_steps=200,
    save_best_model=True,
    show_progress_bar=True
)
