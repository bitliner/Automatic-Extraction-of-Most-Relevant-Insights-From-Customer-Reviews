__author__ = 'Wisse'

# create word2vec representation of sentences
word2vec = gs.models.Word2Vec(sentences)
print word2vec[sentences]

#sentences_word2vec = word2vec[sentences]

#for sentence in sentences_word2vec:
 #   print(sentence)