__author__ = 'Wisse'
import sys
import gensim as gs
import matplotlib.pyplot as plt
import numpy as np
import scipy.cluster.hierarchy as hac
import get_vecs as gv
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

# Create a nested dictionary from the ClusterNode's returned by SciPy
def add_node(node, parent):
    # First create the new node and append it to its parent's children
    newNode = dict(node_id=node.id, children=[])
    parent["children"].append(newNode)

    # Recursively add the current node's children
    if node.left: add_node(node.left, newNode)
    if node.right: add_node(node.right, newNode)

d3Dendro = dict(children=[], name="Root1")
add_node( tree, d3Dendro )


def lookup(dict, id):
    return get_singletons(search_tree(dict, id))

def get_singletons(children):
    indeces = []
    for child in children:
        if not child.isleaf():
            indeces.append(child.getid())
        else: get_singletons([child.getright(), child.getleft()])
    return indeces

def search_tree(tree, id):
    children = [tree.getleft(), tree.getright()]
    for child in children:
        if child.getid() == id:
            return [child.getleft(), child.getright()]
        else:
            for child in [child.getleft(), child.getright()]:
                search_tree(child, id)

