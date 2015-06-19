__author__ = 'Wisse'
import sys
import numpy as np
import scipy.cluster.hierarchy as hac
import pickle
import sentence_splitter as sp



sys.setrecursionlimit(10000)

def search_tree(tree, id):
    if tree.get_id() == id:
        return tree.pre_order()
    if tree.is_leaf():
        return []
    return search_tree(tree.get_left(), id) + search_tree(tree.get_right(), id)


