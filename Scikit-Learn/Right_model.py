import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Regressor Example
from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing()
df_housing = pd.DataFrame(housing.data)
df_housing.columns = housing.feature_names
df_housing["target"] = housing.target
X = df_housing.drop("target", axis= 1)
Y = df_housing.target
from sklearn.model_selection import train_test_split
X_train, X_test,Y_train, Y_test = train_test_split(X,Y,test_size=0.20)
#using Ridge regressor for output
from sklearn.linear_model import Ridge
reg_model = Ridge()
reg_model.fit(X_train, Y_train)
print("Ridge Regressor : ",reg_model.score(X_test, Y_test))
#improving model for better performance using RandomForestRegressor
from sklearn.ensemble import RandomForestRegressor
reg_model2 = RandomForestRegressor()
reg_model2.fit(X_train, Y_train)
print("RandomForestRegressor : ",reg_model2.score(X_test, Y_test))

#Classification Example

df_heart = pd.read_csv("data/heart-disease-classification-sklearn.csv")
X = df_heart.drop("target", axis = 1)
Y = df_heart.target
X1_train, X1_test, Y1_train, Y1_test = train_test_split(X,Y,train_size = 0.80)
#linear Support vector machine for linear Regression
from sklearn.svm import LinearSVC
clf_model = LinearSVC(max_iter=50000)
clf_model.fit(X1_train, Y1_train)
print("Linear SVC : ", clf_model.score(X1_test, Y1_test))
#Other model for Classification is RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier
clf_model12 = RandomForestClassifier()
clf_model12.fit(X1_train, Y1_train)
print("RandomForestClassifier :  ", clf_model12.score(X1_test, Y1_test))