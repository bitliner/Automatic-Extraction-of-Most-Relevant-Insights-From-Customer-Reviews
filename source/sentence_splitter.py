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


#TODO: spell check?
#todo: remove product specific terms (airfryer) ?



# iterating object of directory or file
class MySentences(object):
    def __init__(self, name, log=True, stop=True):
        self.punctuation = """.,?!:;(){}[]/\ """
        self.quotations = """`"'"""
        self.name = name
        self.labels = []
        self.size = 0
        self.log = log
        self.remove_stop_words = stop
    def __iter__(self):
        """Iterate through the lines in file or in files in source directory."""
        self.size = 0
        if os.path.isdir(self.name):
            for fname in os.listdir(self.name):
                for line in open(os.path.join(self.name, fname)):
                    for c in self.punctuation:
                        line = line.replace(c, ' %s '%c)
                    for q in self.quotations:
                        line = line.replace(q, '')
                    sentences = tokenizer.tokenize(gs.utils.to_unicode(line))
                    for item_no, sentence in enumerate(sentences):
                        # preprocessing: remove HTML, stopwords, numbers; convert to lowercase & unicode
                        decoded = parser.unescape(sentence).lower()

                        words = [i.replace("\u2022", '') for i in decoded.split() if not i.isdigit()]
                        label = 'SENT_%s' % item_no

                        # stopwords
                        if self.remove_stop_words:
                            words = [word for word in words if word not in stop]

                        # skip empty sentences
                        if not words:
                            continue

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
                for c in self.punctuation:
                    line = line.replace(c, ' %s '% c)
                for q in self.quotations:
                    line = line.replace(q, ' ')
                sentences = tokenizer.tokenize(gs.utils.to_unicode(line))
                for item_no, sentence in enumerate(sentences):
                    # preprocessing: remove HTML, stopwords, numbers; convert to lowercase & unicode
                    decoded = parser.unescape(sentence).lower()
                    words = [i.replace("\u2022", '') for i in decoded.split() if not i.isdigit()]

                    # stopwords
                    if self.remove_stop_words:
                        words = [word for word in words if word not in stop]
                    label = 'SENT_%s' % item_no

                    # skip empty sentences
                    if not words:
                        continue
                    # store labels
                    if label not in self.labels:
                        self.labels.append(label)

                    # log process
                    self.size += 1
                    if self.log and self.size % 1000 == 0:

                        print "Processed {0} sentences now.".format(self.size)
                    yield LabeledSentence(words, [label])


    def retrieve_sentence(self, index):
        iterate = iter(self)
        while not self.size == index -1:
            iterate.next()
        return iterate.next()

    def get_sentences(self):
        iterate = iter(self)
        words = []
        for i in iterate:
            words.append(i.words)
        return words















