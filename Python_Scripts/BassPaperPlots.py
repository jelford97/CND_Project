import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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
dect=data[data['Detection']=='Yes']
nondect=data[data['Detection']=='No']
dectSI=dect['Spectral Index']

Bass=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Bass_list.csv')
BassDect=Bass[Bass['Lmm']>0]
BassNoDect=Bass[Bass['Lmm']==0]

SI=data['Spectral Index']
SIerr=data['New Index Error']
mmflux=data['1mm flux density (Jy)']
dectmmflux=dect['1mm flux density (Jy)']
nondectmmflux=nondect['1mm flux density (Jy)']
mmrms=data['RMS']
dectrat=mmflux/mmrms
mmfreq=data['1mm frequency (Hz)']
mmdist=data['Distance (Mpc)']
mmfluxcgs=mmflux*1e-23
mmlum=mmfluxcgs*mmfreq*4*math.pi*(mmdist*3.086e24)**2

jet=data[data['Radio Jet']=='Yes']
nonjet=data[data['Radio Jet']=='No']
jetdect=jet[jet['Detection']=='Yes']
jetnodect=jet[jet['Detection']=='No']
nonjetdect=nonjet[nonjet['Detection']=='Yes']
nonjetnodect=nonjet[nonjet['Detection']=='No']

plt.semilogx(dectrat,SI,'o')
plt.errorbar(dectrat,SI,yerr=SIerr,fmt='None',ecolor='black',zorder=0)
plt.xlabel('Nuclear Smm/Sigma_mm')
plt.ylabel('Nuclear mm Spectral Index')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/Detection.png')
plt.close()

plt.loglog(dectrat,SIerr,'o')
plt.xlabel('Nuclear Smm/Sigma_mm')
plt.ylabel('Nucleaar mm Spectral Index Error')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/SI_err_detection.png')
plt.close()

dectmmcgs=dectmmflux*1e-23
nondectmmcgs=nondectmmflux*1e-23
dectmmfreq=dect['1mm frequency (Hz)']
nondectmmfreq=nondect['1mm frequency (Hz)']
dectdist=dect['Distance (Mpc)']
nondectdist=nondect['Distance (Mpc)']

dectmmlum=dectmmcgs*dectmmfreq*4*math.pi*(dectdist*3.086e24)**2
nondectmmlum=nondectmmcgs*nondectmmfreq*4*math.pi*(nondectdist*3.086e24)**2
dectXrayLum=dect['X-ray Luminosity (ergs/s)']
nondectXrayLum=nondect['X-ray Luminosity (ergs/s)']
X=np.logspace(38,45,100)
Y=1.08*np.log10(X)-7.41
#print(Y)
cmap=plt.get_cmap('brg')
cmap.set_bad('black')
im=plt.scatter(np.log10(dectXrayLum),np.log10(dectmmlum),c=dectSI,cmap=cmap,plotnonfinite=True,label='WISDOM')
plt.scatter(np.log10(nondectXrayLum),np.log10(nondectmmlum),marker='v',color='grey',label='WISDOM non-detection')
plt.scatter(BassDect['L210'],BassDect['Lmm'],marker='s',color='red',label='Bass Dectection')
plt.scatter(BassNoDect['L210'],BassNoDect['e_Lmm'],color='black',marker='v',label='Bass Non-Detection')
plt.plot(np.log10(X),Y,linestyle='--')
plt.legend()
plt.xlabel('2-10 keV X-ray Luminosity (erg/s)')
plt.ylabel('Nuclear mm Luminosity (erg/s)')
plt.colorbar(im,label='Nuclear mm Spectral Index',orientation='horizontal')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/mm_Xray.png')
plt.close()



jetmm=jetdect['1mm flux density (Jy)']
jetxray=jetdect['X-ray Luminosity (ergs/s)']
jetdist=jetdect['Distance (Mpc)']
jetfreq=jetdect['1mm frequency (Hz)']
jetmmcgs=jetmm*1e-23

njetmm=nonjetdect['1mm flux density (Jy)']
njetxray=nonjetdect['X-ray Luminosity (ergs/s)']
njetdist=nonjetdect['Distance (Mpc)']
njetfreq=nonjetdect['1mm frequency (Hz)']
njetmmcgs=njetmm*1e-23

