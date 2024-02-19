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
dect=data[data['Detection']=='Yes']
nondect=data[data['Detection']=='No']

jetdect=dect[dect['Radio Jet']=='Yes']
njetdect=dect[dect['Radio Jet']=='No']

jetdectRadioLum=jetdect['Radio Luminosity (erg/s)']
njetdectRadioLum=njetdect['Radio Luminosity (erg/s)']
nondectRadioLum=nondect['Radio Luminosity (erg/s)']

jetdectmmflux=jetdect['1mm flux density (Jy)']
jetdectmmfreq=jetdect['1mm frequency (Hz)']
jetdectdist=jetdect['Distance (Mpc)']
jetdectmmcgs=jetdectmmflux*1e-23
jetdectmmlum=jetdectmmcgs*jetdectmmfreq*4*math.pi*(jetdectdist*3.086e24)**2
jetrms=jetdect['RMS']
jetlumerr=jetdectmmlum*(jetrms/jetdectmmflux)
logjeterr=0.434*(jetlumerr/jetdectmmlum)

njetdectmmflux=njetdect['1mm flux density (Jy)']
njetdectmmfreq=njetdect['1mm frequency (Hz)']
njetdectdist=njetdect['Distance (Mpc)']
njetdectmmcgs=njetdectmmflux*1e-23
njetdectmmlum=njetdectmmcgs*njetdectmmfreq*4*math.pi*(njetdectdist*3.086e24)**2
njetrms=njetdect['RMS']
njetlumerr=njetdectmmlum*(njetrms/njetdectmmflux)
lognjeterr=0.434*(njetlumerr/njetdectmmlum)

nondectmmflux=nondect['1mm flux density (Jy)']
nondectfreq=nondect['1mm frequency (Hz)']
nondectdist=nondect['Distance (Mpc)']
nondectcgs=nondectmmflux*1e-23
nondectmmlum=nondectcgs*nondectfreq*4*math.pi*(nondectdist*3.086e24)**2

jetradioerr=jetdect['Radio Luminosity Error (L_solar)']*3.826e33
njetradioerr=njetdect['Radio Luminosity Error (L_solar)']*3.826e33

Rlogjeterr=0.434*(jetradioerr/jetdectRadioLum)
Rlognjeterr=0.434*(njetradioerr/njetdectRadioLum)

#dectSI=dect['Spectral Index']
#cmap=plt.get_cmap('brg')
#cmap.set_bad('black')

plt.scatter(np.log10(jetdectRadioLum),np.log10(jetdectmmlum),label='WISDOM Jetted Source')
plt.scatter(np.log10(njetdectRadioLum),np.log10(njetdectmmlum),label='WISDOM Non-Jetted Source')
plt.scatter(np.log10(nondectRadioLum),np.log10(nondectmmlum),color='grey',marker='v',label='WISDOM Non-Detection')
plt.errorbar(np.log10(jetdectRadioLum),np.log10(jetdectmmlum),yerr=logjeterr,xerr=Rlogjeterr,fmt='None',ecolor='black',zorder=0)
plt.errorbar(np.log10(njetdectRadioLum),np.log10(njetdectmmlum),yerr=lognjeterr,xerr=Rlognjeterr,fmt='None',ecolor='black',zorder=0)
plt.legend(frameon=False,loc=0,prop={'size':10})
#plt.colorbar(im,label='Nuclear mm Spectral Index',orientation='horizontal')
plt.xlabel('Radio Luminosity (erg/s)')
plt.ylabel('Nuclear mm Luminosity (erg/s)')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/Radio_mm_jet.pdf')
plt.close()
