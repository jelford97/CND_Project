#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl


# In[2]:


plt.rcParams['font.family'] = 'Latin Modern Roman'
plt.rcParams.update({'font.size': 10})
plt.rcParams['legend.fontsize'] = 14
plt.rcParams['axes.linewidth'] = 1.5
plt.rcParams['xtick.labelsize'] = 12;
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['xtick.major.size'] = 10;
plt.rcParams['ytick.major.size'] = 10
plt.rcParams['xtick.major.width'] = 2;
plt.rcParams['ytick.major.width'] = 2
plt.rcParams['xtick.minor.size'] = 5;
plt.rcParams['ytick.minor.size'] = 5
plt.rcParams['xtick.minor.width'] = 1;
plt.rcParams['ytick.minor.width'] = 1
plt.rcParams['xtick.direction'] = 'in';
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['xtick.bottom'] = True
plt.rcParams['ytick.left'] = True
params = {'mathtext.default': 'regular'}
plt.rcParams.update(params)
plt.rcParams['axes.labelsize'] = 16
plt.rcParams['ytick.right']=True
plt.rcParams['xtick.top']=True


# In[3]:


data=pd.read_csv('Documents/Python.csv')
data1=pd.read_csv('Documents/Table 1.csv')


# In[4]:


SI=data['Spectral Index']
Morph=data['Hubble Type']
GalaxyType=data1['Galaxy Type']

WISDOM=pd.read_csv('/home/jacob/Documents/WISDOM_basic_params(1).csv')

SI=WISDOM['Spectral Index']
logMstar=WISDOM['LogMstar']
galaxy=data1['Galaxy']

fulldata={'Galaxy':galaxy,'Galaxy Type':GalaxyType,'Spectral Index':SI,'Stellar Mass':logMstar}
fdf=pd.DataFrame(fulldata)
ETG=fdf[fdf['Galaxy Type']=='ETG']
Spiral=fdf[fdf['Galaxy Type']=='Spiral']
Dwarf=fdf[fdf['Galaxy Type']=='Dwarf']

gradient = np.linspace(1, 0, 100).reshape(-1, 1)
plt.imshow(gradient , extent=[9.5,12, -4, 4], aspect='auto', cmap='brg',alpha=0.5,zorder=0)
plt.scatter(ETG['Stellar Mass'],ETG['Spectral Index'],color='yellow',label='ETG',zorder=2)
plt.scatter(Spiral['Stellar Mass'],Spiral['Spectral Index'],color='black',label='Spirals',zorder=2)
plt.xlabel('log($M_{*}$)')
plt.ylabel('Spectral Index')
plt.legend(frameon=False)
plt.axhline(0,color='black',linestyle='--',zorder=1)
plt.ylim(-4,4)
plt.xlim(9.5,12)
plt.text(9.6,3.1,'Thermal Dominated')
plt.text(9.6,-3.5,'Synchrotron Dominated')
plt.savefig('Galaxy Type.png')



