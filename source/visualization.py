__author__ = 'Wisse'


import gensim as gs
import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from tsne import bh_sne
import sys


def visualize(vecs):
    print "Got the vectors, now doing dimesnion reduction..."
    reduced = bh_sne(vecs)
    print "Reduction done, now plotting: "

    for i in range(len(reduced)):
        plt.plot(vecs[i,0], vecs[i,1], marker='o', markersize=8)

    plt.show()


