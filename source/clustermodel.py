__author__ = 'Wisse'

import sklearn as skl

class ClusterModel:
    def __init__(self, data):
        self.data = data



    def mean_shift(self):
        self.model = skl.cluster.MeanShift()

    def cluster(self):
        self.model.fit(self.data)


