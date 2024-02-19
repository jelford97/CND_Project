#!/usr/bin/env python
# coding: utf-8

# In[20]:


import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt


# In[21]:


data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')
synch=data[data['Dominant']=='Synch']
therm=data[data['Dominant']=='Thermal']
dect=data[data['Detection']=='Yes']
dects=dect[dect['Dominant']=='Synch']
dectt=dect[dect['Dominant']=='Thermal']
em=['Excess Radio Log','X-ray Luminosity (ergs/s)','1mm flux density (Jy)','Accretion rate (M_solar/yr)']
mass=['Mass 100pc','Mass 75pc','Mass 50pc']


# In[24]:


i=3
j=2
if i==2:
    emms=dect[[em[i],mass[j]]]
else:
    emms=data[[em[i],mass[j]]]
emmsdn=emms.dropna()
Stat=stats.spearmanr(emmsdn[mass[j]],emmsdn[em[i]])
print(Stat)





