#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data=pd.read_csv('Documents/Python.csv')


# In[3]:


totmass=np.array(data['Total Mass'])
mass100=np.array(data['Mass 100pc'])
mass75=np.array(data['Mass 75pc'])
mass50=np.array(data['Mass 50pc'])


# In[4]:


massfrac100=(mass100/totmass)*100
massfrac75=(mass75/totmass)*100
massfrac50=(mass50/totmass)*100


# In[5]:


print(massfrac100)


# In[6]:


print(massfrac75)


# In[7]:


print(massfrac50)


# In[ ]:




