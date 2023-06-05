import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

class Knearestneighbours:
    def __init__(self, K:int = 5) ->None:
        self.__features = None
        self.__target = None
        if not isinstance(K,int):
            raise TypeError("Expected an integer for parameter 'n_neighbors' in Knearestneighbours.")
        elif(K%2 ==0):
            self.__nearest = K+1
            print("n_neighbors is even ",K, "making it odd ", K+1)
        else:
            self.__nearest = K
    def fit(self, feature, target) ->None:
        self.__features = pd.DataFrame(feature)
        self.__target = pd.DataFrame(target)
    def predict(self, input) -> np.ndarray:
        self.__distances = np.linalg.norm(self.__features.values - input, axis=1)
        self.__index = np.argsort(self.__distances)[:self.__nearest]
        self.__result = self.__target.values[self.__index]
        self.__unique_values, self.__counts = np.unique(self.__result, return_counts=True)
        self.__max_count_index = np.argmax(self.__counts)
        self.__mode_value = np.array([self.__unique_values[self.__max_count_index]])
        return self.__mode_value

iris = load_iris()
X = pd.DataFrame(iris.data)
Y = pd.DataFrame(iris.target)
flower = {0:'Setosa', 1: 'Versicolor', 2: 'Virginica'}
K = 5
Knn = Knearestneighbours(K)
Knn.fit(X,Y)
test = np.array([5.9, 3.0, 5.1, 1.8])
out = Knn.predict(test)
print(flower[out[0]])
