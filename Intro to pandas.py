#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[7]:


# 2 main datatypes
series = pd.Series(["BMW", "Toyota","Honda"])


# In[8]:


series


# In[12]:


color  = pd.Series(["Red", "Blue","White"])
color


# In[13]:


#Data frame are 2 Dimensional


# In[15]:


car_data = pd.DataFrame({"Car make": series, "Colours": color})
car_data


# In[114]:


df2 = pd.read_csv("car_sales.csv")
df2


# In[53]:


df2.to_csv("Exorted.csv", index = False) #EXPORTS THE dataframe into CSV


# ## Describe Data
# 

# In[62]:


#attribute doesnot have bracket at the end, functions do have such ()
df2.dtypes #shows column with data type


# In[63]:


df2.columns


# In[65]:


car = df2.columns
car #stored as lists


# In[66]:


df2.index #index of the columns


# In[68]:


df2.describe() #statistival values


# In[125]:


df2.mean()


# In[81]:


avg = pd.Series([30,10,20])
avg.mean()


# In[75]:


df2["Engine_size"].sum()


# In[76]:


len(df2)


# In[124]:


df2.head(10)


# In[123]:


df2.tail(3)


# In[97]:


#.loc & .iloc
fds = pd.Series(["Asim", "Asdaq","Kharal","Shahab", "Qasim","Haris"], index = [0,3,3,8,9,10])
fds #gives custom indexes


# In[122]:


fds.loc[3] #shows that particular index


# In[121]:


df2


# In[120]:


df2.loc[2]


# In[119]:


#.iloc
fds.iloc[3] #shows the position


# In[118]:


df2


# In[105]:


df2.iloc[2]


# In[117]:


df2["Engine_size"]


# In[110]:


df2.Engine_size


# In[116]:


df2["Sales pkr"]


# In[130]:


df2[df2.Engine_size == 3.8]


# In[132]:


df2[df2.Manufacturer == "Kia" ]


# In[136]:


df2[df2["Manufacturer"] == "Kia" ]


# In[137]:


df2


# In[142]:


pd.crosstab(df2["Manufacturer"],df2["Engine_size"])


# In[148]:


df2


# In[147]:


#grouping

df2.groupby(["Manufacturer"]).mean()


# In[152]:


df2["Engine_size"].plot(kind="bar")


# In[153]:


df2["Engine_size"].plot()


# In[154]:


df2["Engine_size"].hist()


# In[155]:


df2


# In[159]:


df2['Price']=df2['Wheelbase']
df2


# In[166]:


df2['Price'] = df2['Price'].astype(int)
df2


# In[168]:


df2.Price.plot(kind = "bar")


# ## Manipulating Data

# In[169]:


df2["Manufacturer"].str.lower()


# In[225]:


df3= pd.read_csv("missing.csv")
df3


# In[226]:


df3['Sales pkr'] = df3['Sales pkr'].fillna(df3['Sales pkr'].mean())
df3


# In[227]:


df3.dropna(inplace =True)
df3


# In[235]:


df3['wheelcount'] = 4;
df3


# In[236]:


df3 = df3.drop("wheelcount",axis = 1)


# In[237]:


df3


# In[ ]:




