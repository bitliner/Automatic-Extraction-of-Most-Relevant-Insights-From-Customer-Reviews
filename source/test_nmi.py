__author__ = 'Wisse'

import dendrogram
import get_vecs
import extract
import evaluate
import sys

test_data_path = str(sys.argv[1])
model_path = str(sys.argv[2])
exp_name = str(sys.argv[3])

vector_size = int(sys.argv[4])
save = bool(int(sys.argv[5]))
level = int(sys.argv[6])
stop = bool(int(sys.argv[7]))
method = str(sys.argv[8])


data_vecs = get_vecs.get_data_vecs(model_path, test_data_path, vector_size, stop=stop)

links = extract.cluster(data_vecs, save=save, method=method)


# needs labeled data!
nmi = evaluate.evaluate(test_data_path, links, level, stop, exp_name, save=save)


