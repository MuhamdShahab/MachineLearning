import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def gradient_descent(size, price, weight, bias, learning_rate):
    weight_deriv = 0
    bias_deriv = 0
    len_data = size.shape[0]
    
    weight_deriv += (np.dot((weight*size+bias)-price,size.T).sum())
    bias_deriv += ((weight*size+bias)-price).sum()

    #weight_deriv += 2*(((((weight*size+bias)-price).T)*size.T).sum())
    #bias_deriv += 2*((((weight*size+bias))-price).sum())

    new_w = weight - ((weight_deriv / len_data) * learning_rate)
    new_b = bias -((bias_deriv / len_data) * learning_rate)

    return new_w, new_b

def train(radio, sales, weight, bias, learning_rate, iters):
    cost_history = []

    for i in range(iters):
        weight,bias = gradient_descent(radio, sales, weight, bias, learning_rate)
        # #Calculate cost for auditing purposes
        # cost = cost_function(radio, sales, weight, bias)
        # cost_history.append(cost)

        # Log Progress
        if i % 50 == 0:
            print ("Iter =", i, "Weight =", weight, "Bias =", bias)
    return weight, bias, cost_history


df = pd.read_csv("data/LR-heartdata.csv").head(210)
df.dropna(inplace= True)
x = np.array([df.Size])
y = np.array([df.Price])

m,c,d = train(x.T,y.T,0,0,0.01,99)
hyp = m*x + c
fig, ax1 = plt.subplots()
ax1.set(title = "LR1V", xlabel =  "Year", ylabel = "Price($)")
ax1.scatter(x,y, color = 'Red', marker="x")
ax1.plot(x.T,hyp.T)
plt.show()