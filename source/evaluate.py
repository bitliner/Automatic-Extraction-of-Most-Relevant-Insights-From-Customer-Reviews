__author__ = 'Wisse'

"""
This module provides two methods for quantative evaluation of clustering:
purity and normalized mutual information. The input data should be of the form:
label1 text text text text
label2 text text text text
"""

import numpy as np
import scipy.cluster.hierarchy as hac
import pickle
import sentence_splitter as sp
import math
import tree



def evaluate(labeled_data, linkage_file, p, save=True):
    # construct labels
    sentences = sp.MySentences(labeled_data)
    lines = np.array(sentences.get_sentences())

    # load linkage matrix
    try:
        links = pickle.load(open(linkage_file, 'rb'))
    except:
        links = linkage_file

    link_tree = hac.to_tree(links)

    # intialize variables to save the labels
    labeled = []
    processed = []

    # index map: index -> label
    index_map = {}
    count = 0
    # create tuples from raw text with (label, sentence)
    for line in lines:
        label, text = line[0], line[1:]
        index_map[count] = label
        labeled.append((label, text))
        count += 1


    # label map: label -> index
    label_map = {}

    # create inverse of index_map (values <-> keys)
    for k, v in index_map.iteritems():
        try:
            label_map[v].append(k)
        except Exception:
            label_map[v] = [k]


    # number of instances
    n = sentences.size

    # find indexes of leaves
    def llf(id, tree):
        if id < n:
            return [id]
        else:
            return tree.search_tree(tree, id)

    # untokenize labeled sentences
    for label in labeled:
        label, text = label[0], label[1]
        text = ' '.join([word.encode('ascii', 'ignore') for word in text])
        processed.append((label, text))

    # create dendrogram of level 'p'
    den = hac.dendrogram(links, orientation='right', p=p, truncate_mode='level', labels=processed,
                      show_leaf_counts=True, get_leaves=True)

    # collect clusters in dict
    clusters = {}
    for leave in den['leaves']:
        clusters[leave] = llf(leave, link_tree)

    pur_out = purity(clusters, n)
    print "Purity: "
    print pur_out

    nmi_out = nmi(label_map, clusters,  n)
    print "NMI: "
    print nmi_out

    if save:
        # writing output to file
        def find_sentence(id):
            if id < n:
                label = "Singleton: " + str(processed[id]) + '\n'
                return label
            else:
                indeces = tree.search_tree(link_tree, id)
                sentences = [str(processed[index]) for index in indeces]
                output = [str(len(sentences)) + " ------------------------------------------"] + sentences
                return '\n'.join(output)

        num_singletons = []
        num_clusters = []

        file = open('results/assess_evaluation/%s.txt' % p, 'w')
        singles = [i for i in den['leaves'] if i < n]

        num_clusters.append(len(den['leaves']))
        num_singletons.append(len(singles))

        file.write('Number of clusters: %s \n' % len(den['leaves']))
        file.write('Number of singletons: %s \n\n' % len(singles))
        file.write('Purity: %s \n' % pur_out)
        file.write('NMI: %s\n' % nmi_out)

        for id in den['leaves']:
            file.write(find_sentence(id))
            file.write('\n\n\n\n\n\n')
        file.close()

    return nmi_out, pur_out



# auxillary function to find most common element in list
def most_common(lst):
    return max(set(lst), key=lst.count)

# purity
def purity(clusters, n):
    correct = 0
    for key in clusters.keys():
        value = clusters[key]
        if len(value) < 2:
            c = value[0]
        else:
            c = most_common(value)
        correct += value.count(c)
    return 1/float(n) * correct

# mutual information
def mutual_information(classes, clusters, n):
    n = float(n)
    mi = 0
    for x,i in classes.iteritems():
        for z,j in clusters.iteritems():
            intersect = len([label for label in i if label in j])
            if intersect == 0:
                continue
            mi += (intersect/n) * math.log((n*intersect)/(len(i)*len(j)), 2)
    return mi

# entropy
def entropy(dict, n):
    n = float(n)
    entropy = 0
    for key, value in dict.iteritems():
        entropy += len(value)/n * math.log(len(value)/n, 2)
    return  -entropy

# normalized mutual information
def nmi(classes, clusters, n):
    class_entropy = entropy(classes, n)
    cluster_entropy = entropy(clusters, n)
    normalizer = (cluster_entropy + class_entropy)/2
    return mutual_information(classes, clusters, n)/normalizer