# ----1. importing Dataset----
from sklearn.datasets import load_iris
iris = load_iris() #dictionary that contains the design & target
    #dataset is cleaned already so putting it in matrices
    #no preprocessing required as all the data is numerical
X = iris.data #features
Y = iris.target #output


# ----2. Splitting the data for train and testing
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, train_size=0.80)

# ----3. Choose the KNN model
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors= 5)

# ----4. fitting the data to the model
knn.fit(X_train,Y_train)

# ----5. Evaluating the model
print("Model Score: ",knn.score(X_test, Y_test)) #acuracy nearly 0.966666666667

# ----6. Predicting the output on the basis of user' input.
inp1 = float(input("Enter Sepal length: "))
inp2 = float(input("Enter Sepal width: "))
inp3 = float(input("Enter Sepal length: "))
inp4 = float(input("Enter Sepal width: "))

# create an array to feed into the predition function
import numpy as np
inp = np.array([[inp1, inp2, inp3, inp4]])
prob = knn.predict_proba(inp)
print("Probabilty matrix: ",prob)
out = knn.predict(inp)[0]
# ----7. Interpreting the result in human readable form
flowerdict = {
  0: "Setosa",
  1: "Versicolor",
  2: "Virginia"
}
print("Depending upon features model predict output as : ",flowerdict[out]) 