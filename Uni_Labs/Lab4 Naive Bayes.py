# from sklearn.datasets import load_iris
# from sklearn.naive_bayes import GaussianNB
# gnb = GaussianNB()
# # Loading data
# irisData = load_iris()
# # Create feature and target arrays
# X = irisData.data
# y = irisData.target
# classes={0:'setosa',1:'versicolor',2:'virginica'}
# gnb.fit(X, y)
# f1=float(input('New sepal length:'))
# f2=float(input('New sepal width:'))
# f3=float(input('New petal length:'))
# f4=float(input('New petal width:'))
# x_new=[[f1,f2,f3,f4]]
# y_predict=gnb.predict(x_new)
# print(classes[y_predict[0]])

####TASK 2 ####
import pandas as pd
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
df = pd.read_csv("data/glass.csv")
Y = df.Type
X = df.drop("Type", axis= 1)
gnb.fit(X.values, Y)
f1=float(input('RI: '))
f2=float(input('Na: '))
f3=float(input('Mg: '))
f4=float(input('Al: '))
f5=float(input('Si: '))
f6=float(input('K: '))
f7=float(input('Ca: '))
f8=float(input('Ba: '))
f9=float(input('Fe: '))
x_new=[[f1,f2,f3,f4,f5,f6,f7,f8,f9]]
y_predict=gnb.predict(x_new)
print("Glass has type: ",y_predict[0])