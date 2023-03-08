#neural network with dense layer using OOP Concept in Python with tf
import numpy as np
class Neuron:
    def __init__(self,A_in,W):
        self.__inputn = A_in
        self.Wn = W
    def getneuro(self):
        return np.dot(self.__inputn,self.Wn)

class layer:
#Z = Input.Weight T where bias will be added in the 
    def __init__(self,a_in,units):  
        self.__input  = a_in
        self.__units = units
        self.__W = np.zeros(shape = (self.__units,self.__input.shape[1])).T

    def neuron_trigger(self):
        z  = np.zeros(shape = (1,self.__units))
        
        new_data=[ Neuron(self.__input,self.__W[:, i]) for i in range(self.__units)]
        all_z=[i.getneuro() for i in new_data]
        return np.array(all_z).T
    def activation(self): # following function will output the activation function for the  next layer
        return 1/(1+np.exp(self.neuron_trigger()))
X = np.array([[1,200,17],
[1,220,16],
[1,180,14],
[1,210,17]]) #(x0,x1,x2)
layer_1 = layer(X,3) #example,neurons
#print(layer_1.activation())
layer_2 = layer(layer_1.activation(),2)
#print(layer_2.activation())
layer_3 = layer(layer_2.activation(),1)
print(layer_3.activation())
