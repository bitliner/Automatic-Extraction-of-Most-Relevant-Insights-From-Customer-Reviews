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

# import data and model from command line
data, model = sys.argv[1], sys.argv[0]

# split data into sentences
sentences = ssp.MySentences(data)

# grab lables from labeled sentences

#Get training set vectors from our models
def getVecs(model, corpus, size):
    vecs = [np.array(model[z.labels[0]]).reshape((1, size)) for z in corpus]
    return np.concatenate(vecs)


# grab feature vectors
data = []

for i in labels:
    try:
        vector = feature_model[i]
        data.append(vector)
    except KeyError:
        continue



print "Grabbed the feature vectors... "


begin = time.time()
# estimate bandwidth

data = np.array(data)
bandwidth = estimate_bandwidth(data)

print bandwidth

print "Estimated bandwidth"

bandwidth_time = time.time() - begin

begin = time.time()
# create model
train_model = MeanShift(bandwidth=bandwidth)
train_model.fit(data)
cluster_time = time.time() - begin

print "Trained the model..."

c_labels = train_model.labels_
centers = train_model.cluster_centers_

print "labels are: {0}".format(c_labels)
print "centerss are: {0}".format(centers)

# prediction

for label in labels:
    try:
        vector = np.array(feature_model[label])
        pred = train_model.predict(vector)
    except KeyError:
        continue

    print sentences.lookup(i), pred


file = open("log{0}lines.txt".format(lines),'w')
file.write("The input consisted of {0} lines. \n".format(lines))
file.write("The time to create the doc2vec model was {0} \n".format(doc2vec_time))
file.write('The time to estimate the bandwidth was {0} \n'.format(bandwidth_time))
file.write('The time to create the clustering was {0} \n'.format(cluster_time))
file.close()





























