import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import scipy.stats as stats

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
plt.rcParams['axes.labelsize'] = 16
plt.rcParams['ytick.right']=True
plt.rcParams['xtick.top']=True

data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')
mm=data['mm Luminosity (erg/s)']
radio=data['Excess Radio Log']
xray=data['X-ray Luminosity (ergs/s)']
OIII=10**(data['Log OIII Lum (erg/s)'])
mmerr=data['mm Luminosity Uncertainty (erg/s)']
radioerr=data['Excess Radio Log Error']
xrayerr=data['X-ray Luminosity Uncertainty (ergs/s)']
OIIIerr=data['OIII Lum err (erg/s)']

fig=plt.figure(figsize=(10,10))
ax1=plt.subplot(337)
plt.loglog(OIII,xray,'o')
plt.xticks(fontsize=12)
plt.yticks(fontsize=14)
plt.minorticks_off()
plt.errorbar(OIII,xray,xerr=OIIIerr,yerr=xrayerr,fmt='None',ecolor='k',zorder=0)
plt.xlabel('$L_{[OIII]} \, (erg\,s^{-1})$')
plt.ylabel('$L_{x,2-10} \, (erg\,s^{-1})$')
plt.subplots_adjust(hspace=0)
ax2=plt.subplot(338,sharey=ax1)
plt.tick_params('y', labelleft=False)
plt.xlabel('$L_{mm} \, (erg\,s^{-1})$')
plt.loglog(mm,xray,'o')
plt.xticks(fontsize=14)
plt.minorticks_off()
plt.errorbar(mm,xray,xerr=mmerr,yerr=xrayerr,fmt='None',ecolor='k',zorder=0)
ax3=plt.subplot(339,sharey=ax1)
plt.tick_params('y', labelleft=False)
plt.subplots_adjust(wspace=0)
plt.semilogy(radio,xray,'o')
plt.xticks([-1,0,1,2,3],fontsize=14)
plt.minorticks_off()
plt.errorbar(radio,xray,xerr=radioerr,yerr=xrayerr,fmt='None',ecolor='k',zorder=0)
plt.xlabel(r'$\rm log_{10}\left(\frac{L_{\rm 1.4 \, GHz}}{L_{\rm 1.4 \, GHz\, , \,SF}}\right)$')
ax4=plt.subplot(334,sharex=ax1)
plt.tick_params('x', labelbottom=False)
plt.semilogx(OIII,radio,'o')
plt.yticks(fontsize=14)
plt.minorticks_off()
plt.errorbar(OIII,radio,xerr=OIIIerr,yerr=radioerr,fmt='None',ecolor='k',zorder=0)
plt.ylabel(r'$\rm log_{10}\left(\frac{L_{\rm 1.4 \, GHz}}{L_{\rm 1.4 \, GHz\, , \,SF}}\right)$')
ax5=plt.subplot(335,sharex=ax2,sharey=ax4)
plt.tick_params('x',labelbottom=False)
plt.tick_params('y',labelleft=False)
plt.semilogx(mm,radio,'o')
plt.errorbar(mm,radio,xerr=mmerr,yerr=radioerr,fmt='None',ecolor='k',zorder=0)
plt.minorticks_off()
ax6=plt.subplot(331,sharex=ax1)
plt.tick_params('x',labelbottom=False)
plt.loglog(OIII,mm,'o')
plt.yticks(fontsize=14)
plt.minorticks_off()
plt.errorbar(OIII,mm,xerr=OIIIerr,yerr=mmerr,fmt='None',ecolor='k',zorder=0)
plt.ylabel('$L_{mm} \, (erg\,s^{-1})$')

plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/Paper_Plots/Emission_correlation.pdf',bbox_inches='tight')

em=['Excess Radio Log','mm Luminosity (erg/s)','X-ray Luminosity (ergs/s)','OIII Luminosity (erg/s)']

mm_x=data[[em[1],em[2]]]
mm_xn=mm_x.dropna()
mm_xc=stats.spearmanr(mm_xn[em[1]],mm_xn[em[2]])
print(mm_xc)

mm_r=data[[em[1],em[0]]]
mm_rn=mm_r.dropna()
mm_rnn=mm_rn[mm_rn[em[0]]>0]
mm_rc=stats.spearmanr(mm_rnn[em[1]],mm_rnn[em[0]])
print(mm_rc)

r_x=data[[em[0],em[2]]]
r_xn=r_x.dropna()
r_xnn=r_xn[r_xn[em[0]]>0]
r_xc=stats.spearmanr(r_xnn[em[0]],r_xnn[em[2]])
print(r_xc)

o_x=data[[em[3],em[2]]]
o_xn=o_x.dropna()
o_xc=stats.spearmanr(o_xn[em[3]],o_xn[em[2]])
print(o_xc)

o_r=data[[em[3],em[0]]]
o_rn=o_r.dropna()
o_rnn=o_rn[o_rn[em[0]]>0]
o_rc=stats.spearmanr(o_rnn[em[3]],o_rnn[em[0]])
print(o_rc)

o_mm=data[[em[3],em[1]]]
o_mmn=o_mm.dropna()
o_mmc=stats.spearmanr(o_mmn[em[3]],o_mmn[em[1]])
print(o_mmc)

