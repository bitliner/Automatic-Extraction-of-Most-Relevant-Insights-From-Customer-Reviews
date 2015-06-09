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
    def __init__(self, name, log=True):
        self.name = name
        self.labels = []
        self.size = 0
        self.lod = True
    def __iter__(self):
        if os.path.isdir(self.name):
            """Iterate through the lines in the source directory."""
            for fname in os.listdir(self.name):
                for item_no, line in enumerate(open(os.path.join(self.name, fname))):

                    # preprocessing: remove HTML, stopwords, numbers; convert to lowercase & unicode
                    decoded = parser.unescape(line).lower()
                    words = [i for i in gs.utils.to_unicode(decoded).split() if i not in stop and not i.isdigit()]
                    label = 'SENT_%s' % item_no

                    # store labels
                    if label not in self.labels:
                        self.labels.append(label)

                    # log process
                    if self.log == True and self.size % 1000 == 0:
                        print "The model includes {0} sentences now.".format(self.size)
                    yield LabeledSentence(words, [label])
        else:
            for item_no, line in enumerate(open(self.name, 'r')):
                # preprocessing: remove HTML, stopwords, numbers; convert to lowercase & unicode
                decoded = parser.unescape(line).lower()
                words = [i for i in gs.utils.to_unicode(decoded).split() if i not in stop and not i.isdigit()]
                label = 'SENT_%s' % item_no

                # store labels
                if label not in self.labels:
                    self.labels.append(label)

                # log process
                if self.log == True and self.size % 1000 == 0:
                    print "The model includes {0} sentences now.".format(self.size)

                yield LabeledSentence(words, [label])

















