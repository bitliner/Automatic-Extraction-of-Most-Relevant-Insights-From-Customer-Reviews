__author__ = 'Wisse'
import gensim as gs

"Step 2 of NLP pipeline: Creating doc2vec representation of sentences."


doc2vec = gs.models.Doc2Vec(sentences)
