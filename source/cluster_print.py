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
sentences = sp.MySentences(sys.argv[1])
labels = np.array(sentences.get_sentences())

series = sys.argv[3]

# remove unicode characters like \u2022 from labels and glue lists back to sentences
labels = [' '.join([word.encode('ascii', 'ignore') for word in sent]) for sent in labels]

# load linkage matrix
pickle_file = open(sys.argv[2], 'rb')
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
        sentences = [labels[index] for index in indeces][0:100]
        output = [str(len(sentences)) + " ------------------------------------------"] + sentences
        return '\n'.join(output)

p = range(1, int(series))
clusters = []
singletons = []
for i in range(1,int(series)):
    print "level = %s" % i
    den = hac.dendrogram(links, orientation='right', p=i, truncate_mode='level', labels=labels,
                     leaf_label_func=llf, leaf_font_size=fontsize, show_leaf_counts=True, get_leaves=True)
    file = open('results/lists-of-clusters/%s.txt' % i, 'w')
    singles = [i for i in den['leaves'] if i < n]

    clusters.append(len(den['leaves']))
    singletons.append(len(singles))

    file.write('Number of clusters: %s \n' % len(den['leaves']))
    file.write('Number of singletons: %s \n\n' % len(singles))

    for id in den['leaves']:
        file.write(llf(id))
        file.write('\n\n\n\n\n\n')
    file.close()
    
plt.clf()
plt.plot(p, clusters, label='number of clusters')
plt.plot(p, singletons, label='number of singletons')
plt.legend()
plt.xlabel('level of clustering')
plt.savefig('results/dendogram-level-cluster-behavior.png')
plt.show()