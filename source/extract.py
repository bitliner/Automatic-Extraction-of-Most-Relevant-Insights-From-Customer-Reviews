__author__ = 'Wisse'

import gensim as gs
import numpy as np
import sys
import sentence_splitter as ssp
import fastcluster as fc
# import visualization
import scipy.cluster.hierarchy as hac
import pickle

size = 400

# import data to be clustered from command line
data_path = sys.argv[1]

# load model from command line
model_path = sys.argv[2]
model = gs.models.Doc2Vec.load(model_path)

# name for output
filename = sys.argv[3]

# split data into sentences
sentences = ssp.MySentences(data_path)

#Get training set vectors from our models
def getVecs(model, corpus, size):
    vecs = [np.array(model[z.labels[0]]).reshape((1, size)) for z in corpus]
    return np.concatenate(vecs)

print "Getting the vectors for the test data."
data_vecs = getVecs(model, sentences, size)

# visualize using tSNE
#TODO: (tsne does not work on virtual machine)
# visualization.visualize(data_vecs)

print "Calculating the linkage matrix, metric = cosine, method = average"
links = fc.linkage(data_vecs, metric='cosine',method='average')

print "Saving the model to: results/" + filename + "/linkage"
file = open('results/' + filename + '/linkage', 'rb')
pickle.dump(links, file)
file.close()


