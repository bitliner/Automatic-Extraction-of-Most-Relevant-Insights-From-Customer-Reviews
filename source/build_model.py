#!/usr/local/bin/python
__author__ = 'Wisse'


from guppy import hpy
import gensim as gs
import sys
import logging
import sentence_splitter as s_s


input, series = sys.argv[1], sys.argv[2]
size = 300 # default

print "This model is called: {0}".format(series)

logging.basicConfig(filename="logs/{0}log.txt".format(series),
                    format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


# create object of command line input
sentences = s_s.MySentences(input)

h = hpy()
# create model
model_dm = gs.models.Doc2Vec(min_count=1, window=10, sample=1e-3, negative=5, workers=3)
print "Building vocab for the model now..."
model_dm.build_vocab(sentences)
print "The model has {0} sentences.".format(sentences.size)
print "Memory usage (MB) after building vocab: "
print h.heap().size / 1000000

h = hpy()
# training the model
print "Training the model now..."
model_dm.train(sentences)
print "Done training."
print "Memory usage after training: "
print h.heap().size / 1000000

# testing
print model_dm.similarity("cords", "hotspot")

# saving
model_dm.save("models/{0}/model{0}.doc2vec".format(series), separately=None)




