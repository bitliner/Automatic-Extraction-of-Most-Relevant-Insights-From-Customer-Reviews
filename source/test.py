__author__ = 'Wisse'

import dendrogram
import get_vecs
import extract
import evaluate
import sys

test_data_path = sys.argv[1]
model_path = sys.argv[2]
exp_name = sys.argv[3]

vector_size = int(sys.argv[4])
save = sys.argv[5]
level = int(sys.argv[6])

data_vecs = get_vecs.get_data_vecs(model_path, test_data_path, vector_size)

links = extract.cluster(data_vecs, exp_name, save)

nmi = evaluate.evaluate(test_data_path, links, save, level)


