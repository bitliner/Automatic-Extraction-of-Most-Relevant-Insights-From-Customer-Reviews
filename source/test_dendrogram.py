__author__ = 'Wisse'

import dendrogram
import get_vecs
import extract
import evaluate
import sys

test_data_path = str(sys.argv[1])
model_path = str(sys.argv[2])
series_name = str(sys.argv[3])
vector_size = int(sys.argv[4])
level = int(sys.argv[5])
stop = bool(sys.argv[6])
method = str(sys.argv[7])
show_figure = bool(sys.argv[8])
figure_size = tuple(sys.argv[9])

data_vecs = get_vecs.get_data_vecs(model_path, test_data_path, vector_size, stop=stop)
links = extract.cluster(data_vecs, save=False, method=method)
dendrogram.render(links, test_data_path, series_name, stop,level, show_figure, figure_size[0], figure_size[1])


