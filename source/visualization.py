__author__ = 'Wisse'


import gensim as gs
import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from tsne import bh_sne

def getWordVecs(words):
    vecs = []
    for word in words:
        word = word.replace('\n', '')
        try:
            vecs.append(model[word].reshape((1,300)))
        except KeyError:
            continue
    vecs = np.concatenate(vecs)
    return np.array(vecs, dtype='float')

model = gs.models.Doc2Vec.load("models/model2000.doc2vec")
vocab = model.vocab
vecs = getWordVecs(vocab)
vecs = vecs[10000:100000]

ts = TSNE(2)

print "Got the vectors, now doing dimesnion reduction..."
reduced = bh_sne(vecs)
print "Reduction done, now plotting: "

for i in range(len(reduced)):
    plt.plot(vecs[i,0], vecs[i,1], marker='o', markersize=8)

plt.show()


