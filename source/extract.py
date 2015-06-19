__author__ = 'Wisse'

import gensim as gs
import numpy as np
import sys
import sentence_splitter as ssp
import fastcluster as fc
# import visualization
import scipy.cluster.hierarchy as hac
import pickle

def cluster(data_vecs, filename, method='average', metric='cosine', save=True):
    print "Calculating the linkage matrix, metric = {0}, method = {1}".format(metric, method)
    links = fc.linkage(data_vecs, metric=metric,method=method)

    if save:
        print "Saving the model to: results/" + filename + "/linkage"
        file = open('results/' + filename + '_linkage', 'wb')
        pickle.dump(links, file)
        file.close()
    return links
