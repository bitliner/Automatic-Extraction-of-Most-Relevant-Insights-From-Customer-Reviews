__author__ = 'Wisse'


import gensim as gs
import sys
import logging
import sentence_splitter as s_s

input, series = sys.argv[1], sys.argv[2]

print "This model is called: {0}".format(series)

logging.basicConfig(filename="logs/{0}log.txt".format(series),
                    format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


# create object of command line input
sentences = s_s.MySentences(input)


# create model
model_dm = gs.models.Doc2Vec(min_count=1, window=10, sample=1e-3, negative=5, workers=3)

model_dm.build_vocab(sentences)
model_dm.train(sentences)
print "Done training"
print model_dm.similarity("cords", "hotspot")
model_dm.save("models/model{0}.doc2vec".format(series), separately=None)




