from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class NaiveBayesClassifier:
    def __init__(self, feature, targ):
        #Check validation on the data
        assert len(np.unique(targ)) >= 1, f"The target {targ} contains only one class{valid}."
        #assign the data
        self.__features = feature
        self.__target = targ
        self.__sape = __features.shape
        self.__n_feature = sape[len(sape)-1]
        self.__n_target = sape[len(sape)-2]
        self.__classes = np.unique(targ)
        self.__n_classes = len(classes)

    def predict(self, test):
        #make prediction and return the anwer
        test = test+2
        ans = 1
        return ans




X = load_iris().data
Y = load_iris().target

model1 = NaiveBayesClassifier(X,Y)
X_new = np.array([3.2, 2.3, 2.1, 1.3])
result = model1.predict(X_new)