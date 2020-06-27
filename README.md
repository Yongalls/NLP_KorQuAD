# Project_Title
Final Project for KAIST CS492H: Special Topics in Computer Science<Deep Learning for Real-world Problems.<br>
done by Donghyun Kim([Github](https://github.com/chocolatefudge)) / Yongmin Lee([Github](https://github.com/Yongalls)). 

## Abstract
Recent trends in Natural Language Processing is mostly about gigantic, unsupervised pre-trained language models that could be fine-tuned for many target tasks. It dominates most of the NLP tasks including question answering. However, specific fine-tuning methodologies are not well provided in most of the question-answering task. Performing pre/post-processing or architectural change might bring improvements to our model. Therefore, in this research, we make an effort to find a strategy that is especially well suitable for question answering task with korquad-open dataset. 

## Report
You can check our specific experiment results and analysis on cs492h_nlp_report_15.pdf

## Overall Structure
Our GitHub repo is divided into 5 parts. Please keep in mind that all codes in here are for NSML environment, not in local machines.  <br>

 - Baseline
 - EDA
 - Self_Distillation 
 - Experiment_codes 
 - previous models

## Baseline
Contains code for baseline model changing (BERT / ELECTRA), hyperparameter tuning, and loss function modification. 
This directory corresponds to experiment 1,2,3 in our report. 

## EDA
Contains code for EDA(Easy Data Augmentation) methods applied on ELECTRA model. 
This directory corresponds to experiment 4 in our report. 

## Self_Distillation
Contains code for SDA / SDV structured distillation model. 
This directory corresponds to experiment 5 in our report. 

## Experiment_codes
Contains exact codes which is used for our data in presentation and report. 
Specific description about session number and experiments are in "Experiment_codes/Experiment Data.pdf"

## previous models 
Various codes resulted from our trial&error.

## Original Author
Seonhoon Kim (Naver)
