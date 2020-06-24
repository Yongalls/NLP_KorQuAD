# EDA
This contains codes for EDA models for our experiments
- Strong_EDA refers to augmenting data for 10% of intensity. 
- Weak_EDA is for 5% of intensity + 1:1 ratio between labeled and unlabeled data. 
- Rampup_EDA ramps up indensity value from 0% to 10% during entire training step. 

## Train in NSML
For EDA method, we only used ELECTRA model. 

```bash
sh run_nsml_electra.sh
```
