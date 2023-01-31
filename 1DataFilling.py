import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

##1. G etting the data ready to be used in machine learning
##1.1 Splittin the data into features and labels
##1.2 Filling/Imputing the missing or disregarding the missing values
##1.3 Converting the string data into numerical values known as Feature encoding

heart_disease = pd.read_csv("data/heart-disease.csv")
#1.1 Seprate the Feature and label matrices
X = heart_disease.drop("target", axis=1)
Y = heart_disease.target
#split the data into test and train data
from sklearn.model_selection import train_test_split
X_train,X_test, Y_train, Y_test = train_test_split(X,Y,train_size=0.80)

#1.2 Make sure its all numerical
car_sales= pd.read_csv("data/car-sales-detailed.csv")
X1 = car_sales.drop("Price",axis=1)
Y1 =car_sales.Price
X1_train,X1_test,Y1_train,Y1_test = train_test_split(X1,Y1,train_size=0.80)
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
#model.fit(X1_train,Y1_train) this won't work because all the data is not numerical
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
categories = ["Make","Color","Doors"]
one_hot = OneHotEncoder()
transformer = ColumnTransformer([("one_hot",one_hot,categories)],remainder='passthrough')
transformed_X1 = transformer.fit_transform(X1)
df = pd.DataFrame(transformed_X1)
X2_train,X2_test,Y2_train,Y2_test = train_test_split(transformed_X1,Y1,train_size=0.80)
#model.fit(X2_train,Y2_train)
#model.score(X2_test,Y2_test) #works perfectly 

#1.3 If you face the missing data 1. Fill the data or 2. Remove the misiing data examples
### Remplacing rhe data and droping it
car_missing =  pd.read_csv("data/car_sales_missing_detailed.csv")
car_missing["Make"].fillna("missing",inplace=True)
car_missing["Color"].fillna("missing",inplace=True)
car_missing["Range"].fillna(1000,inplace=True)
car_missing["Doors"].fillna(4,inplace=True)
car_missing.dropna(inplace = True)
X3 = car_missing.drop("Price",axis=1)
Y3 =car_missing.Price
categories = ["Make","Color","Doors"]
one_hot = OneHotEncoder()
transformer = ColumnTransformer([("one_hot",one_hot,categories)],remainder='passthrough')
transformed_X3 = transformer.fit_transform(X3)
df = pd.DataFrame(transformed_X3)
X3_train,X3_test,Y3_train,Y3_test = train_test_split(transformed_X3,Y3,train_size=0.80)
#model.fit(X3_train,Y3_train)
#model.score(X3_test,Y3_test)
# Option2 Filling the data with the some sklearn or called as imputing

car_miss =  pd.read_csv("data/car_sales_missing_detailed.csv")
car_miss.dropna(subset=["Price"], inplace = True)
X4 = car_miss.drop("Price",axis = 1)
Y4 = car_miss.Price
from sklearn.impute import SimpleImputer
#fill categorical values with the missgin and the numerical values as required.
cat_imputer = SimpleImputer(strategy = 'constant',fill_value= "missing")
door_imputer = SimpleImputer(strategy="constant",fill_value=4)
num_imputer = SimpleImputer(strategy="mean")
#Define columns
cat_features = ["Make","Color"]
door_feature = ["Doors"]
num_feature =["Range"]
#create an imputer(something the fills the missing data)
imputer = ColumnTransformer([
    ("cat_imputer",cat_imputer,cat_features),
    ("door_imputer",door_imputer, door_feature),
    ("num_imputer",num_imputer,num_feature)])
filled_X4 = imputer.fit_transform(X4)
car_sales_imputed = pd.DataFrame(filled_X4)
car_sales_imputed.rename(columns = {0:'Make',1:'Color',2:'Doors',3:'Range'}, inplace = True)
#testing the model after imputing the values 
model = RandomForestRegressor()
categories = ["Make","Color","Doors"]
one_hot = OneHotEncoder()
transformer = ColumnTransformer([("one_hot",one_hot,categories)],remainder='passthrough')
transformed_X5 = transformer.fit_transform(car_sales_imputed)
X5_train,X5_test,Y5_train,Y5_test = train_test_split(transformed_X5,Y4,train_size=0.80)
model.fit(X5_train,Y5_train)
print(model.score(X5_test,Y5_test)) #works perfectly 