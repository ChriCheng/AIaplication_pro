---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:440268
- loss:CosineSimilarityLoss
widget:
- source_sentence: 用手机怎么进淘宝网站
  sentences:
  - 这张图片是什么动漫
  - 手机淘宝网怎么上不去
  - 你听不懂吗
- source_sentence: 一台电动缝纫机当废品卖多少钱？
  sentences:
  - 中国武器最厉害的是什么
  - 请问现在二手平车缝纫机多少钱一台，
  - 打开一下QQ
- source_sentence: 苹果手机怎么删除短信?
  sentences:
  - 让我开始学习吧
  - 苹果手机怎么找回删除的短信
  - 打开照相机
- source_sentence: 微信找出来
  sentences:
  - 奶茶加什么会更稠
  - 迥然不同
  - 给开心发微信
- source_sentence: 有什么好玩的吗
  sentences:
  - 通话时是不是不能上网
  - 感冒了该怎么办
  - 沈阳有什么好玩的
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
- pearson_cosine
- spearman_cosine
model-index:
- name: SentenceTransformer
  results:
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      name: csts dev
      type: csts-dev
    metrics:
    - type: pearson_cosine
      value: 0.7082076419785658
      name: Pearson Cosine
    - type: spearman_cosine
      value: 0.6910989860608941
      name: Spearman Cosine
---

# SentenceTransformer

