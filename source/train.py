__author__ = 'Wisse'

import build_model
import sys

data_path = str(sys.argv[1])
series = str(sys.argv[2])
size = int(sys.argv[3])
training_rounds = int(sys.argv[4])
min_count = int(sys.argv[5])
save = bool(sys.argv[6])
remove_stop = bool(sys.argv[7])

build_model.train(data_path, series, size, training_rounds=training_rounds, min_count=min_count, save=save, stop=remove_stop)
