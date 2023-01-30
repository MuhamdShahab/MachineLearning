
---------------------------------------------------------------------------
################ 0.End to end Sikit-learn workflow
################ 1.Getting the Data Ready
################ 2.Choose the right estimator/algorithm for our problems
################ 3.Fit the model
################ 4.Evaluating the model 
################ 5.Improve the model
################ 6.Save & load the model
################ 7.Putting it all togather
---------------------------------------------------------------------------

################# 0. An end to end Scikit-Learn workflow
import pandas as pd
import numpy as np
################# 1. Getting the DataReady
heart_disease = pd.read_csv('data/heart-disease.csv') #reading csv

X = heart_disease.drop('target', axis= 1) #creating the design matrix
Y = heart_disease['target'] #creating the supervision matrix

################## 2. Choose the model and the right hyperparameter
from sklearn.ensemble import RandomForestClassifier 
clf = RandomForestClassifier(n_estimators= 100) #classifier model
#print(clf.get_params())

################### 3. Fit the model and use it to make predictions on our data
from sklearn.model_selection import train_test_split 
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2) #spliting the data
clf.fit(X_train,Y_train) #fitting the data to check the patterns
Y_preds = clf.predict(X_test)

################### 4. Evaluate the model
print(clf.score(X_train, Y_train))
print(clf.score(X_test, Y_test))

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(classification_report(Y_test, Y_preds))
print(confusion_matrix(Y_test, Y_preds))
print(accuracy_score(Y_test, Y_preds))

#################### 5. Improve the model
np.random.seed(seed=0)
for i in range(10,100,10):
    print(f"Trying model with {i} estimator...")
    clf = RandomForestClassifier(n_estimators=i).fit(X_train,Y_train)
    print(f"Model Accurace on test set: {clf.score(X_test,Y_test) * 100:.2f}%")
    print(" ")

#################### 6. Save the model and load it 
import pickle

pickle.dump(clf, open("random_forst_model_1.pkl", "wb"))

load_model = pickle.load(open("random_forst_model_1.pkl", "rb"))
print(load_model.score(X_test, Y_test))
 