jetmmlum=jetmmcgs*jetfreq*4*math.pi*(jetdist*3.086e24)**2
njetmmlum=njetmmcgs*njetfreq*4*math.pi*(njetdist*3.086e24)**2

XrayLum=data['X-ray Luminosity (ergs/s)']

jetrms=jetdect['RMS']
njetrms=nonjetdect['RMS']
jetmmlumerror=jetmmlum*(jetrms/jetmm)
njetmmlumerror=njetmmlum*(njetrms/njetmm)

logjetmmlumerr=0.434*(jetmmlumerror/jetmmlum)
lognjetmmlumerr=0.434*(njetmmlumerror/njetmmlum)

jetxrayerr=jetdect['X-ray Luminosity Uncertainty (ergs/s)']
njetxrayerr=nonjetdect['X-ray Luminosity Uncertainty (ergs/s)']

logjetxrayerr=0.434*(jetxrayerr/jetxray)
lognjetxrayerr=0.434*(njetxrayerr/njetxray)

plt.scatter(np.log10(jetxray),np.log10(jetmmlum),label='WISDOM Jetted Source')
plt.scatter(np.log10(njetxray),np.log10(njetmmlum),label='WISDOM Non-Jetted Source')
plt.errorbar(np.log10(jetxray),np.log10(jetmmlum),yerr=logjetmmlumerr,xerr=logjetxrayerr,fmt='None',ecolor='black',zorder=0)
plt.errorbar(np.log10(njetxray),np.log10(njetmmlum),yerr=lognjetmmlumerr,xerr=lognjetxrayerr,fmt='None',ecolor='black',zorder=0)
plt.scatter(np.log10(nondectXrayLum),np.log10(nondectmmlum),marker='v',color='black',label='WISDOM Non-Detection')
plt.scatter(BassDect['L210'],BassDect['Lmm'],color='grey',marker='s',label='BASS',zorder=0)
plt.errorbar(BassDect['L210'],BassDect['Lmm'],yerr=BassDect['e_Lmm'],xerr=BassDect['e_L210'],fmt='None',ecolor='black',zorder=-1)
plt.scatter(BassNoDect['L210'],BassNoDect['e_Lmm'],color='grey',marker='v',label='BASS Non-Detection',zorder=0)
plt.plot(np.log10(X),Y,linestyle='--',color='black')
plt.legend(frameon=False,prop={'size':10}, loc='lower right')
plt.xlabel('2-10 keV X-ray Luminosity (erg/s)')
plt.ylabel('Nuclear mm Luminosity (erg/s)')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/mm_Xray_Jet.pdf')
plt.close()

XrayLbol=data['Bolometric Luminosity (erg/s)']
OIIILbol=data['OIII Lbol']

plt.scatter(np.log10(XrayLbol),np.log10(mmlum),label='WISDOM')
plt.xlabel('X-ray Traced Bolometric Luminosity (erg/s)')
plt.ylabel('Nuclear mm Luminosity (erg/s)')
#plt.legend()
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/mm_XrayLbol.png')
plt.close()

plt.scatter(np.log10(OIIILbol),np.log10(mmlum))
plt.xlabel('OIII Traced Bolometric Luminosity (erg/s)')
plt.ylabel('Nuclear mm Luminosity (erg/s)')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/mm_OIIILbol.png')
plt.close()

SFR=10**data['Tim SFR Log']
Tsize=data['Total Size (as)']
totsize=4.84*Tsize*mmdist
totsizekpc=totsize/1e3
SFRSD=SFR/(math.pi*(totsizekpc)**2)

plt.scatter(np.log10(SFRSD),SI)
plt.xlabel('SFR Surface Density')
plt.ylabel('Spectral Index')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/SI_SFRSD.png')
plt.close()

plt.scatter(np.log10(XrayLum),SI)
plt.xlabel('log 2-10 keV X-ray Luminosity')
plt.ylabel('Spectral Index')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/SI_Xray.png')
plt.close()

plt.scatter(np.log10(XrayLbol),SI)
plt.xlabel('X-ray Traced Lbol')
plt.ylabel('SI')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/SI_XrayLbol.png')
plt.close()

plt.scatter(np.log10(OIIILbol),SI)
plt.xlabel('OIII Traced Lbol')
plt.ylabel('SI')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/SI_OIIILbol.png')
plt.close()
