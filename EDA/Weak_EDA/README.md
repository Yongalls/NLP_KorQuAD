# Weak EDA
Weak EDA model (augmentation ratio = 5%).  
Especially in this model, we used also original(unaugmented) data for training. Ratio of augmented data and original data is 1:1 and both have only 2 contexts per question.

## Train in NSML
For EDA method, we only used ELECTRA model.

```bash
sh run_nsml_electra.sh
```
