# -*- coding: utf-8 -*-
__author__ = 'Wisse'


import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.cluster.hierarchy as hac
import pickle
import sentence_splitter as sp
import tree

sys.setrecursionlimit(10000)


def render(linkage_file, test_data, file_name, stop, level, show, fig_height=20, fig_width=8):
    fontsize = 4

    # construct labels
    sentences = sp.MySentences(test_data, stop=stop)
    labels = np.array(sentences.get_sentences())


    # remove unicode characters like \u2022 from labels and glue lists back to sentences
    labels = [' '.join([word.encode('ascii', 'ignore') for word in sent]) for sent in labels]


    # load linkage matrix

    links = linkage_file
    link_tree = hac.to_tree(linkage_file)


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


    plt.savefig('results/' + file_name +'/dendrogram' + str(level) + '.png')

    if show:
        plt.show()

    # print indexes and corresponding labels to terminal and file
    output = open('results/' + file_name + 'clusters' + str(level) + '.txt', 'w')

    def find_sentence(id):
        if id < n:
            label = "Singleton: " + str(labels[id]) + '\n'
            return label
        else:
            indeces = tree.search_tree(link_tree, id)
            sentences = [str(labels[index]) for index in indeces]
            output = [str(len(sentences)) + " ------------------------------------------"] + sentences
            return '\n'.join(output)

    num_singletons = []
    num_clusters = []

    singles = [i for i in den['leaves'] if i < n]

    num_clusters.append(len(den['leaves']))
    num_singletons.append(len(singles))

    output.write('Number of clusters: %s \n' % len(den['leaves']))
    output.write('Number of singletons: %s \n\n' % len(singles))

    for id in den['leaves']:
        output.write(find_sentence(id))
        output.write('\n\n\n\n\n\n')
    output.close()


