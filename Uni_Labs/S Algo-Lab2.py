#Finding S algorithm Lab#2 ML
import pandas as pd
import numpy as np

#reading file and mking dataframe
data = pd.read_csv('data/findingSdataset.csv')
#taking only positive examples and dropping the example type column
data = data[data.Target !="No"].drop(columns=["Target"],axis=1)
#initializing the hypothesis array
inthyp = np.array(data.head(1))
#iterating the row and replacing the value
dataarray = np.array(data.tail(len(data)-1))
compared = (inthyp == dataarray)
len = compared.shape[0]
for i in range (len):
    inthyp = inthyp * compared[i]
inthyp = np.where(inthyp=='','?',inthyp)
#braodcasting
inthyp = inthyp.reshape(inthyp.shape[1],)
#output
print(inthyp)