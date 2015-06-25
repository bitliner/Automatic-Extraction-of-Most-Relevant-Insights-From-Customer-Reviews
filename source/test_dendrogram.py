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
remove_stop = bool(int(sys.argv[6]))
method = str(sys.argv[7])
show_figure = bool(int(sys.argv[8]))
save = bool(int(sys.argv[9]))
figure_height = int(sys.argv[10])

data_vecs = get_vecs.get_data_vecs(model_path, test_data_path, vector_size, stop=remove_stop)
links = extract.cluster(data_vecs, save=False, method=method)
dendrogram.render(links, test_data_path, series_name, remove_stop, level, show_figure, save, fig_height=figure_height)


