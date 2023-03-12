import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def compute_cost(x,y,w):
    #mean square error is the cost function
    cost = ((((np.dot(w,x.T)).sum(axis =0))-y.reshape(y.shape[0],))**2).sum() #squaring the error and summing for m examples
    return cost/(x.shape[0]) #divided by number of examples for taking mean

def gradient_descent(x,y,w,lr):

    weight_deriv = np.dot((((np.dot(w,x.T)).sum(axis =0))-y.reshape(y.shape[0],)),X)
    new_w = w - ((weight_deriv / x.shape[0]) * lr)
    return new_w

def train(x,y,w,lr,iters):
    np_c = np.array([])
    for i in range(iters):
        w = gradient_descent(x,y,w,lr)
        cost = compute_cost(x,y,w)
        np_c = np.append(np_c,[cost])
        if (i%50 == 0):
            print("Weight = ",w,"   Cost = ",cost)
    return w,np_c


#importing data to create dataset
df = pd.read_csv("data/real-estate.csv").dropna().head(350) #preprocessing not required as all float and int
df /=df.max()
df.No =1

X = np.array([df.drop("price",axis=1)]) 
X = X.reshape((X.shape[1],X.shape[2]))
Y = np.array([df.price]).T
ln_rate = 99999
W = np.zeros((1,X.shape[1]))
weight, cost_history = train(X,Y,W,0.001,ln_rate)#design, Supervision, Weight,Learnigng rate, iteratio
iters = np.arange(start=0, stop=ln_rate, step=1)
print(X.shape)
fig, ax = plt.subplots()
ax.scatter(X,Y)
ax.plot(iters,cost_history)
plt.show()
