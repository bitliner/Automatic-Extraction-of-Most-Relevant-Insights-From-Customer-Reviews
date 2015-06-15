__author__ = 'Wisse'
import sys
import gensim as gs
import matplotlib.pyplot as plt
import numpy as np
import scipy.cluster.hierarchy as hac
import get_vecs as gv
import pickle
import sentence_splitter as sp
from tree import lookup

sys.setrecursionlimit(10000)

# construct labels
sentences = sp.MySentences('data/test_data.txt')
words = np.array(sentences.get_sentences())


# load linkage matrix
pickle_file = open(sys.argv[1], 'rb')
links = pickle.load(pickle_file)
tree = hac.to_tree(links)

n = sentences.size
# leaf lable function
def llf(id):
    if id < n:
        return words[n].join(" ")
    else:
        indeces = lookup(tree, id)
        return [words[index] for index in indeces].join("/n")


# create dendogram
plt.figure(figsize=(20, 100))
den = hac.dendrogram(links, orientation='right', p=10, truncate_mode='level', labels=words)

plt.savefig('results/dendrogram_large.png')
plt.show()
