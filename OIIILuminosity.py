#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats


# In[2]:


data=pd.read_csv('Documents/Python.csv')
OIIILum=data['Log OIII Lum (erg/s)']
Lbol=(10**(OIIILum))*3500
data['OIII Lbol']=Lbol

# In[3]:


eta=0.1
Acc_rate=(0.15*(0.1/eta))*(Lbol/1e45)
data['OIII Accretion rate']=Acc_rate
data.to_csv('Documents/Python.csv',index=False)


# In[4]:


mass100=data['Mass 100pc']
mass75=data['Mass 75pc']
mass50=data['Mass 50pc']


# In[5]:


plt.loglog(mass100,Acc_rate,'o')
plt.xlabel('Mass 100pc')
plt.ylabel('Accretion rate')
plt.savefig('OIIIMass100.png')
plt.close()

# In[6]:


mass100acc=data[['Mass 100pc','OIII Accretion rate']]
mass100acc=mass100acc.dropna()
OIII100=stats.spearmanr(mass100acc['Mass 100pc'],mass100acc['OIII Accretion rate'])
print(OIII100)

# In[7]:


plt.loglog(mass75,Acc_rate,'o')
plt.xlabel('Mass 75pc')
plt.ylabel('Accretion rate')
plt.savefig('OIIIMass75.png')
plt.close()
# In[8]:


mass75acc=data[['Mass 75pc','OIII Accretion rate']]
mass75acc=mass75acc.dropna()
OIII75=stats.spearmanr(mass75acc['Mass 75pc'],mass75acc['OIII Accretion rate'])
print(OIII75)

# In[9]:


plt.loglog(mass50,Acc_rate,'o')
plt.xlabel('Mass 50pc')
plt.ylabel('Accretion rate')
plt.savefig('OIIIMass50.png')
plt.close()


# In[10]:


mass50acc=data[['Mass 50pc','OIII Accretion rate']]
mass50acc=mass50acc.dropna()
OIII50=stats.spearmanr(mass50acc['Mass 50pc'],mass50acc['OIII Accretion rate'])
print(OIII50)

# In[ ]:




