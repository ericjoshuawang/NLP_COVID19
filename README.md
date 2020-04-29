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

In this work, we provide a comparison between the performance of BERT-based and DenSPI-based machine learning models. The BERT-based model achieved high accuracy on an old QA task from BioASQ, while the DenSPI-based model behind [covidAsk](https://covidask.korea.ac.kr) provided a real-time answering server for COVID-19-related questions with lower accuracy. We point out that the difference in accuracy stems from data limitation as we lack curated COVID-19 data. As COVID-19 data becomes annotated, future work can focus on formulating a QA problem and applying BioBERT on the annotated corpus.

## Previous Work

### BioBERT
[BioBERT](https://github.com/dmis-lab/biobert/blob/master) is a biomedical language representation model designed for biomedical text mining tasks such as biomedical named entity recognition, relation extraction, question answering. 

BioBERT is pre-trained on PubMed manuscripts based on the original BERT model designed by Google AI Language.

**BERT**, or **B**idirectional **E**ncoder **R**epresentations from
**T**ransformers, is a method of pre-training language representations which
obtains state-of-the-art results on a wide array of Natural Language Processing
(NLP) tasks.

The paper on BERT can be found [here](https://arxiv.org/abs/1810.04805).

### SQuAD Fine-tuning

Stanford Question Answering Dataset ([SQuAD](https://rajpurkar.github.io/SQuAD-explorer/)) is a reading comprehension dataset, consisting of questions posed by crowdworkers on a set of Wikipedia articles, where the answer to every question is a segment of text, or span, from the corresponding reading passage, or the question might be unanswerable.

BioBERT was trained on PubMed corpus and fine-tuned on SQuAD to achieve the state-of-the-art performance for NLP tasks. 

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

Compared to the datasets used for BioBERT training and validation with annotated questions and answers, the CORD-19 dataset is unstructured with only text and phrases. Without extensive processing, the current CORD-19 data does not fit well into pre-trained BERT models.

## Results and Discussion

The BioBERT model with SQuAD fine-tuning outperformed the baseline model on the BioASQ QA task. This shows the importance of SQuAD fine-tuning.

Models       | `BERT-Base`  | `BERT-SQuAD`
------------ | ----------   | --------------
SAcc         | 0.128        | **0.282**
LAcc         | 0.359        | **0.564**
MRR          | 0.206        | **0.385**

The SAcc score represents the fraction of questions answered correctly by the first/top element of the predicted list.

The LAcc score represents the fraction of questions answered correctly by any element of the predicted list.

```
{'exact_match_top1': 17.56756756756757, 'f1_score_top1': 26.885230840315774}
{'exact_match_top10': 25.675675675675677, 'f1_score_top10': 43.14339166481719}
```

The exact_match_top1 represents the fraction of correct classifications by the top 1 element.

The exact_match_top10 represents the fraction of correct classifications by the top 10 element.


As the covidAsk model operated under a classification task rather than a QA task for BioBERT, the evaluation parameters are slightly different. Nonetheless, the exact_match_top1 score can be compared to the SAcc scorea; the exact_match_top10 score is more stringent than the LAcc score and thus the comparison between these two parameters isn't informative to draw a conclusion.

Models       | `BERT-Base`  | `BERT-SQuAD`  | `covidAsk-DenSPI`  
------------ | ----------   | --------------| --------------
SAcc         | 0.128        | **0.282**     | 0.176
LAcc         | 0.359        | 0.564         | (0.257)
MRR          | 0.206        | 0.385         | N/A

Provided by the updated table, the SAcc score of 0.282 for `BERT-SQuAD` compared to the similar parameter for `covidAsk` being 0.176 suggests that the BERT model performs better if there's annotated data avaialable. As both BioBERT-SQuAD and covidAsk-DenSPI are fine-tuned on SQuAD, the difference in performance can be attributed to the pre-training corpus. BioBERT was pre-trained on PubMed corpus while DenSPI was pre-trained on Wikipedia corpus; hence BioBERT has more high quality scientific exposure and is more focused on the biomedical field than DenSPI.

However due to the current limitation of data, BioBERT can't be applied directly on the unstructured CORD-19 corpus for a QA taks. Therefore, the DMIS-lab compromised by using the DenSPI model for classification and real-time answering. As the CORD-19 corpus becomes annotated, the BioBERT model can be eventually used to achieve a higher accuracy when trained and tested locally.

To answer our proposed questions, we replicated the covidAsk platform and held our own covidAsk server on local host with GPUs. Using the pre-trained DenSPI model, we tested our questions to obtain the following predictions.

Input question string: "What is the range of incubation periods for the disease in humans?"

Output prediction vector: ['7.1 (6.13, 8.25) days', '3-7 days', '2‐ to 10‐day', 'three to eight days', '1 to 20 days', '7.4, 4 and 7 days', 'about 3-7 days', 'between 3 and 7 days', '4.4 (95% CI 3.8-5.1) days', 'days or even weeks']


Input question string: "How long are individuals contagious, even after recovery?"

Output prediction vector: ['1-2 months', 'hours to months', '21 days', '4 to 6 days', 'R time units', '21 and 31 days', '1-3 days', '21 and 31 days', 'a few days', 'transiently to very few individuals']


