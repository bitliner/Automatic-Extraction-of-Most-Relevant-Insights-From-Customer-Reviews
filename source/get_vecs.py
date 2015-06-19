__author__ = 'Wisse'
import numpy as np

import gensim as gs
import sentence_splitter as ssp
import scipy.cluster.hierarchy as hac

def create_sentences(data_path,stop):
    return ssp.MySentences(data_path, stop=stop)

def create_model(model_path):
    return gs.models.Doc2Vec.load(model_path)

def getVecs(model, corpus, size):
    vecs = [np.array(model[z.labels[0]]).reshape((1, size)) for z in corpus]
    return np.concatenate(vecs)

def get_data_vecs(model_path, data_path, size, stop):
    return getVecs(create_model(model_path),create_sentences(data_path, stop), size)

