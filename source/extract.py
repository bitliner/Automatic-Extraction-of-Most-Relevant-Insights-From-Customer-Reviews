__author__ = 'Wisse'

import gensim as gs
import numpy as np
import sys
import sentence_splitter as ssp
import fastcluster as fc
import visualization
import scipy.cluster.hierarchy as hac

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
    vecs = [np.array(model[z.labels[0]]).reshape((1, size)) for z in corpus]
    return np.concatenate(vecs)

data_vecs = getVecs(model, data, size)

# visualize using tSNE
#TODO: (tsne does not work on virtual machine)
# visualization.visualize(data_vecs)

links = fc.linkage(data_vecs, metric='cosine',method='average')

n = sentences.size

# first nodes to group together
index1, index2 = links[-1, 0] - n, links[-1, 1] - n

print sentences.retrieve_sentence(index1), sentences.retrieve_sentence(index2)
