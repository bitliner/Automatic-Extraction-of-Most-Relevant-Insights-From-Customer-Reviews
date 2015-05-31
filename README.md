# Automatic Extraction of Most Relevant Insights from Customer Reviews

## Index

1. [Introduction](introduction)
2. [Algorithm](algorithm)
3. [Implementation details](implementation-details)
4. [Experiments](#experiments)
5. [Release cycle](release-cycle)

## Introduction

In the last 5 years more than 5 billion of reviews shoppers wrote on the Web. 

Manufacturers know that is essential to understand what customer say, in order to create better products.

A lot of work on understanding customer reviews has been focused on sentiment analysis, especially aspect based sentiment analysis, to understand what product feature is considered positive or negative into a review. 

But not so work has been focused on extracting other meaningful information. 


**We propose a technique to extract the most relevant insights for a manufacturer from a set of text  reviews.** 

Most relevant insights correspond to those thoughts/opinions/sentences that customers express more often or less often inside a corpus of reviews. 

In this way manufacturers can have a clear overview of what the majority of their online customers are thinking on their products.

## Algorithm

The algorithm is based on 2 main concepts:

1. **sentence modeling**: to transform sentences and represent them as vectors
2. **clustering**: to organize sentence vectors in groups and each group includes all the sentences with almost the same meaning

The algorithm can be described with the the following steps:

1. the text of each review is divided into sentences
2. each sentence is transformed into a sentence vector
3. all the vectors representing the sentences are organized in groups by some clustering algorithm like MeanShift
4. the clusters/groups with the biggest size are selected (they are the most occurring sentences in the input set of reviews)
5. the centroid of each cluster is selected as one of the most relevant insights

## Implementation details

[TBD - libraries, programming languages, etc.]

## Experiments

### How experiments are organized

### What metrics to use for experiments

### Description

## Release cycle

### v1 (I week)

Simple prototype:

* takes as input an array of documents - eventually read from a file
* run the NLP pipeline
* returns the best insights printed on command line - or on a file

#### NLP Pipeline required for v1

1. Sentence Splitter on each document (1h)
2. Doc2Vec representation on each document, at sentence level (16h)
3. Clustering on the whole corpus of sentences (16h)
4. Selection of the best insights from the clusters resulting from previous step (8h)

### v2 (II week)

1. First execution on a real dataset
2. Better definition of a set experiments to run and metrics
3. First measurement of metrics

### v3 (III week)

[TBD] 

### v4 (IV week)

[TBD]





