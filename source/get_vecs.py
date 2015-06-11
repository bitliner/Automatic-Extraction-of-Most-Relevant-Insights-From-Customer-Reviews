__author__ = 'Wisse'
import numpy as np

#Get training set vectors from our models
def getVecs(model, corpus, size):
    for z in corpus:
        print z
    vecs = [np.array(model[z.labels[0]]).reshape((1, size)) for z in corpus]
    return np.concatenate(vecs)
