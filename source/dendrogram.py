# -*- coding: utf-8 -*-
__author__ = 'Wisse'
import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.cluster.hierarchy as hac
import pickle
import sentence_splitter as sp



fontsize = 4
points_per_inch = 72


sys.setrecursionlimit(10000)

# construct labels
sentences = sp.MySentences('data/test_data.txt')
labels = np.array(sentences.get_sentences())



# remove unicode characters like \u2022 from labels and glue lists back to sentences
labels = [' '.join([word.encode('ascii', 'ignore') for word in sent]) for sent in labels]


# load linkage matrix
pickle_file = open(sys.argv[1], 'rb')
links = pickle.load(pickle_file)
tree = hac.to_tree(links)

def search_tree(tree, id):
    if tree.get_id() == id:
        return tree.pre_order()
    if tree.is_leaf():
        return []
    return search_tree(tree.get_left(), id) + search_tree(tree.get_right(), id)

n = sentences.size
print n
# leaf lable function

def llf(id):
    if id < n:
        label = "Singleton: " + str(labels[id]) + '\n'
        return label
    else:
        indeces = search_tree(tree, id)
        sentences = [labels[index] for index in indeces][5:35]
        output = [str(len(sentences)) + " ------------------------------------------"] + sentences
        return '\n'.join(output)

# create dendogram
height = sentences.size * fontsize
print height
plt.figure(figsize=([20, 300]))
plt.subplots_adjust(right = 0.5, top=1, bottom=0)
den = hac.dendrogram(links, orientation='right', p=5, truncate_mode='level', labels=labels,
                     leaf_label_func=llf, leaf_font_size=fontsize, show_leaf_counts=True, get_leaves=True)


plt.savefig('results/dendrogram_all_sentences.png')
plt.show()

# print indexes and corresponding labels to terminal
for i in den['leaves']:
    if i < n:
        print i, llf(i)
    else: print i, llf(i)