# RNN to Write Patent Abstracts

Based on [Recurrent Neural Networks by Example in Python](https://towardsdatascience.com/recurrent-neural-networks-by-example-in-python-ffd204f99470) by Will Koehrsen.

## Objective

Build a RNN that produces abstracts for patents.

## Problem Formulation

The RNN will have as input a sequence of words, that denotes the start of the abstract, and as output will produce the very next word. This word will be added to the input sequence, and the process continues ultil the abstract is fulfilled.
