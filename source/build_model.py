#!/usr/local/bin/python
__author__ = 'Wisse'


from guppy import hpy
import gensim as gs
import sys
import logging
import sentence_splitter as s_s


def train(data, series, size, training_rounds=10, workers=8, min_count=10, save=True, stop=True):
    """Train a doc2vec model on given input data, saves in:
    models/[series]/model[size].doc2vec
    NOTE: mkdir models/[series]/ first"""

    print "This model is called: {0}".format(series)

    # log
    logging.basicConfig(filename="logs/{0}log.txt".format(series),
                    format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


    # create object of command line input
    sentences = s_s.MySentences(data, stop=stop)

    h = hpy()
    # create model
    model_dm = gs.models.Doc2Vec(min_count=min_count, window=10, sample=1e-3, negative=5,
                             workers=workers, alpha=0.025, min_alpha=0.025, size=size)

    print "Building vocab for the model now..."
    model_dm.build_vocab(sentences)
    print "The model has {0} sentences.".format(sentences.size)
    print "Memory usage (MB) after building vocab: "
    print h.heap().size / 1000000

    # training the model
    h = hpy()
    for epoch in range(training_rounds):
        print "Training the model now, epoch no. %s" % epoch
        model_dm.train(sentences)
        model_dm.alpha -= 0.002
        model_dm.min_alpha = model_dm.alpha

    print "Done training."
    print "Memory usage after training: "
    print h.heap().size / 1000000

    # saving
    if save:
        if stop:
            model_dm.save("models/{0}/model{1}no_stop.doc2vec".format(series, size), separately=None)
        else:
            model_dm.save("models/{0}/model{1}with_stop.doc2vec".format(series, size), separately=None)
    return model_dm



