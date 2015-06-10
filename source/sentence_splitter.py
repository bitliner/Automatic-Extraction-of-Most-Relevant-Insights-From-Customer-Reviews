#!/usr/local/bin/python

__author__ = 'Wisse'

import gensim as gs
import nltk
from HTMLParser import HTMLParser
import os
import string

stop = nltk.corpus.stopwords.words('english')

LabeledSentence = gs.models.doc2vec.LabeledSentence
parser = HTMLParser()
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

#TODO: Splits lines not sentences!



# iterating object of directory or file
class MySentences(object):
    def __init__(self, name, log=True):
        self.name = name
        self.labels = []
        self.size = 0
        self.log = True
    def __iter__(self):
        """Iterate through the lines in file or in files in source directory."""
        self.size = 0
        if os.path.isdir(self.name):
            for fname in os.listdir(self.name):
                for line in open(os.path.join(self.name, fname)):
                    sentences = tokenizer.tokenize(gs.utils.to_unicode(line))
                    for item_no, sentence in enumerate(sentences):
                        # preprocessing: remove HTML, stopwords, numbers; convert to lowercase & unicode
                        decoded = parser.unescape(sentence).lower()
                        words = [i for i in decoded.split() if i not in stop and not i.isdigit()]
                        label = 'SENT_%s' % item_no

                        # store labels
                        if label not in self.labels:
                            self.labels.append(label)

                        # log process
                        self.size += 1
                        if self.log and self.size % 1000 == 0:

                            print "Processed {0} sentences now.".format(self.size)
                        yield LabeledSentence(words, [label])
        else:
            for line in open(self.name, 'r'):
                sentences = tokenizer.tokenize(gs.utils.to_unicode(line))
                for item_no, sentence in enumerate(sentences):
                    # preprocessing: remove HTML, stopwords, numbers; convert to lowercase & unicode
                    decoded = parser.unescape(sentence).lower()
                    words = [i for i in decoded.split() if i not in stop and not i.isdigit()]
                    label = 'SENT_%s' % item_no

                    # store labels
                    if label not in self.labels:
                        self.labels.append(label)

                    # log process
                    self.size += 1
                    if self.log and self.size % 1000 == 0:

                        print "Processed {0} sentences now.".format(self.size)
                    yield LabeledSentence(words, [label])

















