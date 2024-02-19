import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

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

MLbolD=TimData['OIII Bolometric Luminosity (erg/s)']
MLbol=MLbolD[~np.isnan(MLbolD)]
MeddFracD=TimData['Eddington Fraction']
TMBHD=TimData['log M_BH']
TMBH=TMBHD[~np.isnan(TMBHD)]
MeddFrac=MeddFracD[~np.isnan(MeddFracD)]

ILbol=Izumi['Lbol']
IeddFrac=Izumi['Eddington Fraction']
IMBH=Izumi['MBH']

GBLbol=GB['Lbol']
GBMBH=GB['MBH']
GBEddFrac=GB['Eddington Fraction']

MJetPowerD=Data['Jet Power']
MJetPower=MJetPowerD[~np.isnan(MJetPowerD)]
BJetPower=Babyk['Jet Power']

MvdispD=Data['Sigma Star (km/s)']
Mvdisp=MvdispD[~np.isnan(MvdispD)]
GBvdispD=GB['Central Velocity Dispersion (km/s)']
GBvdisp=GBvdispD[~np.isnan(GBvdispD)]

LbolData=[np.log10(np.array(MLbol)),np.log10(np.array(ILbol)),np.log10(np.array(GBLbol))]
MBHData=[np.array(TMBH),np.array(IMBH),np.array(GBMBH)]
EddFracData=[np.log10(np.array(MeddFrac)),np.log10(np.array(IeddFrac)),np.log10(np.array(GBEddFrac))]
JetData=[np.log10(np.array(MJetPower)),np.log10(np.array(BJetPower))]
VdispData=[np.log10(np.array(Mvdisp)),np.log10(np.array(GBvdisp))]

colors_3=['blue','red','gold']
colors_2=['blue','gold']
colors_2B=['blue','orangered']
Labels=['This Work','Izumi+16','Garcia-Burillo+21']
JLabels=['This Work','Babyk+19']
VDLabels=['This Work','Garcia-Burillo+21']

fig, ax=plt.subplots()
vp=ax.violinplot(LbolData,showmedians=True)
for pc, color  in zip(vp['bodies'],colors_3):
    pc.set_facecolor(color)
vp['cmedians'].set_color(colors_3)
vp['cmins'].set_color(colors_3)
vp['cmaxes'].set_color(colors_3)
vp['cbars'].set_color(colors_3)
ax.set_xticks([1,2,3])
ax.set_xticklabels(Labels)
ax.set_xlabel('Sample')
ax.set_ylabel('log$L_{Bol}(erg \, s^{-1}$)')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/Lbol_VP.pdf')

fig1,ax1=plt.subplots()
vp1=ax1.violinplot(MBHData,showmedians=True)
for pc, color  in zip(vp1['bodies'],colors_3):
    pc.set_facecolor(color)
vp1['cmedians'].set_color(colors_3)
vp1['cmins'].set_color(colors_3)
vp1['cmaxes'].set_color(colors_3)
vp1['cbars'].set_color(colors_3)
ax1.set_xticks([1,2,3])
ax1.set_xticklabels(Labels)
ax1.set_xlabel('Sample')
ax1.set_ylabel('log$M_{BH}(M_{\odot}$)')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/MBH_VP.pdf')

fig2,ax2=plt.subplots()
vp2=ax2.violinplot(EddFracData,showmedians=True)
for pc, color  in zip(vp2['bodies'],colors_3):
    pc.set_facecolor(color)
vp2['cmedians'].set_color(colors_3)
vp2['cmins'].set_color(colors_3)
vp2['cmaxes'].set_color(colors_3)
vp2['cbars'].set_color(colors_3)
ax2.set_xticks([1,2,3])
ax2.set_xticklabels(Labels)
ax2.set_xlabel('Sample')
ax2.set_ylabel('log($\lambda_{Edd}$)')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/EddFrac_VP.pdf')

fig3, ax3=plt.subplots()
vp3=ax3.violinplot(JetData,showmedians=True)
for pc, color  in zip(vp3['bodies'],colors_2):
    pc.set_facecolor(color)
vp3['cmedians'].set_color(colors_2B)
vp3['cmins'].set_color(colors_2B)
vp3['cmaxes'].set_color(colors_2B)
vp3['cbars'].set_color(colors_2B)
ax3.set_xticks([1,2])
ax3.set_xticklabels(JLabels)
ax3.set_xlabel('Sample')
ax3.set_ylabel('log$P_{Jet}(erg \, s^{-1}$)')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/JetPower_VP.pdf')

fig4, ax4=plt.subplots()
vp4=ax4.violinplot(VdispData,showmedians=True)
for pc, color  in zip(vp4['bodies'],colors_2):
    pc.set_facecolor(color)
vp4['cmedians'].set_color(colors_2)
vp4['cmins'].set_color(colors_2)
vp4['cmaxes'].set_color(colors_2)
vp4['cbars'].set_color(colors_2)
ax4.set_xticks([1,2])
ax4.set_xticklabels(VDLabels)
ax4.set_xlabel('Sample')
ax4.set_ylabel('log $\sigma_{*} (km\,s^{-1})$')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/VelocityDisp_VP.pdf')
