__author__ = 'Wisse'
import sys
import numpy as np
import scipy.cluster.hierarchy as hac
import pickle
import sentence_splitter as sp



sys.setrecursionlimit(10000)

# construct labels
sentences = sp.MySentences('data/test_data.txt')
words = np.array(sentences.get_sentences())


# load linkage matrix
pickle_file = open(sys.argv[1], 'rb')
links = pickle.load(pickle_file)

n = sentences.size

tree = hac.to_tree(links)

def search_tree(tree, id):
    if tree.get_id() == id:
        return tree.pre_order()
    if tree.is_leaf():
        return []
    return search_tree(tree.get_left(), id) + search_tree(tree.get_right(), id)


