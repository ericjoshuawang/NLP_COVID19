# NLP_COVID19
Final Project for UVA CS4501-MMM

Project members: Eric Wang, Serena Jiao, Megan Cheng, Christine Cheng

## Disclaimer
This project is based on the work of [DMIS-Lab](https://dmis.korea.ac.kr) including [BioBERT](https://github.com/dmis-lab/biobert/blob/master) and [covidAsk](https://github.com/dmis-lab/covidAsk/blob/master).

## Introduction
Given the rapid spreading of COVID19 worldwide and an abundance of manuscript preprints with critical findings regarding this pandemic being published daily, we believe that a machine learning method that summarizes and extracts information from the large and unstructured corpus will be beneficial to this ongoing fight. The more we learn about the virus, the more prepared we are to fight against it. In particular, we hope our model can provide answers to the following questions:
* What is the range of incubation periods for the disease in humans?
* How long are individuals contagious?

With these extracted information from reliable publications, governments and organizations can make adjustments on their policies and precautions.

## Previous Work
[BioBERT](https://github.com/dmis-lab/biobert/blob/master) is a 

## Data
Kaggle COVID-19 Open Research Dataset Challenge ([CORD-19](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)) provided 8GB of manuscript data that is not annotated. 

CORD-19 data was downloaded with the Kaggle API installed 

```bash
$ pip install kaggle
$ kaggle datasets download allen-institute-for-ai/CORD-19-research-challenge
```
