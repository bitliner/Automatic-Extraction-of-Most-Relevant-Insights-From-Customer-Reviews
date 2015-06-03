__author__ = 'Wisse'

import gensim as gs

class SentenceSplitter:
    "Split sentences according to Doc2Vec.LabeledLineSentences in multiple formats"
    def __init__(self, source):
        self.source = source
        self.sentences = gs.models.doc2vec.LabeledLineSentence(source)
        self.sentences_dict = {}

    def labeled_line_sentences(self):
        "Returns LabeledLineSentences of source"
        #TODO: a newline is a new sentence

        return self.sentences

    def sentences_to_dict(self):
        "Returns sentences in dictionary"
        for sentence in self.sentences:
            self.sentences_dict[sentence.labels[0]] = sentence.words
        return self.sentences

    def lookup(self, key):
        if not self.sentences_dict:
            self.sentences_to_dict()

        return self.sentences_dict[key]

    def labels(self):
        self.sentences_to_dict()
        return self.sentences_dict.keys()















