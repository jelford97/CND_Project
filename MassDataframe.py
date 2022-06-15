#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data=pd.read_csv('Documents/Python.csv')


# In[3]:


galaxy=data['Galaxy']
mass100=data['Mass 100pc']
mass75=data['Mass 75pc']
mass50=data['Mass 50pc']
mass100err=data['Mass 100pc Error']
mass75err=data['Mass 75pc Error']
mass50err=data['Mass 50pc Error']


# In[4]:


logmass100=np.around(np.log10(mass100),2)
logmass75=np.around(np.log10(mass75),2)
logmass50=np.around(np.log10(mass50),2)


# In[5]:


logmass100err=np.around(np.log10(mass100+mass100err)-logmass100,2)
logmass75err=np.around(np.log10(mass75+mass75err)-logmass75,2)
logmass50err=np.around(np.log10(mass50+mass50err)-logmass50,2)


# In[6]:


massdata={'Galaxy':galaxy,'log Mass 100pc':logmass100,'log Mass 100pc error':logmass100err,'log Mass 75pc':logmass75,'log Mass 75pc error':logmass75err,'log Mass 50pc':logmass50,'log Mass 50pc error':logmass50err}


# In[7]:


df=pd.DataFrame(massdata)


# In[8]:


df.to_csv('logmassdata.csv')


# In[9]:


Tab=pd.read_csv('Documents/Table 2.csv')


# In[10]:


mmrms=data['RMS']


# In[11]:


mmrmsmjy=mmrms/1e-3


# In[12]:


Tab['mm RMS']=mmrmsmjy

Tab.to_csv('Documents/Table 2.csv',index=False)

# In[ ]:




