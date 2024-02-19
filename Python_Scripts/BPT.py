import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Latin Modern Roman'
plt.rcParams.update({'font.size': 10})
plt.rcParams['legend.fontsize'] = 14
plt.rcParams['axes.linewidth'] = 1.5
plt.rcParams['xtick.labelsize'] = 10;
plt.rcParams['ytick.labelsize'] = 10
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
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['ytick.right']=True
plt.rcParams['xtick.top']=True

data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/BPT_Data.csv')

Galaxies=data['Galaxy']
OIII_HB=data['log(OIII/H_beta)']
NII_HA=data['log(NII/H_alpha)']

XK1=np.linspace(-1.5,0.3)
YK1=(0.61/(XK1-0.47))+1.19

XS7=np.linspace(-0.180,1.5)
YS7=1.05*XS7+0.45

XK3=np.linspace(-1.5,0.)
YK3=0.61/(XK3-0.05)+1.3


for i in range(len(Galaxies)):
    if np.isnan(OIII_HB[i])==True or np.isnan(NII_HA[i])==True:
        print('passed')
        pass
    else:
        plt.plot(NII_HA[i],OIII_HB[i],'o')
        plt.plot(XK1,YK1,'--',color='black')
        plt.plot(XS7,YS7,'--',color='black')
        plt.plot(XK3,YK3,'--',color='black')
        plt.xlabel(r"log([NII] $\lambda$ 6583/H$\alpha$)")
        plt.ylabel(r"log([OIII] $\lambda$ 5007/H$\beta$)")
        plt.text(-1,1,'AGN')
        plt.text(0.5,0,'LINER')
        plt.text(-0.2,-1,'Comp')
        plt.text(-1,-1,'HII')
        plt.xlim(-1.2,1.2)
        plt.ylim(-1.5,1.5)
        plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/BPT_Diagrams/'+str(Galaxies[i])+'BPT.png')
        plt.close()