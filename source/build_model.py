__author__ = 'Wisse'


import gensim as gs
import os
import sys
from HTMLParser import HTMLParser
import logging
logging.basicConfig(filename="log.txt", format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


input = sys.argv[1]

LabeledSentence = gs.models.doc2vec.LabeledSentence
parser = HTMLParser()


# iterating object of directory or file
class MySentences(object):
    def __init__(self, name):
        self.name = name
    def __iter__(self):
        if os.path.isdir(self.name):
            """Iterate through the lines in the source directory."""
            for fname in os.listdir(self.name):
                for itme_no, line in enumerate(open(os.path.join(self.name, fname))):
                    decoded = parser.unescape(line)
                    #TODO: add preprocessing here
                    yield LabeledSentence(gs.utils.to_unicode(decoded).split(), ['SENT_%s' % item_no])
        else:
            for item_no, line in enumerate(open(self.name, 'r')):
                decoded = parser.unescape(line)
                #TODO: add preprocessing here
                yield LabeledSentence(gs.utils.to_unicode(decoded).split(), ['SENT_%s' % item_no])

# create object of command line input
sentences = MySentences(input)


# create model
model_dm = gs.models.Doc2Vec(min_count=1, window=10, sample=1e-3, negative=5, workers=3)

model_dm.build_vocab(sentences)
model_dm.train(sentences)
print "Done training"
model_dm.save("../models/model-amazone-review-all.doc2vec")




