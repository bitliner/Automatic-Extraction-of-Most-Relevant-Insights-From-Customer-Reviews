__author__ = 'Wisse'

import gensim as gs
import sys


model = gs.models.Doc2Vec.load(sys.arv[1])
print model.accuracy(sys.argv[2])