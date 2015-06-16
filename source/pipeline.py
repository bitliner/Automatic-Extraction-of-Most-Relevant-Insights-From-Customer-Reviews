__author__ = 'Wisse'
__author__ = 'Wisse'

import sys
import gensim as gs
import clustermodel
import sentence_splitter as ssp
from sklearn.cluster import MeanShift, estimate_bandwidth
import numpy as np
import time

"""NLTK Pipeline:

Processes commandline argument according to following scheme:

1. Sentence Splitter on each document
2. Doc2vec representation on each document, at sentence level
3. Clustering on the whole corpus of sentences
4. Selection of the best insights from the clusters resulting from previous step
"""
size = 300 # default

# import data to be clustered and model from command line
data, model = sys.argv[1], sys.argv[0]

# split data into sentences
sentences = ssp.MySentences(data)

#Get training set vectors from our models
def getVecs(model, corpus, size):
    vecs = [np.array(model[z.labels[0]]).reshape((1, size)) for z in corpus]
    return np.concatenate(vecs)

data_vecs = getVecs(model, data, size)

print "Grabbed the data's feature vectors... "

# clustering


file = open("log{0}lines.txt".format(lines),'w')
file.write("The input consisted of {0} lines. \n".format(lines))
file.write("The time to create the doc2vec model was {0} \n".format(doc2vec_time))
file.write('The time to estimate the bandwidth was {0} \n'.format(bandwidth_time))
file.write('The time to create the clustering was {0} \n'.format(cluster_time))
file.close()


###
### example of simple pipeline, using external modules

# text=readfile('...')
# sentences=ssp.split(text)
# vectors=sentence2vec(sentences)
# clusters=clustering.run(vectors)
# output_file=visualizer.render(clusters)




























