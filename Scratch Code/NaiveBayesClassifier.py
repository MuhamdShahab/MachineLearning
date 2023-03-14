import pandas as pd
import numpy as np


class GaussianNB():
    def __init__(self):
        self.__feature=None
        self.__target=None
    def fit(self,feature,target):
        feature = pd.DataFrame(feature)
        target = pd.DataFrame(target)
        assert len(target.value_counts().index) != 1 , "Prediction can't be done on single class problem"
        self.__feature = feature
        self.__target = target
        df_new = self.__feature.copy();    
        df_new["Target"] = self.__target.copy()
        self.__p_class = df_new.Target.value_counts()/df_new.Target.count()
        self.__data_mean = df_new.groupby('Target').mean()
        self.__data_variance = df_new.groupby('Target').var()
    def __multiply_row(self, row):
        return row.prod()
    def predict_proba(self, test):
        assert test.shape[0] == self.__feature.shape[1] , "Incorrect Dimensions in Prediction"
        self.__dependent = 1/(np.sqrt(2*np.pi*self.__data_variance)) * np.exp((-(test-self.__data_mean)**2)/(2*self.__data_variance))
        self.__dependent['Prior'] = self.__p_class
        self.__dependent['Posterior'] = self.__dependent.apply(self.__multiply_row, axis=1)
        self.__evidence = self.__dependent.Posterior.sum()
        return self.__dependent.Posterior/self.__evidence
    def predict(self, test):
        assert test.shape[0] == self.__feature.shape[1] , "Incorrect Dimensions in Predict"
        self.__proba = self.predict_proba(test)
        return self.__proba.idxmax()


from sklearn.datasets import load_iris
X =  load_iris().data
Y = load_iris().target
gnb = GaussianNB()
gnb.fit(X,Y)
test = np.array([5.3, 3, 5.1,1.8])
result = gnb.predict(test)
flowers = { 0: "Setosa",1: "Versicolor",2: "Virginica"}
print("Resulting Flower is: ",flowers[result])
