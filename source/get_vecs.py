__author__ = 'Wisse'
import numpy as np

import gensim as gs
import sentence_splitter as ssp
import scipy.cluster.hierarchy as hac

size = 300
def create_sentences(data_path):
    return ssp.MySentences(data_path)

def create_model(model_path):
    return gs.models.Doc2Vec.load(model_path)

def getVecs(model, corpus, size):
    vecs = [np.array(model[z.labels[0]]).reshape((1, size)) for z in corpus]
    return np.concatenate(vecs)

def get_data_vecs(model_path, data_path, size):
    return getVecs(create_sentences(data_path), create_model(model_path), size)

