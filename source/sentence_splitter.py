__author__ = 'Wisse'

import gensim as gs
import nltk
from HTMLParser import HTMLParser
import os
import string

stop = nltk.corpus.stopwords.words('english')

LabeledSentence = gs.models.doc2vec.LabeledSentence
parser = HTMLParser()

# iterating object of directory or file
class MySentences(object):
    def __init__(self, name):
        self.name = name
        self.labels = []
    def __iter__(self):
        if os.path.isdir(self.name):
            """Iterate through the lines in the source directory."""
            for fname in os.listdir(self.name):
                for item_no, line in enumerate(open(os.path.join(self.name, fname))):
                    decoded = parser.unescape(line).lower()
                    words = [i for i in gs.utils.to_unicode(decoded).split() if i not in stop and not i.isdigit()]
                    #TODO: add preprocessing here
                    label = 'SENT_%s' % item_no
                    if label not in self.labels:
                        self.labels.append(label)
                    yield LabeledSentence(words, [label])
        else:
            for item_no, line in enumerate(open(self.name, 'r')):
                decoded = parser.unescape(line).lower()
                words = [i for i in gs.utils.to_unicode(decoded).split() if i not in stop and not i.isdigit()]
                #TODO: add preprocessing here
                label = 'SENT_%s' % item_no
                if label not in self.labels:
                    self.labels.append(label)
                yield LabeledSentence(words, [label])

















