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


data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')

ETG=data[data['Galaxy Type']=='ETG']
Spiral=data[data['Galaxy Type']=='Spiral']
print(Spiral['Spectral Index'])
gradient = np.linspace(1, 0, 100).reshape(-1, 1)
plt.imshow(gradient , extent=[9.5,12, -10, 12], aspect='auto', cmap='brg',alpha=0.5,zorder=0)
plt.scatter(ETG['Stellar Mass (Log)'],ETG['Spectral Index'],color='yellow',label='ETG',zorder=2)
plt.scatter(Spiral['Stellar Mass (Log)'],Spiral['Spectral Index'],color='black',label='Spirals',zorder=3)
plt.errorbar(ETG['Stellar Mass (Log)'], ETG['Spectral Index'],yerr=ETG['New Index Error'],fmt='None',ecolor='yellow',zorder=0)
plt.errorbar(Spiral['Stellar Mass (Log)'], Spiral['Spectral Index'], yerr=Spiral['New Index Error'], fmt='None',ecolor='black',zorder=1)
plt.xlabel('log($M_{*}$)')
plt.ylabel('Spectral Index')
plt.legend(frameon=False)
plt.axhline(0,color='black',linestyle='--',zorder=1)
plt.ylim(-10,12)
plt.xlim(9.5,12)
plt.text(9.6,10,'Thermal Dominated')
plt.text(9.6,-8,'Synchrotron Dominated')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/Paper_Plots/Galaxy Type.png')