This is a [sentence-transformers](https://www.SBERT.net) model trained. It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
<!-- - **Base model:** [Unknown](https://huggingface.co/unknown) -->
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
    '有什么好玩的吗',
    '沈阳有什么好玩的',
    '感冒了该怎么办',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 768]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[ 1.0000,  0.0244, -0.0672],
#         [ 0.0244,  1.0000,  0.2665],
#         [-0.0672,  0.2665,  1.0000]])
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
| pearson_cosine      | 0.7082     |
| **spearman_cosine** | **0.6911** |

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
  | details | <ul><li>min: 4 tokens</li><li>mean: 11.35 tokens</li><li>max: 40 tokens</li></ul> | <ul><li>min: 5 tokens</li><li>mean: 11.71 tokens</li><li>max: 46 tokens</li></ul> | <ul><li>min: 0.0</li><li>mean: 0.46</li><li>max: 1.0</li></ul> |
* Samples:
  | sentence_0                   | sentence_1                     | label            |
  |:-----------------------------|:-------------------------------|:-----------------|
  | <code>好看的韩国爱情喜剧电影!</code>    | <code>介绍些好看的香港爱情喜剧电影</code>    | <code>0.0</code> |
  | <code>一台电动缝纫机当废品卖多少钱？</code> | <code>请问现在二手平车缝纫机多少钱一台，</code> | <code>0.0</code> |
  | <code>谁有好看的狼图片</code>        | <code>谁见过杨幂的这张照片？</code>       | <code>0.0</code> |
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
| 0.0073 | 200   | -             | 0.6638                   |
| 0.0145 | 400   | -             | 0.6740                   |
| 0.0182 | 500   | 0.0844        | -                        |
| 0.0218 | 600   | -             | 0.6757                   |
| 0.0291 | 800   | -             | 0.6717                   |
| 0.0363 | 1000  | 0.0846        | 0.6719                   |
| 0.0436 | 1200  | -             | 0.6575                   |
| 0.0509 | 1400  | -             | 0.6704                   |
| 0.0545 | 1500  | 0.0862        | -                        |
| 0.0581 | 1600  | -             | 0.6662                   |
| 0.0654 | 1800  | -             | 0.6718                   |
| 0.0727 | 2000  | 0.0869        | 0.6677                   |
| 0.0800 | 2200  | -             | 0.6779                   |
| 0.0872 | 2400  | -             | 0.6746                   |
| 0.0909 | 2500  | 0.0876        | -                        |
| 0.0945 | 2600  | -             | 0.6712                   |
| 0.1018 | 2800  | -             | 0.6692                   |
| 0.1090 | 3000  | 0.087         | 0.6642                   |
| 0.1163 | 3200  | -             | 0.6631                   |
| 0.1236 | 3400  | -             | 0.6605                   |
| 0.1272 | 3500  | 0.0901        | -                        |
| 0.1308 | 3600  | -             | 0.6663                   |
| 0.1381 | 3800  | -             | 0.6683                   |
| 0.1454 | 4000  | 0.0889        | 0.6697                   |
| 0.1526 | 4200  | -             | 0.6683                   |
| 0.1599 | 4400  | -             | 0.6612                   |
| 0.1635 | 4500  | 0.0865        | -                        |
| 0.1672 | 4600  | -             | 0.6643                   |
| 0.1744 | 4800  | -             | 0.6681                   |
| 0.1817 | 5000  | 0.0897        | 0.6668                   |
| 0.1890 | 5200  | -             | 0.6759                   |
| 0.1962 | 5400  | -             | 0.6686                   |
| 0.1999 | 5500  | 0.0897        | -                        |
| 0.2035 | 5600  | -             | 0.6689                   |
| 0.2108 | 5800  | -             | 0.6586                   |
| 0.2180 | 6000  | 0.0877        | 0.6704                   |
| 0.2253 | 6200  | -             | 0.6669                   |
| 0.2326 | 6400  | -             | 0.6709                   |
| 0.2362 | 6500  | 0.0907        | -                        |
| 0.2399 | 6600  | -             | 0.6705                   |
| 0.2471 | 6800  | -             | 0.6715                   |
| 0.2544 | 7000  | 0.0862        | 0.6648                   |
| 0.2617 | 7200  | -             | 0.6673                   |
| 0.2689 | 7400  | -             | 0.6703                   |
| 0.2726 | 7500  | 0.0898        | -                        |
| 0.2762 | 7600  | -             | 0.6696                   |
| 0.2835 | 7800  | -             | 0.6662                   |
| 0.2907 | 8000  | 0.089         | 0.6677                   |
| 0.2980 | 8200  | -             | 0.6691                   |
| 0.3053 | 8400  | -             | 0.6731                   |
| 0.3089 | 8500  | 0.0907        | -                        |
| 0.3125 | 8600  | -             | 0.6706                   |
| 0.3198 | 8800  | -             | 0.6668                   |
| 0.3271 | 9000  | 0.0909        | 0.6701                   |
| 0.3343 | 9200  | -             | 0.6735                   |
| 0.3416 | 9400  | -             | 0.6712                   |
| 0.3452 | 9500  | 0.0907        | -                        |
| 0.3489 | 9600  | -             | 0.6690                   |
| 0.3561 | 9800  | -             | 0.6655                   |
| 0.3634 | 10000 | 0.0902        | 0.6626                   |
| 0.3707 | 10200 | -             | 0.6708                   |
| 0.3779 | 10400 | -             | 0.6631                   |
| 0.3816 | 10500 | 0.0874        | -                        |
| 0.3852 | 10600 | -             | 0.6703                   |
| 0.3925 | 10800 | -             | 0.6725                   |
| 0.3998 | 11000 | 0.0893        | 0.6682                   |
| 0.4070 | 11200 | -             | 0.6727                   |
| 0.4143 | 11400 | -             | 0.6742                   |
| 0.4179 | 11500 | 0.0919        | -                        |
| 0.4216 | 11600 | -             | 0.6730                   |
| 0.4288 | 11800 | -             | 0.6721                   |
| 0.4361 | 12000 | 0.09          | 0.6738                   |
| 0.4434 | 12200 | -             | 0.6596                   |
| 0.4506 | 12400 | -             | 0.6714                   |
| 0.4543 | 12500 | 0.0864        | -                        |
| 0.4579 | 12600 | -             | 0.6675                   |
| 0.4652 | 12800 | -             | 0.6745                   |
| 0.4724 | 13000 | 0.0898        | 0.6750                   |
| 0.4797 | 13200 | -             | 0.6699                   |
| 0.4870 | 13400 | -             | 0.6745                   |
| 0.4906 | 13500 | 0.091         | -                        |
| 0.4942 | 13600 | -             | 0.6725                   |
| 0.5015 | 13800 | -             | 0.6713                   |
| 0.5088 | 14000 | 0.0887        | 0.6683                   |
| 0.5160 | 14200 | -             | 0.6738                   |
| 0.5233 | 14400 | -             | 0.6730                   |
| 0.5269 | 14500 | 0.089         | -                        |
| 0.5306 | 14600 | -             | 0.6708                   |
| 0.5378 | 14800 | -             | 0.6724                   |
| 0.5451 | 15000 | 0.0881        | 0.6717                   |
| 0.5524 | 15200 | -             | 0.6727                   |
| 0.5597 | 15400 | -             | 0.6679                   |
| 0.5633 | 15500 | 0.0907        | -                        |
| 0.5669 | 15600 | -             | 0.6763                   |
| 0.5742 | 15800 | -             | 0.6760                   |
| 0.5815 | 16000 | 0.0871        | 0.6801                   |
| 0.5887 | 16200 | -             | 0.6790                   |
| 0.5960 | 16400 | -             | 0.6747                   |
| 0.5996 | 16500 | 0.0893        | -                        |
| 0.6033 | 16600 | -             | 0.6759                   |
| 0.6105 | 16800 | -             | 0.6802                   |
| 0.6178 | 17000 | 0.0919        | 0.6795                   |
| 0.6251 | 17200 | -             | 0.6806                   |
| 0.6323 | 17400 | -             | 0.6790                   |
| 0.6360 | 17500 | 0.09          | -                        |
| 0.6396 | 17600 | -             | 0.6726                   |
| 0.6469 | 17800 | -             | 0.6743                   |
| 0.6541 | 18000 | 0.0884        | 0.6739                   |
| 0.6614 | 18200 | -             | 0.6735                   |
| 0.6687 | 18400 | -             | 0.6779                   |
| 0.6723 | 18500 | 0.0852        | -                        |
| 0.6759 | 18600 | -             | 0.6770                   |
| 0.6832 | 18800 | -             | 0.6760                   |
| 0.6905 | 19000 | 0.089         | 0.6765                   |
| 0.6978 | 19200 | -             | 0.6749                   |
| 0.7050 | 19400 | -             | 0.6821                   |
| 0.7087 | 19500 | 0.0867        | -                        |
| 0.7123 | 19600 | -             | 0.6769                   |
| 0.7196 | 19800 | -             | 0.6726                   |
| 0.7268 | 20000 | 0.0874        | 0.6813                   |
| 0.7341 | 20200 | -             | 0.6755                   |
| 0.7414 | 20400 | -             | 0.6802                   |
| 0.7450 | 20500 | 0.0894        | -                        |
| 0.7486 | 20600 | -             | 0.6769                   |
| 0.7559 | 20800 | -             | 0.6744                   |
| 0.7632 | 21000 | 0.0899        | 0.6778                   |
| 0.7704 | 21200 | -             | 0.6794                   |
| 0.7777 | 21400 | -             | 0.6807                   |
| 0.7813 | 21500 | 0.0881        | -                        |
| 0.7850 | 21600 | -             | 0.6801                   |
| 0.7922 | 21800 | -             | 0.6772                   |
| 0.7995 | 22000 | 0.0889        | 0.6789                   |
| 0.8068 | 22200 | -             | 0.6806                   |
| 0.8140 | 22400 | -             | 0.6793                   |
| 0.8177 | 22500 | 0.0885        | -                        |
| 0.8213 | 22600 | -             | 0.6847                   |
| 0.8286 | 22800 | -             | 0.6830                   |
| 0.8358 | 23000 | 0.0885        | 0.6824                   |
| 0.8431 | 23200 | -             | 0.6811                   |
| 0.8504 | 23400 | -             | 0.6792                   |
| 0.8540 | 23500 | 0.0882        | -                        |
| 0.8577 | 23600 | -             | 0.6805                   |
| 0.8649 | 23800 | -             | 0.6816                   |
| 0.8722 | 24000 | 0.0888        | 0.6779                   |
| 0.8795 | 24200 | -             | 0.6788                   |
| 0.8867 | 24400 | -             | 0.6792                   |
| 0.8904 | 24500 | 0.0881        | -                        |
| 0.8940 | 24600 | -             | 0.6761                   |
| 0.9013 | 24800 | -             | 0.6752                   |
| 0.9085 | 25000 | 0.089         | 0.6821                   |
| 0.9158 | 25200 | -             | 0.6807                   |
| 0.9231 | 25400 | -             | 0.6858                   |
| 0.9267 | 25500 | 0.0872        | -                        |
| 0.9303 | 25600 | -             | 0.6813                   |
| 0.9376 | 25800 | -             | 0.6794                   |
| 0.9449 | 26000 | 0.0892        | 0.6827                   |
| 0.9521 | 26200 | -             | 0.6799                   |
| 0.9594 | 26400 | -             | 0.6823                   |
| 0.9630 | 26500 | 0.0888        | -                        |
| 0.9667 | 26600 | -             | 0.6802                   |
| 0.9739 | 26800 | -             | 0.6753                   |
| 0.9812 | 27000 | 0.0872        | 0.6774                   |
| 0.9885 | 27200 | -             | 0.6778                   |
| 0.9957 | 27400 | -             | 0.6710                   |
| 0.9994 | 27500 | 0.0872        | -                        |
| 1.0    | 27517 | -             | 0.6805                   |
| 1.0030 | 27600 | -             | 0.6808                   |
| 1.0103 | 27800 | -             | 0.6841                   |
| 1.0176 | 28000 | 0.0694        | 0.6764                   |
| 1.0248 | 28200 | -             | 0.6860                   |
| 1.0321 | 28400 | -             | 0.6815                   |
| 1.0357 | 28500 | 0.0734        | -                        |
| 1.0394 | 28600 | -             | 0.6832                   |
| 1.0466 | 28800 | -             | 0.6799                   |
| 1.0539 | 29000 | 0.0698        | 0.6813                   |
| 1.0612 | 29200 | -             | 0.6797                   |
| 1.0684 | 29400 | -             | 0.6820                   |
| 1.0721 | 29500 | 0.0711        | -                        |
| 1.0757 | 29600 | -             | 0.6799                   |
| 1.0830 | 29800 | -             | 0.6744                   |
| 1.0902 | 30000 | 0.0685        | 0.6758                   |
| 1.0975 | 30200 | -             | 0.6767                   |
| 1.1048 | 30400 | -             | 0.6810                   |
| 1.1084 | 30500 | 0.0738        | -                        |
| 1.1120 | 30600 | -             | 0.6765                   |
| 1.1193 | 30800 | -             | 0.6797                   |
| 1.1266 | 31000 | 0.0686        | 0.6812                   |
| 1.1338 | 31200 | -             | 0.6790                   |
| 1.1411 | 31400 | -             | 0.6811                   |
| 1.1447 | 31500 | 0.0708        | -                        |
| 1.1484 | 31600 | -             | 0.6794                   |
| 1.1556 | 31800 | -             | 0.6802                   |
| 1.1629 | 32000 | 0.0717        | 0.6808                   |
| 1.1702 | 32200 | -             | 0.6739                   |
| 1.1775 | 32400 | -             | 0.6772                   |
| 1.1811 | 32500 | 0.0703        | -                        |
| 1.1847 | 32600 | -             | 0.6791                   |
| 1.1920 | 32800 | -             | 0.6846                   |
| 1.1993 | 33000 | 0.0736        | 0.6810                   |
| 1.2065 | 33200 | -             | 0.6788                   |
| 1.2138 | 33400 | -             | 0.6774                   |
| 1.2174 | 33500 | 0.0721        | -                        |
| 1.2211 | 33600 | -             | 0.6811                   |
| 1.2283 | 33800 | -             | 0.6824                   |
| 1.2356 | 34000 | 0.0712        | 0.6786                   |
| 1.2429 | 34200 | -             | 0.6789                   |
| 1.2501 | 34400 | -             | 0.6779                   |
| 1.2538 | 34500 | 0.0704        | -                        |
| 1.2574 | 34600 | -             | 0.6762                   |
| 1.2647 | 34800 | -             | 0.6752                   |
| 1.2719 | 35000 | 0.0708        | 0.6749                   |
| 1.2792 | 35200 | -             | 0.6779                   |
| 1.2865 | 35400 | -             | 0.6842                   |
| 1.2901 | 35500 | 0.0697        | -                        |
| 1.2937 | 35600 | -             | 0.6835                   |
| 1.3010 | 35800 | -             | 0.6826                   |
| 1.3083 | 36000 | 0.0726        | 0.6821                   |
| 1.3156 | 36200 | -             | 0.6820                   |
| 1.3228 | 36400 | -             | 0.6773                   |
| 1.3265 | 36500 | 0.0727        | -                        |
| 1.3301 | 36600 | -             | 0.6820                   |
| 1.3374 | 36800 | -             | 0.6804                   |
| 1.3446 | 37000 | 0.071         | 0.6807                   |
| 1.3519 | 37200 | -             | 0.6788                   |
| 1.3592 | 37400 | -             | 0.6861                   |
| 1.3628 | 37500 | 0.0706        | -                        |
| 1.3664 | 37600 | -             | 0.6824                   |
| 1.3737 | 37800 | -             | 0.6787                   |
| 1.3810 | 38000 | 0.0735        | 0.6829                   |
| 1.3882 | 38200 | -             | 0.6820                   |
| 1.3955 | 38400 | -             | 0.6834                   |
| 1.3991 | 38500 | 0.073         | -                        |
| 1.4028 | 38600 | -             | 0.6851                   |
| 1.4100 | 38800 | -             | 0.6811                   |
| 1.4173 | 39000 | 0.072         | 0.6838                   |
| 1.4246 | 39200 | -             | 0.6826                   |
| 1.4318 | 39400 | -             | 0.6857                   |
| 1.4355 | 39500 | 0.0733        | -                        |
| 1.4391 | 39600 | -             | 0.6830                   |
| 1.4464 | 39800 | -             | 0.6840                   |
| 1.4536 | 40000 | 0.0722        | 0.6853                   |
| 1.4609 | 40200 | -             | 0.6818                   |
| 1.4682 | 40400 | -             | 0.6827                   |
| 1.4718 | 40500 | 0.0712        | -                        |
| 1.4755 | 40600 | -             | 0.6791                   |
| 1.4827 | 40800 | -             | 0.6846                   |
| 1.4900 | 41000 | 0.0713        | 0.6810                   |
| 1.4973 | 41200 | -             | 0.6829                   |
| 1.5045 | 41400 | -             | 0.6843                   |
| 1.5082 | 41500 | 0.0715        | -                        |
| 1.5118 | 41600 | -             | 0.6819                   |
| 1.5191 | 41800 | -             | 0.6870                   |
| 1.5263 | 42000 | 0.0716        | 0.6847                   |
| 1.5336 | 42200 | -             | 0.6857                   |
| 1.5409 | 42400 | -             | 0.6813                   |
| 1.5445 | 42500 | 0.0721        | -                        |
| 1.5481 | 42600 | -             | 0.6866                   |
| 1.5554 | 42800 | -             | 0.6833                   |
| 1.5627 | 43000 | 0.074         | 0.6839                   |
| 1.5699 | 43200 | -             | 0.6853                   |
| 1.5772 | 43400 | -             | 0.6846                   |
| 1.5808 | 43500 | 0.0717        | -                        |
| 1.5845 | 43600 | -             | 0.6887                   |
| 1.5917 | 43800 | -             | 0.6871                   |
| 1.5990 | 44000 | 0.0714        | 0.6796                   |
| 1.6063 | 44200 | -             | 0.6806                   |
| 1.6135 | 44400 | -             | 0.6848                   |
| 1.6172 | 44500 | 0.0693        | -                        |
| 1.6208 | 44600 | -             | 0.6850                   |
| 1.6281 | 44800 | -             | 0.6818                   |
| 1.6354 | 45000 | 0.0687        | 0.6864                   |
| 1.6426 | 45200 | -             | 0.6863                   |
| 1.6499 | 45400 | -             | 0.6902                   |
| 1.6535 | 45500 | 0.0765        | -                        |
| 1.6572 | 45600 | -             | 0.6894                   |
| 1.6644 | 45800 | -             | 0.6885                   |
| 1.6717 | 46000 | 0.0701        | 0.6817                   |
| 1.6790 | 46200 | -             | 0.6888                   |
| 1.6862 | 46400 | -             | 0.6838                   |
| 1.6899 | 46500 | 0.0725        | -                        |
| 1.6935 | 46600 | -             | 0.6786                   |
| 1.7008 | 46800 | -             | 0.6876                   |
| 1.7080 | 47000 | 0.0709        | 0.6866                   |
| 1.7153 | 47200 | -             | 0.6866                   |
| 1.7226 | 47400 | -             | 0.6868                   |
| 1.7262 | 47500 | 0.0716        | -                        |
| 1.7298 | 47600 | -             | 0.6883                   |
| 1.7371 | 47800 | -             | 0.6890                   |
| 1.7444 | 48000 | 0.0705        | 0.6843                   |
| 1.7516 | 48200 | -             | 0.6816                   |
| 1.7589 | 48400 | -             | 0.6860                   |
| 1.7625 | 48500 | 0.0701        | -                        |
| 1.7662 | 48600 | -             | 0.6879                   |
| 1.7734 | 48800 | -             | 0.6886                   |
| 1.7807 | 49000 | 0.0702        | 0.6870                   |
| 1.7880 | 49200 | -             | 0.6874                   |
| 1.7953 | 49400 | -             | 0.6867                   |
| 1.7989 | 49500 | 0.0717        | -                        |
| 1.8025 | 49600 | -             | 0.6822                   |
| 1.8098 | 49800 | -             | 0.6853                   |
| 1.8171 | 50000 | 0.0682        | 0.6866                   |
| 1.8243 | 50200 | -             | 0.6876                   |
| 1.8316 | 50400 | -             | 0.6846                   |
| 1.8352 | 50500 | 0.07          | -                        |
| 1.8389 | 50600 | -             | 0.6829                   |
| 1.8461 | 50800 | -             | 0.6850                   |
| 1.8534 | 51000 | 0.0712        | 0.6856                   |
| 1.8607 | 51200 | -             | 0.6788                   |
| 1.8679 | 51400 | -             | 0.6862                   |
| 1.8716 | 51500 | 0.0692        | -                        |
| 1.8752 | 51600 | -             | 0.6866                   |
| 1.8825 | 51800 | -             | 0.6853                   |
| 1.8897 | 52000 | 0.0704        | 0.6869                   |
| 1.8970 | 52200 | -             | 0.6882                   |
| 1.9043 | 52400 | -             | 0.6881                   |
| 1.9079 | 52500 | 0.0692        | -                        |
| 1.9115 | 52600 | -             | 0.6856                   |
| 1.9188 | 52800 | -             | 0.6899                   |
| 1.9261 | 53000 | 0.0707        | 0.6902                   |
| 1.9334 | 53200 | -             | 0.6911                   |

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