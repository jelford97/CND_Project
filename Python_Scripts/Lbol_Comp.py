import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math


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

data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')
OIIILbol=data['OIII Lbol']
XrayLbol=data['Bolometric Luminosity (erg/s)']
OIIILbolerror=data['OIII Lbol error']

plt.loglog(XrayLbol,OIIILbol,'o')
plt.errorbar(XrayLbol,OIIILbol,xerr=XrayLbol*0.1,yerr=OIIILbolerror,fmt='None',ecolor='k',zorder=0)
plt.ylabel('$L_{Bol,OIII}\,(erg\,s^{-1})$')
plt.xlabel('$L_{Bol,X-ray}\,(erg\,s^{-1})$')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/Paper_Plots/LbolComp.pdf',bbox_inches='tight')