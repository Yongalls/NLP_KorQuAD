#!/usr/bin/env bash

nsml run \
  -m 'kaist korquad open' \
  -d korquad-open-ldbd \
  -g 1 \
  -c 1 \
  -e run_squad.py \
  -a "--model_type electra
    --model_name_or_path monologg/koelectra-base-v2-discriminator
    --do_train
    --do_eval
    --data_dir train
    --num_train_epochs 10
    --per_gpu_train_batch_size 4
    --per_gpu_eval_batch_size 4
    --output_dir output
    --overwrite_output_dir
    --logging_steps 500
    --version_2_with_negative
    --K 5
    --dropout 0.1
    --gradient_accumulation_steps 4
    --learning_rate 1e-5
    "
