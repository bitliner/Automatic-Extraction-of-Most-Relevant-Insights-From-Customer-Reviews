__author__ = 'Wisse'

import gensim as gs
import numpy as np
import sys
import sentence_splitter as ssp
import visualization

size = 300

# import data to be clustered from command line
data = open(sys.argv[1], 'r')

model_path = sys.argv[0]
# load model from command line
model = gs.models.Doc2Vec.load(model_path)

# split data into sentences
sentences = ssp.MySentences(data)

#Get training set vectors from our models
def getVecs(model, corpus, size):
    for z in corpus:
        print z
    vecs = [np.array(model[z.labels[0]]).reshape((1, size)) for z in corpus]
    return np.concatenate(vecs)

data_vecs = getVecs(model, data, size)

# visualize using tSNE
visualization.visualize(data_vecs)