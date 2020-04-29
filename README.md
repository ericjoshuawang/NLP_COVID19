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

### BioBERT
[BioBERT](https://github.com/dmis-lab/biobert/blob/master) is a biomedical language representation model designed for biomedical text mining tasks such as biomedical named entity recognition, relation extraction, question answering. 

BioBERT is trained on PubMed manuscripts based on the original BERT model designed by Google AI Language.

**BERT**, or **B**idirectional **E**ncoder **R**epresentations from
**T**ransformers, is a method of pre-training language representations which
obtains state-of-the-art results on a wide array of Natural Language Processing
(NLP) tasks.

The paper on BERT can be found [here](https://arxiv.org/abs/1810.04805).

### SQuAD Fine-tuning

Stanford Question Answering Dataset ([SQuAD](https://rajpurkar.github.io/SQuAD-explorer/)) is a reading comprehension dataset, consisting of questions posed by crowdworkers on a set of Wikipedia articles, where the answer to every question is a segment of text, or span, from the corresponding reading passage, or the question might be unanswerable.

### CovidAsk
[CovidAsk](https://github.com/dmis-lab/covidAsk) is real-time biomedical question answering system trained on COVID-19 articles. A server for querying is current hosted at [https://covidask.korea.ac.kr](https://covidask.korea.ac.kr).

CovidAsk is trained based on DenSPI, which supports real-time question answering on a large unstructured corpus.

## Data

### CORD-19

Kaggle COVID-19 Open Research Dataset Challenge ([CORD-19](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)) provided 8GB of manuscript data. 

CORD-19 data was downloaded with the Kaggle API installed 

```bash
$ pip install kaggle
$ kaggle datasets download allen-institute-for-ai/CORD-19-research-challenge
```

Additionally, DMIS-Lab provided pre-processed CORD-19 data matching the SQuAD format. The pre-processed CORD-19 data was used to train the covidAsk model.

### Limitations

Compared to the datasets used for BioBERT fine-tuning
