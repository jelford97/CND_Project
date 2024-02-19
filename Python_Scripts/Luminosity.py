import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.stats as stats

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
GBData=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/GBData.csv')
GB200=GBData['SD 200pc']
GB50=GBData['SD 50pc']
GBXraydata=GBData['X-ray Luminosity']

GBSD200=10**(GB200)
GBSD50=10**(GB50)
GBXray=10**(GBXraydata)

GBSDratio=np.log10(GBSD50/GBSD200)

RadioLum=data['Radio Luminosity (erg/s)']
RadioLumErr=data['Radio Luminosity Error (L_solar)']*3.826e33
mmflux=data['1mm flux density (Jy)']*1e-23
mmfreq=data['1mm frequency (Hz)']
dist=data['Distance (Mpc)']
mmlum=mmflux*mmfreq*4*math.pi*(dist*3.086e24)**2
Xraylum=data['X-ray Luminosity (ergs/s)']
XrayLumErr=data['X-ray Luminosity Uncertainty (ergs/s)']
Mass200Err=data['Mass 200pc Error']
Mass50Err=data['Mass 50pc Error']
sd200pc=data['Mass 200pc']/(math.pi*200**2)
data['log10 Surface Density 200pc']=np.round(np.log10(sd200pc),2)
sd200pcerr=sd200pc*(Mass200Err/data['Mass 200pc'])
logSD200err=0.434*(sd200pcerr/sd200pc)
data['log10 Surface Density 200pc error']=np.round(logSD200err,2)
sd50pc=data['Mass 50pc']/(math.pi*50**2)
data['log10 Surface Density 50pc']=np.round(np.log10(sd50pc),2)
sd50pcerr=sd50pc*(Mass50Err/data['Mass 50pc'])
logSD50err=0.434*(sd50pcerr/sd50pc)
data['log10 Surface Density 50pc error']=np.round(logSD50err,2)
sdratio=np.log10(sd50pc/sd200pc)
sdratioerr=0.434*(np.sqrt((sd200pcerr/sd200pc)**2+(sd50pcerr/sd50pc)**2))
data['Surface Density Ratio']=sdratio
data.to_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv',index=False)

plt.semilogx(RadioLum,sdratio,'o')
plt.errorbar(RadioLum,sdratio,yerr=sdratioerr,xerr=RadioLumErr,fmt='None',ecolor='black',zorder=0)
#plt.yscale('log')
plt.xlabel('log 1.4 GHz Luminosity (erg/s)')
plt.ylabel('$log(\Sigma^{50pc}_{H_2}/\Sigma^{200pc}_{H_2})$')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/RadioLumMassNew.png',bbox_inches='tight')
plt.close()


plt.semilogx(Xraylum,sdratio,'o',color='blue',label='WISDOM')
plt.semilogx(GBXray,GBSDratio,'o',color='red',label='GATOS')
plt.errorbar(Xraylum,sdratio,yerr=sdratioerr,xerr=XrayLumErr,fmt='None',ecolor='black',zorder=0)
plt.errorbar(GBXray, GBSDratio,yerr=0.2,xerr=1.41,fmt='None',ecolor='black',zorder=0)
#plt.yscale('log')
plt.xlabel('$L_{x,2-10}$ (erg/s)')
plt.ylabel('$log_{10}(\Sigma^{50pc}_{H_2}/\Sigma^{200pc}_{H_2})$')
plt.legend(frameon=True)
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/XrayLumMass.pdf',bbox_inches='tight')
plt.close()

plt.semilogx(mmlum,sdratio,'o',color='blue')
plt.xlabel('Nuclear mm luminosity (erg/s)')
plt.ylabel('$log(\Sigma^{50pc}_{H_2}/\Sigma^{200pc}_{H_2})$')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/mmLumMass.png')
plt.close()

Xrayrankdata=data[['Surface Density Ratio','X-ray Luminosity (ergs/s)']]
Radiorankdata=data[['Surface Density Ratio','Radio Luminosity (erg/s)']]

Xrayrankdrop=Xrayrankdata.dropna()
Radiorankdrop=Radiorankdata.dropna()

Xraystat=stats.spearmanr(Xrayrankdrop['X-ray Luminosity (ergs/s)'],Xrayrankdrop['Surface Density Ratio'])
Radiostat=stats.spearmanr(Radiorankdrop['Radio Luminosity (erg/s)'],Radiorankdrop['Surface Density Ratio'])

print(Xraystat)
print(Radiostat)
