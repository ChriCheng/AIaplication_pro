from sentence_transformers import SentenceTransformer, InputExample, losses, evaluation
from torch.utils.data import DataLoader
import os, json, glob, datetime
#t
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

# ====== 1. 自动检测 checkpoint ======
base_model_dir = os.path.abspath("bge-base-zh-v1.5-csts-finetuned")
checkpoint_dir = os.path.join(base_model_dir, "checkpoints")
log_path = "train.log"

def log(msg):
    """记录到日志文件并打印"""
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"[{time}] {msg}\n")
    print(msg)

resume_checkpoint = None
if os.path.exists(checkpoint_dir):
    checkpoints = sorted(glob.glob(os.path.join(checkpoint_dir, "checkpoint_*")), key=os.path.getmtime)
    if checkpoints:
        resume_checkpoint = checkpoints[-1]
        log(f"🔁 检测到断点: {resume_checkpoint}")
    else:
        log("🚀 未检测到断点，将从 finetuned 模型开始训练。")
else:
    log("🚀 第一次训练，未找到 checkpoint 目录。")

# ====== 2. 加载模型 ======
model = SentenceTransformer(base_model_dir)
log(f"✅ 已加载模型: {base_model_dir}")

# ====== 3. 加载数据 ======
train_path = "CSTS_BGE/train.jsonl"
dev_path = "CSTS_BGE/dev.jsonl"

def load_jsonl(path):
    data = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            obj = json.loads(line)
            data.append(InputExample(texts=[obj["sentence1"], obj["sentence2"]], label=float(obj["label"])))
    return data

train_samples = load_jsonl(train_path)
dev_samples = load_jsonl(dev_path)
log(f"📚 数据加载完成: train={len(train_samples)} 条, dev={len(dev_samples)} 条")

# ====== 4. 构造 DataLoader ======
train_dataloader = DataLoader(train_samples, shuffle=True, batch_size=16)
train_loss = losses.CosineSimilarityLoss(model)
log("🧩 构建 DataLoader 完成。")

# ====== 5. 构造验证器 ======
dev_evaluator = evaluation.EmbeddingSimilarityEvaluator.from_input_examples(
    dev_samples, name="csts-dev"
)

# ====== 6. 自定义评估回调 ======
def eval_callback(score, epoch, steps):
    msg = f"📈 [Epoch {epoch} | Step {steps}] Spearman: {score:.4f}"
    log(msg)

# ====== 7. 开始训练 ======
log("🏋️‍♂️ 开始训练 ...")

model.fit(
    train_objectives=[(train_dataloader, train_loss)],
    evaluator=dev_evaluator,
    epochs=3,
    warmup_steps=100,
    output_path=base_model_dir,
    evaluation_steps=200,
    save_best_model=True,
    show_progress_bar=True,
    checkpoint_path=checkpoint_dir,
    checkpoint_save_steps=5000,
    checkpoint_save_total_limit=3,
    resume_from_checkpoint=resume_checkpoint,
    callback=eval_callback  # ✅ 记录每次评估结果
)

log("✅ 训练完成。模型已保存到: " + base_model_dir)
