#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
#from scipy.optimize import curve_fit
import math
#from gastimator import gastimator
#from gastimator import corner_plot


# In[3]:


data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')


# In[137]:


i=float(input("What galaxy index? "))
LSBfreq=data['LSB Frequency (Hz)']
LSB=data['LSB Flux Density']
LSBrms=data['LSB RMS']
USBfreq=data['USB Frequency (Hz)']
USB=data['USB Flux Density']
USBrms=data['USB RMS']
almafreq=np.array([LSBfreq[i],USBfreq[i]])
alma=np.array([LSB[i],USB[i]])
almarms=np.array([LSBrms[i],USBrms[i]])
logAfreq=np.log10(almafreq)
logAlma=np.log10(alma)
logAlmarms=np.log10(almarms)


# In[138]:


def index(ALMAfreq,ALMA):
    lalma=np.log10(ALMA)
    lalmafreq=np.log10(ALMAfreq)
    m=(lalma[1]-lalma[0])/(lalmafreq[1]-lalmafreq[0])
    return m


# In[139]:


m=index(almafreq,alma)
print(m)


# In[140]:


def indexerr3(Almafreq,ALMA,ALMArms,m,freqerr):
    lfreq=np.log10(Almafreq)
    lfreqerr=0.434*(freqerr/Almafreq)
    lalma=np.log10(ALMA)
    lalmaerr=0.434*(ALMArms/ALMA)
    dy=np.sqrt(((lalmaerr[1])**2)+((lalmaerr[0])**2))
    dx=np.sqrt(((lfreqerr[1])**2)+((lfreqerr[0])**2))
    x=lfreq[1]-lfreq[0]
    y=lalma[1]-lalma[0]

    merr=np.abs(m)*np.sqrt(((dx/x)**2)+((dy/y)**2))
    merrold=np.abs(m)*np.sqrt((dy/y)**2)
    return merr,merrold


# In[141]:

inerr=indexerr3(almafreq,alma,almarms,m,4e9)

print(inerr[1])
print(inerr[0])


# In[ ]:




