#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello world")


# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn


# ## Heart Disease Project
# This project is classifying whether a patient has disease or not
# Learning the libraries
# 

# In[5]:


import pandas as pd


# In[10]:


df = pd.read_csv("dildata.csv")


# In[11]:


df.head(10)


# In[26]:


import matplotlib.pyplot as plt


# In[24]:


df.sex.value_counts() 


# In[34]:


df.sex.value_counts().plot(kind="bar")


# ## Learning Flow

# ![](stepsml.jpeg)

# ## 1. Problem Definition
# 
# Predict Heart disease

# In[ ]:





# ## 2. Data
# This is the data we are tryna use in Model

# In[ ]:




