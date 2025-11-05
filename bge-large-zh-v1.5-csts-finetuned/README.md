---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:440268
- loss:CosineSimilarityLoss
base_model: BAAI/bge-base-zh-v1.5
widget:
- source_sentence: 你在我身边好不好
  sentences:
  - 梅西为什么没在世界杯上进球
  - 你一定会一直在身边吗
  - 什么杯子喝茶好？
- source_sentence: 练字买什么字帖好
  sentences:
  - 长发好还是短发好
  - 什么字帖练字好
  - 你在那里，干嘛
- source_sentence: 马云和李嘉诚谁更有钱
  sentences:
  - 求闪金镇那一夜的动画。
  - 李嘉诚和马云谁最有钱
  - 上海有什么好厂?
- source_sentence: 亲，是您有开通花呗的吗
  sentences:
  - 逾期费用的计算公式：逾期费用=逾期金额*逾期天数*0.05%
  - 各位大神求出处阿！
  - 稍等我查一下您的额店铺是有开通花呗吗
- source_sentence: 本期双色球开奖号码
  sentences:
  - 京东买东西怎么换？
  - 妈妈快生日了！不知道送什么礼物好
  - 福彩3D开奖结果
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
- pearson_cosine
- spearman_cosine
model-index:
- name: SentenceTransformer based on BAAI/bge-base-zh-v1.5
  results:
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      name: csts dev
      type: csts-dev
    metrics:
    - type: pearson_cosine
      value: 0.6935277861882515
      name: Pearson Cosine
    - type: spearman_cosine
      value: 0.6848100091232606
      name: Spearman Cosine
---

# SentenceTransformer based on BAAI/bge-base-zh-v1.5

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [BAAI/bge-base-zh-v1.5](https://huggingface.co/BAAI/bge-base-zh-v1.5). It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [BAAI/bge-base-zh-v1.5](https://huggingface.co/BAAI/bge-base-zh-v1.5) <!-- at revision f03589ceff5aac7111bd60cfc7d497ca17ecac65 -->
- **Maximum Sequence Length:** 512 tokens
- **Output Dimensionality:** 768 dimensions
- **Similarity Function:** Cosine Similarity
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 512, 'do_lower_case': True, 'architecture': 'BertModel'})
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': True, 'pooling_mode_mean_tokens': False, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
  (2): Normalize()
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```

Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
sentences = [
    '本期双色球开奖号码',
    '福彩3D开奖结果',
    '妈妈快生日了！不知道送什么礼物好',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 768]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[1.0000, 0.0570, 0.0646],
#         [0.0570, 1.0000, 0.0584],
#         [0.0646, 0.0584, 1.0000]])
```

<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

## Evaluation

### Metrics

#### Semantic Similarity

* Dataset: `csts-dev`
* Evaluated with [<code>EmbeddingSimilarityEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.EmbeddingSimilarityEvaluator)

| Metric              | Value      |
|:--------------------|:-----------|
| pearson_cosine      | 0.6935     |
| **spearman_cosine** | **0.6848** |

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### Unnamed Dataset

* Size: 440,268 training samples
* Columns: <code>sentence_0</code>, <code>sentence_1</code>, and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | sentence_0                                                                        | sentence_1                                                                        | label                                                          |
  |:--------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|:---------------------------------------------------------------|
  | type    | string                                                                            | string                                                                            | float                                                          |
  | details | <ul><li>min: 4 tokens</li><li>mean: 11.49 tokens</li><li>max: 38 tokens</li></ul> | <ul><li>min: 5 tokens</li><li>mean: 11.82 tokens</li><li>max: 60 tokens</li></ul> | <ul><li>min: 0.0</li><li>mean: 0.47</li><li>max: 1.0</li></ul> |
* Samples:
  | sentence_0                 | sentence_1                   | label            |
  |:---------------------------|:-----------------------------|:-----------------|
  | <code>微信视频美颜是否只能用手机</code> | <code>微信视频美颜机能有没有</code>     | <code>1.0</code> |
  | <code>什么银行的信用卡最好</code>    | <code>什么银行信用卡最好用</code>      | <code>1.0</code> |
  | <code>头上长了一个小包，一摸就疼</code> | <code>我的头上长了一个包，已经好久了</code> | <code>0.0</code> |
* Loss: [<code>CosineSimilarityLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#cosinesimilarityloss) with these parameters:
  ```json
  {
      "loss_fct": "torch.nn.modules.loss.MSELoss"
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `eval_strategy`: steps
- `per_device_train_batch_size`: 16
- `per_device_eval_batch_size`: 16
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: steps
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 16
- `per_device_eval_batch_size`: 16
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 5e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1
- `num_train_epochs`: 3
- `max_steps`: -1
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: {}
- `warmup_ratio`: 0.0
- `warmup_steps`: 0
- `log_level`: passive
- `log_level_replica`: warning
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `save_safetensors`: True
- `save_on_each_node`: False
- `save_only_model`: False
- `restore_callback_states_from_checkpoint`: False
- `no_cuda`: False
- `use_cpu`: False
- `use_mps_device`: False
- `seed`: 42
- `data_seed`: None
- `jit_mode_eval`: False
- `bf16`: False
- `fp16`: False
- `fp16_opt_level`: O1
- `half_precision_backend`: auto
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `local_rank`: 0
- `ddp_backend`: None
- `tpu_num_cores`: None
- `tpu_metrics_debug`: False
- `debug`: []
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_prefetch_factor`: None
- `past_index`: -1
- `disable_tqdm`: False
- `remove_unused_columns`: True
- `label_names`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `fsdp`: []
- `fsdp_min_num_params`: 0
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `fsdp_transformer_layer_cls_to_wrap`: None
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `parallelism_config`: None
- `deepspeed`: None
- `label_smoothing_factor`: 0.0
- `optim`: adamw_torch_fused
- `optim_args`: None
- `adafactor`: False
- `group_by_length`: False
- `length_column_name`: length
- `project`: huggingface
- `trackio_space_id`: trackio
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `skip_memory_metrics`: True
- `use_legacy_prediction_loop`: False
- `push_to_hub`: False
- `resume_from_checkpoint`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_private_repo`: None
- `hub_always_push`: False
- `hub_revision`: None
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `include_inputs_for_metrics`: False
- `include_for_metrics`: []
- `eval_do_concat_batches`: True
- `fp16_backend`: auto
- `push_to_hub_model_id`: None
- `push_to_hub_organization`: None
- `mp_parameters`: 
- `auto_find_batch_size`: False
- `full_determinism`: False
- `torchdynamo`: None
- `ray_scope`: last
- `ddp_timeout`: 1800
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `include_tokens_per_second`: False
- `include_num_input_tokens_seen`: no
- `neftune_noise_alpha`: None
- `optim_target_modules`: None
- `batch_eval_metrics`: False
- `eval_on_start`: False
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `eval_use_gather_object`: False
- `average_tokens_across_devices`: True
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: round_robin
- `router_mapping`: {}
- `learning_rate_mapping`: {}

</details>

### Training Logs
<details><summary>Click to expand</summary>

| Epoch  | Step  | Training Loss | csts-dev_spearman_cosine |
|:------:|:-----:|:-------------:|:------------------------:|
| 0.0073 | 200   | -             | 0.5858                   |
| 0.0145 | 400   | -             | 0.5988                   |
| 0.0182 | 500   | 0.1502        | -                        |
| 0.0218 | 600   | -             | 0.6100                   |
| 0.0291 | 800   | -             | 0.6137                   |
| 0.0363 | 1000  | 0.1364        | 0.6124                   |
| 0.0436 | 1200  | -             | 0.6069                   |
| 0.0509 | 1400  | -             | 0.6064                   |
| 0.0545 | 1500  | 0.1296        | -                        |
| 0.0581 | 1600  | -             | 0.6212                   |
| 0.0654 | 1800  | -             | 0.6202                   |
| 0.0727 | 2000  | 0.1297        | 0.6087                   |
| 0.0800 | 2200  | -             | 0.6075                   |
| 0.0872 | 2400  | -             | 0.6225                   |
| 0.0909 | 2500  | 0.1291        | -                        |
| 0.0945 | 2600  | -             | 0.6173                   |
| 0.1018 | 2800  | -             | 0.6361                   |
| 0.1090 | 3000  | 0.1279        | 0.6266                   |
| 0.1163 | 3200  | -             | 0.6174                   |
| 0.1236 | 3400  | -             | 0.6164                   |
| 0.1272 | 3500  | 0.1236        | -                        |
| 0.1308 | 3600  | -             | 0.6202                   |
| 0.1381 | 3800  | -             | 0.6180                   |
| 0.1454 | 4000  | 0.1228        | 0.6274                   |
| 0.1526 | 4200  | -             | 0.6165                   |
| 0.1599 | 4400  | -             | 0.6302                   |
| 0.1635 | 4500  | 0.1242        | -                        |
| 0.1672 | 4600  | -             | 0.6194                   |
| 0.1744 | 4800  | -             | 0.6173                   |
| 0.1817 | 5000  | 0.1214        | 0.6235                   |
| 0.1890 | 5200  | -             | 0.6292                   |
| 0.1962 | 5400  | -             | 0.6366                   |
| 0.1999 | 5500  | 0.1249        | -                        |
| 0.2035 | 5600  | -             | 0.6361                   |
| 0.2108 | 5800  | -             | 0.6228                   |
| 0.2180 | 6000  | 0.1233        | 0.6307                   |
| 0.2253 | 6200  | -             | 0.6376                   |
| 0.2326 | 6400  | -             | 0.6439                   |
| 0.2362 | 6500  | 0.1235        | -                        |
| 0.2399 | 6600  | -             | 0.6324                   |
| 0.2471 | 6800  | -             | 0.6417                   |
| 0.2544 | 7000  | 0.1224        | 0.6348                   |
| 0.2617 | 7200  | -             | 0.6320                   |
| 0.2689 | 7400  | -             | 0.6403                   |
| 0.2726 | 7500  | 0.1169        | -                        |
| 0.2762 | 7600  | -             | 0.6357                   |
| 0.2835 | 7800  | -             | 0.6263                   |
| 0.2907 | 8000  | 0.1147        | 0.6336                   |
| 0.2980 | 8200  | -             | 0.6368                   |
| 0.3053 | 8400  | -             | 0.6329                   |
| 0.3089 | 8500  | 0.1194        | -                        |
| 0.3125 | 8600  | -             | 0.6362                   |
| 0.3198 | 8800  | -             | 0.6368                   |
| 0.3271 | 9000  | 0.1186        | 0.6345                   |
| 0.3343 | 9200  | -             | 0.6446                   |
| 0.3416 | 9400  | -             | 0.6408                   |
| 0.3452 | 9500  | 0.1181        | -                        |
| 0.3489 | 9600  | -             | 0.6428                   |
| 0.3561 | 9800  | -             | 0.6456                   |
| 0.3634 | 10000 | 0.1168        | 0.6293                   |
| 0.3707 | 10200 | -             | 0.6458                   |
| 0.3779 | 10400 | -             | 0.6369                   |
| 0.3816 | 10500 | 0.1158        | -                        |
| 0.3852 | 10600 | -             | 0.6428                   |
| 0.3925 | 10800 | -             | 0.6318                   |
| 0.3998 | 11000 | 0.1174        | 0.6414                   |
| 0.4070 | 11200 | -             | 0.6104                   |
| 0.4143 | 11400 | -             | 0.6245                   |
| 0.4179 | 11500 | 0.1144        | -                        |
| 0.4216 | 11600 | -             | 0.6438                   |
| 0.4288 | 11800 | -             | 0.6467                   |
| 0.4361 | 12000 | 0.1147        | 0.6450                   |
| 0.4434 | 12200 | -             | 0.6454                   |
| 0.4506 | 12400 | -             | 0.6448                   |
| 0.4543 | 12500 | 0.115         | -                        |
| 0.4579 | 12600 | -             | 0.6429                   |
| 0.4652 | 12800 | -             | 0.6438                   |
| 0.4724 | 13000 | 0.1154        | 0.6409                   |
| 0.4797 | 13200 | -             | 0.6399                   |
| 0.4870 | 13400 | -             | 0.6520                   |
| 0.4906 | 13500 | 0.1116        | -                        |
| 0.4942 | 13600 | -             | 0.6482                   |
| 0.5015 | 13800 | -             | 0.6507                   |
| 0.5088 | 14000 | 0.1136        | 0.6512                   |
| 0.5160 | 14200 | -             | 0.6429                   |
| 0.5233 | 14400 | -             | 0.6285                   |
| 0.5269 | 14500 | 0.1123        | -                        |
| 0.5306 | 14600 | -             | 0.6307                   |
| 0.5378 | 14800 | -             | 0.6476                   |
| 0.5451 | 15000 | 0.1123        | 0.6525                   |
| 0.5524 | 15200 | -             | 0.6605                   |
| 0.5597 | 15400 | -             | 0.6450                   |
| 0.5633 | 15500 | 0.1147        | -                        |
| 0.5669 | 15600 | -             | 0.6513                   |
| 0.5742 | 15800 | -             | 0.6590                   |
| 0.5815 | 16000 | 0.1158        | 0.6583                   |
| 0.5887 | 16200 | -             | 0.6498                   |
| 0.5960 | 16400 | -             | 0.6571                   |
| 0.5996 | 16500 | 0.1131        | -                        |
| 0.6033 | 16600 | -             | 0.6526                   |
| 0.6105 | 16800 | -             | 0.6337                   |
| 0.6178 | 17000 | 0.1138        | 0.6428                   |
| 0.6251 | 17200 | -             | 0.6452                   |
| 0.6323 | 17400 | -             | 0.6428                   |
| 0.6360 | 17500 | 0.1141        | -                        |
| 0.6396 | 17600 | -             | 0.6493                   |
| 0.6469 | 17800 | -             | 0.6585                   |
| 0.6541 | 18000 | 0.1129        | 0.6531                   |
| 0.6614 | 18200 | -             | 0.6521                   |
| 0.6687 | 18400 | -             | 0.6579                   |
| 0.6723 | 18500 | 0.1142        | -                        |
| 0.6759 | 18600 | -             | 0.6572                   |
| 0.6832 | 18800 | -             | 0.6596                   |
| 0.6905 | 19000 | 0.109         | 0.6622                   |
| 0.6978 | 19200 | -             | 0.6517                   |
| 0.7050 | 19400 | -             | 0.6618                   |
| 0.7087 | 19500 | 0.1122        | -                        |
| 0.7123 | 19600 | -             | 0.6567                   |
| 0.7196 | 19800 | -             | 0.6625                   |
| 0.7268 | 20000 | 0.1099        | 0.6554                   |
| 0.7341 | 20200 | -             | 0.6554                   |
| 0.7414 | 20400 | -             | 0.6638                   |
| 0.7450 | 20500 | 0.1109        | -                        |
| 0.7486 | 20600 | -             | 0.6524                   |
| 0.7559 | 20800 | -             | 0.6624                   |
| 0.7632 | 21000 | 0.1107        | 0.6633                   |
| 0.7704 | 21200 | -             | 0.6643                   |
| 0.7777 | 21400 | -             | 0.6676                   |
| 0.7813 | 21500 | 0.1098        | -                        |
| 0.7850 | 21600 | -             | 0.6650                   |
| 0.7922 | 21800 | -             | 0.6649                   |
| 0.7995 | 22000 | 0.1134        | 0.6686                   |
| 0.8068 | 22200 | -             | 0.6656                   |
| 0.8140 | 22400 | -             | 0.6670                   |
| 0.8177 | 22500 | 0.1092        | -                        |
| 0.8213 | 22600 | -             | 0.6605                   |
| 0.8286 | 22800 | -             | 0.6638                   |
| 0.8358 | 23000 | 0.1075        | 0.6644                   |
| 0.8431 | 23200 | -             | 0.6633                   |
| 0.8504 | 23400 | -             | 0.6645                   |
| 0.8540 | 23500 | 0.1068        | -                        |
| 0.8577 | 23600 | -             | 0.6656                   |
| 0.8649 | 23800 | -             | 0.6654                   |
| 0.8722 | 24000 | 0.1079        | 0.6635                   |
| 0.8795 | 24200 | -             | 0.6698                   |
| 0.8867 | 24400 | -             | 0.6706                   |
| 0.8904 | 24500 | 0.1114        | -                        |
| 0.8940 | 24600 | -             | 0.6712                   |
| 0.9013 | 24800 | -             | 0.6670                   |
| 0.9085 | 25000 | 0.1058        | 0.6583                   |
| 0.9158 | 25200 | -             | 0.6646                   |
| 0.9231 | 25400 | -             | 0.6706                   |
| 0.9267 | 25500 | 0.1067        | -                        |
| 0.9303 | 25600 | -             | 0.6698                   |
| 0.9376 | 25800 | -             | 0.6616                   |
| 0.9449 | 26000 | 0.1078        | 0.6700                   |
| 0.9521 | 26200 | -             | 0.6693                   |
| 0.9594 | 26400 | -             | 0.6655                   |
| 0.9630 | 26500 | 0.1089        | -                        |
| 0.9667 | 26600 | -             | 0.6652                   |
| 0.9739 | 26800 | -             | 0.6664                   |
| 0.9812 | 27000 | 0.1087        | 0.6723                   |
| 0.9885 | 27200 | -             | 0.6655                   |
| 0.9957 | 27400 | -             | 0.6622                   |
| 0.9994 | 27500 | 0.1084        | -                        |
| 1.0    | 27517 | -             | 0.6623                   |
| 1.0030 | 27600 | -             | 0.6725                   |
| 1.0103 | 27800 | -             | 0.6720                   |
| 1.0176 | 28000 | 0.0923        | 0.6669                   |
| 1.0248 | 28200 | -             | 0.6755                   |
| 1.0321 | 28400 | -             | 0.6715                   |
| 1.0357 | 28500 | 0.0938        | -                        |
| 1.0394 | 28600 | -             | 0.6673                   |
| 1.0466 | 28800 | -             | 0.6712                   |
| 1.0539 | 29000 | 0.0933        | 0.6719                   |
| 1.0612 | 29200 | -             | 0.6707                   |
| 1.0684 | 29400 | -             | 0.6686                   |
| 1.0721 | 29500 | 0.0924        | -                        |
| 1.0757 | 29600 | -             | 0.6663                   |
| 1.0830 | 29800 | -             | 0.6692                   |
| 1.0902 | 30000 | 0.0931        | 0.6602                   |
| 1.0975 | 30200 | -             | 0.6617                   |
| 1.1048 | 30400 | -             | 0.6649                   |
| 1.1084 | 30500 | 0.0918        | -                        |
| 1.1120 | 30600 | -             | 0.6624                   |
| 1.1193 | 30800 | -             | 0.6594                   |
| 1.1266 | 31000 | 0.093         | 0.6689                   |
| 1.1338 | 31200 | -             | 0.6688                   |
| 1.1411 | 31400 | -             | 0.6663                   |
| 1.1447 | 31500 | 0.0918        | -                        |
| 1.1484 | 31600 | -             | 0.6700                   |
| 1.1556 | 31800 | -             | 0.6650                   |
| 1.1629 | 32000 | 0.0957        | 0.6721                   |
| 1.1702 | 32200 | -             | 0.6668                   |
| 1.1775 | 32400 | -             | 0.6650                   |
| 1.1811 | 32500 | 0.092         | -                        |
| 1.1847 | 32600 | -             | 0.6720                   |
| 1.1920 | 32800 | -             | 0.6691                   |
| 1.1993 | 33000 | 0.0892        | 0.6670                   |
| 1.2065 | 33200 | -             | 0.6714                   |
| 1.2138 | 33400 | -             | 0.6722                   |
| 1.2174 | 33500 | 0.0907        | -                        |
| 1.2211 | 33600 | -             | 0.6705                   |
| 1.2283 | 33800 | -             | 0.6713                   |
| 1.2356 | 34000 | 0.0903        | 0.6733                   |
| 1.2429 | 34200 | -             | 0.6647                   |
| 1.2501 | 34400 | -             | 0.6787                   |
| 1.2538 | 34500 | 0.0932        | -                        |
| 1.2574 | 34600 | -             | 0.6723                   |
| 1.2647 | 34800 | -             | 0.6585                   |
| 1.2719 | 35000 | 0.094         | 0.6732                   |
| 1.2792 | 35200 | -             | 0.6666                   |
| 1.2865 | 35400 | -             | 0.6712                   |
| 1.2901 | 35500 | 0.0886        | -                        |
| 1.2937 | 35600 | -             | 0.6782                   |
| 1.3010 | 35800 | -             | 0.6710                   |
| 1.3083 | 36000 | 0.0906        | 0.6694                   |
| 1.3156 | 36200 | -             | 0.6693                   |
| 1.3228 | 36400 | -             | 0.6686                   |
| 1.3265 | 36500 | 0.0896        | -                        |
| 1.3301 | 36600 | -             | 0.6740                   |
| 1.3374 | 36800 | -             | 0.6711                   |
| 1.3446 | 37000 | 0.0947        | 0.6699                   |
| 1.3519 | 37200 | -             | 0.6722                   |
| 1.3592 | 37400 | -             | 0.6666                   |
| 1.3628 | 37500 | 0.0883        | -                        |
| 1.3664 | 37600 | -             | 0.6747                   |
| 1.3737 | 37800 | -             | 0.6680                   |
| 1.3810 | 38000 | 0.0853        | 0.6738                   |
| 1.3882 | 38200 | -             | 0.6781                   |
| 1.3955 | 38400 | -             | 0.6796                   |
| 1.3991 | 38500 | 0.0923        | -                        |
| 1.4028 | 38600 | -             | 0.6759                   |
| 1.4100 | 38800 | -             | 0.6778                   |
| 1.4173 | 39000 | 0.0906        | 0.6818                   |
| 1.4246 | 39200 | -             | 0.6796                   |
| 1.4318 | 39400 | -             | 0.6715                   |
| 1.4355 | 39500 | 0.0908        | -                        |
| 1.4391 | 39600 | -             | 0.6765                   |
| 1.4464 | 39800 | -             | 0.6735                   |
| 1.4536 | 40000 | 0.0933        | 0.6786                   |
| 1.4609 | 40200 | -             | 0.6775                   |
| 1.4682 | 40400 | -             | 0.6763                   |
| 1.4718 | 40500 | 0.0941        | -                        |
| 1.4755 | 40600 | -             | 0.6798                   |
| 1.4827 | 40800 | -             | 0.6754                   |
| 1.4900 | 41000 | 0.0915        | 0.6722                   |
| 1.4973 | 41200 | -             | 0.6729                   |
| 1.5045 | 41400 | -             | 0.6706                   |
| 1.5082 | 41500 | 0.0919        | -                        |
| 1.5118 | 41600 | -             | 0.6774                   |
| 1.5191 | 41800 | -             | 0.6767                   |
| 1.5263 | 42000 | 0.0885        | 0.6743                   |
| 1.5336 | 42200 | -             | 0.6750                   |
| 1.5409 | 42400 | -             | 0.6754                   |
| 1.5445 | 42500 | 0.0878        | -                        |
| 1.5481 | 42600 | -             | 0.6689                   |
| 1.5554 | 42800 | -             | 0.6735                   |
| 1.5627 | 43000 | 0.0941        | 0.6765                   |
| 1.5699 | 43200 | -             | 0.6787                   |
| 1.5772 | 43400 | -             | 0.6835                   |
| 1.5808 | 43500 | 0.0935        | -                        |
| 1.5845 | 43600 | -             | 0.6746                   |
| 1.5917 | 43800 | -             | 0.6789                   |
| 1.5990 | 44000 | 0.0897        | 0.6780                   |
| 1.6063 | 44200 | -             | 0.6848                   |

</details>

### Framework Versions
- Python: 3.13.9
- Sentence Transformers: 5.1.2
- Transformers: 4.57.1
- PyTorch: 2.9.0+cu128
- Accelerate: 1.11.0
- Datasets: 4.3.0
- Tokenizers: 0.22.1

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->