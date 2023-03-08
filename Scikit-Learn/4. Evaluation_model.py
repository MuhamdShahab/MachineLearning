#model.fit is the best example for fitting the model
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
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
#linear Support vector machine
from sklearn.svm import LinearSVC
clf_model = LinearSVC(max_iter=2000)
clf_model.fit(X1_train, Y1_train)
print("Linear SVC : ", clf_model.score(X1_test, Y1_test))
#Other model for Classification is RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier
clf_model12 = RandomForestClassifier()
clf_model12.fit(X1_train, Y1_train)
print("RandomForestClassifier :  ", clf_model12.score(X1_test, Y1_test))

#4. Evaluating a model
#4.1 Using the Score function
#print("RandomForestRegressor : ",reg_model.score(X_test, Y_test))
#we can alter the n_estimators to change the results as well.
#reg_model = RandomForestRegressor(n_estimators = 50) #gives 0.8022791474334594
#reg_model = RandomForestRegressor(n_estimators = 100) #gives 0.8062379399942214
#reg_model = RandomForestRegressor(n_estimators = 500) #gives 0.807990704101994
#reg_model.fit(X_train, Y_train)
#print("Random Forest Regressor With Params : ",reg_model.score(X_test, Y_test))

#4.2 Using the Scoring function; it uses a cross validation technique
np.random.seed(42)
clf_model13 = RandomForestClassifier(n_estimators= 100)
clf_model13.fit(X1_train, Y1_train)
print("RandomForestClassifierLatest :  ", clf_model12.score(X1_test, Y1_test))
from sklearn.model_selection import cross_val_score
clf_score = cross_val_score(clf_model13,X,Y,cv=7)
print("Cross val score for the 7 set are: ",clf_score)
print("Mean of the CLF score is : ", np.mean(clf_score))
#clf_score2 = cross_val_score(clf_model13, X, Y, cv = 7, scoring = None) #if scoring is none it uses the default scoring parameter which is mean accuracy

### 4.2.1 Classification model evaluation 
#1. Accuracy
#2. Area under ROC Curve
#3. Confusion Matrix
#4. Classification report

#1. Accuracy
np.random.seed(42)
clf_model14 = RandomForestClassifier(n_estimators= 100)
cross_val_score2 = cross_val_score(clf_model14, X, Y, cv = 7, scoring = None)
accuracy_clf_model14 = np.mean(cross_val_score2)*100
print("Accuracy for the CV model is: % ", accuracy_clf_model14)


#2. Area under the ROC Curve- Reciever Operating Characteristic Curve
#ROC Curve are the comparison for the model's True positive Rate(tpr) versus a models false positive Rate (fpr)
#True Positive = model predicts 1 when actual answer is 1
#False Positive = model predicts 1 when truth is 0
#True Negative = model predicts 0 when actual answer is 0
#False Negative = model predicts 0 when truth is 1

from sklearn.metrics import roc_curve
clf_model14.fit(X1_train, Y1_train);
y_probs = clf_model14.predict_proba(X1_test)
#print(y_probs[:10])
y_probs_positive = y_probs[:,1]
fpr, tpr, thresholds = roc_curve(Y1_test, y_probs_positive)
import matplotlib.pyplot as plt

def plot_roc_curve(fpr,tpr):
    plt.plot(fpr,tpr,color = "orange", label ="ROC")
    plt.plot([0,1],[0,1], color = "darkblue", linestyle="--", label = "Guessing")
    plt.xlabel("False positive rate(fpr)")
    plt.ylabel("True positive rate(tpr)")
    plt.title("Reciever Operating Characteristics (ROC) Curve")
    plt.legend()
    plt.show()

plot_roc_curve(fpr,tpr)

from sklearn.metrics import roc_auc_score
vali = roc_auc_score(Y1_test, y_probs_positive)
print("vali ", vali) #curve max value is 1

#confusion Matrix
from sklearn.metrics import confusion_matrix
