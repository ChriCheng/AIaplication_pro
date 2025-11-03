#传统方法计算文本相似度（TF-IDF baseline）
import json
import os
import numpy as np
from tqdm import tqdm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import accuracy_score, f1_score

DATASET = "CSTS_preprocessed/LCQMC"  # 可切换为任意子集
SPLIT = "test.json"

# === 读取数据 ===
data = [json.loads(line) for line in open(os.path.join(DATASET, SPLIT), "r", encoding="utf-8")]
s1 = [d["sentence1"] for d in data]
s2 = [d["sentence2"] for d in data]
labels = [int(d["label"]) for d in data]

# === 构建TF-IDF向量 ===
corpus = s1 + s2
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(corpus)
v1, v2 = vectors[:len(s1)], vectors[len(s1):]

# === 计算余弦相似度 ===
scores = cosine_similarity(v1, v2).diagonal()  # 对应行对相似度
preds = (scores > 0.5).astype(int)  # 阈值可调

# === 输出评估指标 ===
acc = accuracy_score(labels, preds)
f1 = f1_score(labels, preds)
print(f"✅ TF-IDF Baseline on {DATASET}: ACC={acc:.4f}, F1={f1:.4f}")
