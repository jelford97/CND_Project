#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


# In[2]:


data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')


# In[3]:


D=data['Distance (Mpc)']
Fr=1.4e9
Telc=1e4


# In[4]:


SFRtot=data['Total Mass']/2e9


# In[5]:


def radio_flux(SFR,Te,fr,dist):
    radiolum=(SFR/1e-27)*(2.18*(Te/1e4)**0.45*(fr/1e9)**(-0.1)+15.1*(fr/1e9)**-0.8)
    d=dist*3.086e24
    radio=radiolum/(4*math.pi*(d)**2)
    radioflux=radio/1e-23
    return radioflux


# In[6]:


totrf=radio_flux(SFRtot,Telc,Fr,D)


# In[7]:


data['Total Radio Flux SFR']=totrf
data.to_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv',index=False)

# In[8]:


x=np.logspace(-5,-1,100)
y=x


# In[9]:


plt.loglog(data['Total Radio Flux SFR'],data['Radio Flux (Jy)'],'o')
plt.loglog(x,y,color='black',linestyle='--')
plt.xlabel('Total Radio Flux from SF')
plt.ylabel('Measured Radio Flux')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/Radio Flux SFR.png',bbox_inches='tight')



print(data['Radio Flux (Jy)']/data['Total Radio Flux SFR'])









