import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from IzumiLbol import EddFrac

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

TimData=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Tim_data_New.csv')
Data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')
Izumi=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/IzumiCND.csv')
GB=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/GBData.csv')
Babyk=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Babyk.csv')

MLbol=TimData['OIII Bolometric Luminosity (erg/s)']
MeddFrac=TimData['Eddington Fraction']
TMBH=TimData['log M_BH']

ILbol=Izumi['Lbol']
IeddFrac=Izumi['Eddington Fraction']
IMBH=Izumi['MBH']

GBLbol=GB['Lbol']
GBMBH=GB['MBH']
GBEddFrac=GB['Eddington Fraction']

MJetPower=Data['Jet Power']
BJetPower=Babyk['Jet Power']

plt.hist(np.log10(MeddFrac),color='red',zorder=1,bins=10,label='This work',histtype='step',linewidth=3)
plt.hist(np.log10(IeddFrac),color='blue',zorder=2,bins=11,label='Izumi+16',histtype='step',linewidth=1.5)
plt.hist(np.log10(GBEddFrac),color='black',zorder=0,bins=11,label='Garcia-Burillo+21',histtype='step',linewidth=4.5)
plt.legend(frameon=False,loc=2,fontsize=8)
plt.xlabel('log($\lambda_{Edd}$)')
plt.ylabel('Count')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/EddFracHist.pdf')
plt.close()

plt.hist(TMBH,color='red',zorder=0,bins=8,label='This work',histtype='step',linewidth=4.5)
plt.hist(IMBH,color='blue',zorder=1,bins=6,label='Izumi+16',histtype='step',linewidth=3)
plt.hist(GBMBH,color='black',zorder=2,bins=3,label='Garcia-Burillo+21',histtype='step',linewidth=1.5)
plt.legend(frameon=False,loc=0,fontsize=8)
plt.xlabel('log$M_{BH}(M_{\odot}$)')
plt.ylabel('Count')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/MBHHist.pdf')
plt.close()

plt.hist(np.log10(MLbol),color='red',zorder=0,bins=10,label='This work',histtype='step',linewidth=4.5)
plt.hist(np.log10(ILbol),color='blue',zorder=2,bins=11,label='Izumi+16',histtype='step',linewidth=1.5)
plt.hist(np.log10(GBLbol),color='black',zorder=1,bins=12,label='Garcia-Burillo+21',histtype='step',linewidth=3)
plt.legend(frameon=False,loc=2,fontsize=8)
plt.xlabel('log$L_{Bol}(erg \, s^{-1}$)')
plt.ylabel('Count')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/LbolHist.pdf')
plt.close()

plt.hist(np.log10(MJetPower),color='red',zorder=0,bins=10,label='This work',histtype='step',linewidth=3)
plt.hist(np.log10(BJetPower),color='black',zorder=1,bins=6,label='Babyk+19',histtype='step',linewidth=1.5)
plt.legend(frameon=False,loc=2,fontsize=8)
plt.xlabel('log$P_{Jet}(erg \, s^{-1}$)')
plt.ylabel('Count')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/JetPowerHist.pdf')
plt.close()

Mvdisp=Data['Sigma Star (km/s)']
GBvdisp=GB['Central Velocity Dispersion (km/s)']


plt.hist(np.log10(Mvdisp),color='red',zorder=0,bins=21,label='This work',histtype='step',linewidth=3)
plt.hist(np.log10(GBvdisp),color='black',zorder=1,bins=5,label='Garcia-Burillo+21',histtype='step',linewidth=1.5)
plt.legend(frameon=False,loc=2,fontsize=8)
plt.xlabel('log $\sigma_{*} (km\,s^{-1})$')
plt.ylabel('Count')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/VelocityDispHist.pdf')
plt.close()

