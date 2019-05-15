# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 10:43:37 2018

@author: DeSI-Anjin Liu
"D:/Anjin/GithubProjects/ConceptDriftDatasets/"
"""

import arff
import numpy as np


# import torch
# torch.from_np

class DriftDataset(object):
    """concept drift dataset loading class"""

    _datasetDict = {
        "elec": "RealWorld/Classification/elec/elecNorm.arff",
        "weather": "RealWorld/Classification/weather/weather.arff",
        "spam": "RealWorld/Classification/spam_corpus_x2_feature_selected/spam_corpus_x2fs.arff",
        "usenet1": "RealWorld/Classification/usenet1_2/usenet1.arff",
        "usenet2": "RealWorld/Classification/usenet1_2/usenet2.arff",
        "airline": "RealWorld/Classification/airline/airlines.arff",
        "covtype" : "RealWorld/Classification/covtype/covtypeNorm.arff",
        "poker" : "RealWorld/Classification/Poker-Hand/poker-hand-testing.arff",
        "SEAa": "Synthetic/SEAa/SEAa0.arff",
        "SEAg": "Synthetic/SEAg/SEAg0.arff",
        "HYP": "Synthetic/HYP/HYP0.arff",
        "AGRa": "Synthetic/AGRa/AGRa0.arff",
        "AGRg": "Synthetic/AGRg/AGRg0.arff",
        "LEDa": "Synthetic/LEDa/LEDa0.arff",
        "LEDg": "Synthetic/LEDg/LEDg0.arff",
        "RBF": "Synthetic/RBF/RBF0.arff",
        "RBFr": "Synthetic/RBFr/RBFr0.arff",
        "RTG": "Synthetic/RTG/RTG0.arff"
    }

    def __str__(self):
        return "Class: concept_drift_dataset_loader"

    def load_np(self, dataset_name):
        file_ = self.DATA_FILE_PATH + DriftDataset._datasetDict[dataset_name]
        dataset = arff.load(open(file_), encode_nominal=True)
        self.np_data = np.array(dataset["data"])
        # self.np_data, self.meta = arff.loadarff()

    def __init__(self, path, dataset_name):
        self.DATA_FILE_PATH = path
        print("==========================================================")
        print("Setting data file path:")
        print("  ", DriftDataset._datasetDict[dataset_name])
        print("   Loading dataset")
        self.load_np(dataset_name)
        print("   Loading finish")
        print("==========================================================")
        self.num_class = np.unique(self.np_data[:,-1]).shape[0]

if __name__ == "__main__":
    path = "D:/Anjin/GithubProjects/ConceptDriftDatasets/"
    dataset_name = "poker"
    data = DriftDataset(path, dataset_name)
    
    a = data.np_data[:1000◙,:]
    c1 = np.where(a[:,-1] == 0)
    c2 = np.where(a[:,-1] == 1)
    c3 = np.where(a[:,-1] == 2)
    c4 = np.where(a[:,-1] == 3)
    c5 = np.where(a[:,-1] == 4)
    c6 = np.where(a[:,-1] == 5)
    c7 = np.where(a[:,-1] == 6)
    c8 = np.where(a[:,-1] == 7)
    c9 = np.where(a[:,-1] == 8)
    c10 = np.where(a[:,-1] == 9)
    print(c1[0].shape)
    print(c2[0].shape)
    print(c3[0].shape)
    print(c4[0].shape)
    print(c5[0].shape)
    print(c6[0].shape)
    print(c7[0].shape)
    print(c8[0].shape)
    print(c9[0].shape)
    print(c10[0].shape)
    # cov remove 3,4,5 index
    # poker remove 4,5,6,7,8,9