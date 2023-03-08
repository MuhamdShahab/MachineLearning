from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
# Loading data
irisData = load_iris()
# Create feature and target arrays
X = irisData.data
y = irisData.target
classes={0:'setosa',1:'versicolor',2:'virginica'}
gnb.fit(X, y)
f1=float(input('New sepal length:'))
f2=float(input('New sepal width:'))
f3=float(input('New petal length:'))
f4=float(input('New petal width:'))
x_new=[[f1,f2,f3,f4]]
y_predict=gnb.predict(x_new)
print(classes[y_predict[0]])
