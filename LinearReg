import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def update_weights(size, price, weight, bias, learning_rate):
    weight_deriv = 0
    bias_deriv = 0
    len_data = size.shape[0]

    weight_deriv += 2*(((((weight*size+bias)-price).T)*size.T).sum())
    bias_deriv += 2*((((weight*size+bias))-price).sum())

    weight -=((weight_deriv / len_data) * learning_rate)
    bias -=((bias_deriv / len_data) * learning_rate)

    return weight, bias

df = pd.read_csv("LR-heartdata.csv").head(210)
df.dropna(inplace= True)
x = np.array([df.Size])
y = np.array([df.Price])

m,c = update_weights(x.T,y.T,0,200,0.0001)
print(m)
print(c)
hyp = m*x + c
fig, ax1 = plt.subplots()
ax1.set(title = "LR1V", xlabel =  "Size(m^2)", ylabel = "Price($)")
ax1.scatter(x,y, color = 'Red', marker="x")
ax1.plot(x.T,hyp.T)
plt.show()
