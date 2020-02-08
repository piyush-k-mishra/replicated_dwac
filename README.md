## Replication of Deep Weighted Averaging Classifier

This project is a replication of the [*Deep Weighted Averaging Classifiers*](https://arxiv.org/abs/1811.02579)'s implementation code i.e. [*Deep Weighted Averaging Classifiers*](https://github.com/dallascard/DWAC)

This project tries to confirm the consistency of Deep Weighted Averaging Classifier across model. For this case, text classification of imdb comments is done with two different models.

The binary classification is done first using A CNN using softmax. This model is then extended to use DWAC as an alternative for softmax. And finally an RNN model is trained with DWAC.

To run code use following command:

 `python -m text.run --model [basline|dwac_model|dwac_rnn] --dataset [dataset] --device [GPU number]`
 
 where,
 dwac_model = CNN with DWAC
 dwac_rnn = RNN with DWAC
 baseline = CNN with softmax
 
 Befor running the code, GloVe `glove.6B.300d.txt` text file needs to be included in path `data\temp\vectors\`.
