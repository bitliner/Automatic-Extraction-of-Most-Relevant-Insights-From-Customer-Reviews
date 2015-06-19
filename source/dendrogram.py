# -*- coding: utf-8 -*-
__author__ = 'Wisse'
""" Input consists of a set of test data, it's linkage-matrix and a name
fot the output figure. The linkage-matrix is constructed with extract.py.

Example usage:
python source/dendrogram.py data/test_data.txt results/test_linkage a_test_figure """

import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.cluster.hierarchy as hac
import pickle
import sentence_splitter as sp
import tree

sys.setrecursionlimit(10000)


def render(linkage_file, test_data, file_name, stop, level, fig_height=20, fig_width=8):
    fontsize = 4

    # construct labels
    sentences = sp.MySentences(test_data)
    labels = np.array(sentences.get_sentences())


    # remove unicode characters like \u2022 from labels and glue lists back to sentences
    labels = [' '.join([word.encode('ascii', 'ignore') for word in sent]) for sent in labels]


    # load linkage matrix

    links = pickle.load(open(linkage_file))
    link_tree = hac.to_tree(links)


    n = sentences.size

    # leaf lable function
    def llf(id):
        if id < n:
            label = "Singleton: " + str(labels[id]) + '\n'
            return label
        else:
            indeces = tree.search_tree(link_tree, id)
            sentences = [labels[index] for index in indeces][0:9]
            output = [str(len(sentences)) + " ------------------------------------------"] + sentences
            return '\n'.join(output)

    plt.figure(figsize=([fig_width,fig_height]))

    plt.subplots_adjust(right = 0.7, top=1, bottom=0)
    den = hac.dendrogram(links, orientation='right', p=level, truncate_mode='level', labels=labels,
                     leaf_label_func=llf, leaf_font_size=fontsize, show_leaf_counts=True, get_leaves=True)


    plt.savefig('results/' + file_name)
    plt.show()

    # print indexes and corresponding labels to terminal
    for i in den['leaves']:
        if i < n:
            print i, llf(i)
        else: print i, llf(i)

