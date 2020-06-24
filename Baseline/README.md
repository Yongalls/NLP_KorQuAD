# Baseline
This directory contains codes for baseline mBERT / KoELECTRA that is used in our experiment.

## Running multilingual BERT
```bash
sh run_nsml_bert.sh
```

## Running KoELECTRA

```bash
sh run_local_electra.sh
```
## Changing hyperparameters in shell

```bash
--start_loss #enables start loss
--answer_loss #enables answer loss
--dropout 0.2 #changes dropout value
--learning_rate 1e-5 #changes learning rate. 

```
