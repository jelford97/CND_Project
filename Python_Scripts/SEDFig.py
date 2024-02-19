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

def power_law(a,p,K):
    B=(K*(a/1e10)**p)
    return B

def mod_black_body(M,T,v,v0,D,b):
    d=D*3.0856e22
    m=M*2e30
    c=3e8
    h=6.626e-34
    kb=1.38e-23
    B=((2*h*v**3/c**2)*1/(np.exp(h*v/(kb*T))))
    k0=0.051
    k=k0*((v/v0)**b)
    S=(k*B*m/(d**2))
    sj=S/1e-26
    return sj

def combined(p,K,M,T,v,v0,D,b):
    com=power_law(v,p,K)+mod_black_body(M,T,v,v0,D,b)
    return com

def figure(p,k,M,T,D,b,LSB,LSBfr,USB,USBfr,SEDfl,SEDfr,x0,y0,h,w,SEDerror,LSBerr,USBerr):
    fig,axs=plt.subplots(3,1,sharex=True)
    fig.subplots_adjust(hspace=0)
    fig.set_figheight(15)
    fig.set_figwidth(10)
    
    rfreq=np.logspace(7,12,100)
    dfreq=np.logspace(10,13,100)
    ffreq=np.logspace(7,13,100)
    pl=[]
    dust=[]
    com=[]
    for i in range(0,3):
        pwr=power_law(rfreq,p[i],k[i])
        dst=mod_black_body(M[i],T[i],dfreq,6e11,D[i],b[i])
        cm=combined(p[i],k[i],M[i],T[i],ffreq,6e11,D[i],b[i])
        pl.append(pwr)
        dust.append(dst)
        com.append(cm)
    
    plmjy=np.array(pl)/1e-3
    dustmjy=np.array(dust)/1e-3
    commjy=np.array(com)/1e-3
    SEDflmjy=np.array(SEDfl)/1e-3
    SEDerrmjy=np.array(SEDerror)/1e-3
    LSBmjy=np.array(LSB)/1e-3
    USBmjy=np.array(USB)/1e-3
    LSBerrmjy=np.array(LSBerr)/1e-3
    USBerrmjy=np.array(USBerr)/1e-3
    
    axs[0].loglog(dfreq/1e9,dustmjy[0],color='green',label='Modified Black Body',zorder=2)
    axs[0].loglog(rfreq/1e9,plmjy[0],color='red',label='Synchrotron',zorder=3)
    axs[0].loglog(ffreq/1e9,commjy[0],color='orchid',label='Total',zorder=4)
    LSB,=axs[0].loglog(LSBfr[0]/1e9,LSBmjy[0],'*',markersize=12,color='orange',zorder=6)
    USB,=axs[0].loglog(USBfr[0]/1e9,USBmjy[0],'*',markersize=12,color='green',zorder=7)
    axs[0].errorbar(LSBfr[0]/1e9,LSBmjy[0],yerr=LSBerrmjy[0],fmt='none',ecolor='black')
    axs[0].errorbar(USBfr[0]/1e9,USBmjy[0],yerr=USBerrmjy[0],fmt='none',ecolor='black')
    axs[0].set_ylim(5e-5)
    SED,=axs[0].loglog(SEDfr[:,0]/1e9,SEDflmjy[:,0],'o',zorder=8)
    axs[0].errorbar(SEDfr[:,0]/1e9,SEDflmjy[:,0],yerr=SEDerrmjy[:,0],fmt='none',ecolor='black')
    leg1=axs[0].legend(prop={'size':10},frameon=False,loc='lower left')
    almafl=np.array([LSBmjy[0],USBmjy[0]])
    almafr=np.array([LSBfr[0],USBfr[0]])/1e9
    axins=axs[0].inset_axes([x0[0],y0[0],h[0],w[0]])
    axins.plot(almafr,almafl,color='black')
    axins.plot(LSBfr[0]/1e9,LSBmjy[0],'*',markersize=12,color='orange')
    axins.plot(USBfr[0]/1e9,USBmjy[0],'*',markersize=12,color='green')
    axins.errorbar(LSBfr[0]/1e9,LSBmjy[0],yerr=LSBerrmjy[0],fmt='none',ecolor='black')
    axins.errorbar(USBfr[0]/1e9,USBmjy[0],yerr=USBerrmjy[0],fmt='none',ecolor='black')
    #axins.set_xlabel('GHz')
    #axins.set_ylabel('mJy')
    #axs[0].add_artist(leg1)
    axs[0].indicate_inset_zoom(axins,edgecolor='black')
    axs[0].set_ylabel('Flux density (mJy)')
    
    
    axs[1].loglog(dfreq/1e9,dustmjy[1],color='green',zorder=2)
    axs[1].loglog(rfreq/1e9,plmjy[1],color='red',zorder=3)
    axs[1].loglog(ffreq/1e9,commjy[1],color='orchid',zorder=4)
    axs[1].loglog(LSBfr[1]/1e9,LSBmjy[1],'*',markersize=12,color='orange',zorder=6)
    axs[1].loglog(USBfr[1]/1e9,USBmjy[1],'*',markersize=12,color='green',zorder=7)
    axs[1].errorbar(LSBfr[1]/1e9,LSBmjy[1],yerr=LSBerrmjy[1],fmt='none',ecolor='black')
    axs[1].errorbar(USBfr[1]/1e9,USBmjy[1],yerr=USBerrmjy[1],fmt='none',ecolor='black')
    axs[1].set_ylim(5e-5)
    axs[1].loglog(SEDfr[:,1]/1e9,SEDflmjy[:,1],'o',zorder=8)
    axs[1].errorbar(SEDfr[:,1]/1e9,SEDflmjy[:,1],yerr=SEDerrmjy[:,1],fmt='none',ecolor='black')
    axins1=axs[1].inset_axes([x0[1],y0[1],h[1],w[1]])
    almafl=[LSBmjy[1],USBmjy[1]]
    almafr=np.array([LSBfr[1],USBfr[1]])/1e9
    axins1.plot(almafr,almafl,color='black')
    axins1.plot(LSBfr[1]/1e9,LSBmjy[1],'*',markersize=12,color='orange')
    axins1.plot(USBfr[1]/1e9,USBmjy[1],'*',markersize=12,color='green')
    axins1.errorbar(LSBfr[1]/1e9,LSBmjy[1],yerr=LSBerrmjy[1],fmt='none',ecolor='black')
    axins1.errorbar(USBfr[1]/1e9,USBmjy[1],yerr=USBerrmjy[1],fmt='none',ecolor='black')
    #axins1.set_xlabel('GHz')
    #axins1.set_ylabel('mJy')
    axs[1].indicate_inset_zoom(axins1,edgecolor='black')
    axs[1].set_ylabel('Flux density (mJy)')
    
    axs[2].loglog(dfreq/1e9,dustmjy[2],color='green',zorder=2)
    axs[2].loglog(rfreq/1e9,plmjy[2],color='red',zorder=3)
    axs[2].loglog(ffreq/1e9,commjy[2],color='orchid',zorder=4)
    axs[2].loglog(LSBfr[2]/1e9,LSBmjy[2],'*',markersize=12,color='orange',zorder=6)
    axs[2].loglog(USBfr[2]/1e9,USBmjy[2],'*',markersize=12,color='green',zorder=7)
    axs[2].errorbar(LSBfr[2]/1e9,LSBmjy[2],yerr=LSBerrmjy[2],fmt='none',ecolor='black')
    axs[2].errorbar(USBfr[2]/1e9,USBmjy[2],yerr=USBerrmjy[2],fmt='none',ecolor='black')
    axs[2].set_ylim(5e-5)
    axs[2].loglog(SEDfr[:,2]/1e9,SEDflmjy[:,2],'o',zorder=8)
    axs[2].errorbar(SEDfr[:,2]/1e9,SEDflmjy[:,2],yerr=SEDerrmjy[:,2],fmt='none',ecolor='black')
    axins2=axs[2].inset_axes([x0[2],y0[2],h[2],w[2]])
    #axins3=axs[2].inset_axes([0.78,0.53,0.05,0.1])
    #axins3.set_xticks([])
    #axins3.set_yticks([])
    almafl=[LSBmjy[2],USBmjy[2]]
    almafr=np.array([LSBfr[2],USBfr[2]])/1e9
    axins2.plot(almafr,almafl,color='black')
    axins2.plot(LSBfr[2]/1e9,LSBmjy[2],'*',markersize=12,color='orange')
    axins2.plot(USBfr[2]/1e9,USBmjy[2],'*',markersize=12,color='green')
    axins2.errorbar(LSBfr[2]/1e9,LSBmjy[2],yerr=LSBerrmjy[2],fmt='none',ecolor='black')
    axins2.errorbar(USBfr[2]/1e9,USBmjy[2],yerr=USBerrmjy[2],fmt='none',ecolor='black')
    leg2=axs[2].legend([USB,LSB,SED],['LSB (nuclear: not fitted)','USB (nuclear: not fitted)','Archival data (entire galaxy)'],prop={'size':10},frameon=False,loc='lower right')
    #axins2.set_xlabel('GHz')
    #axins2.set_ylabel('mJy')
    axs[2].indicate_inset_zoom(axins2,edgecolor='black')
    axs[2].set_ylabel('Flux density (mJy)')
    axs[2].set_xlabel('Frequency (GHz)')
    plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/ThermalSED.pdf',bbox_inches='tight')

data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/SED.csv')
plot=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Plot.csv')

i=3
j=5
k=9
index=np.array(plot['Index'])
inter=np.array(plot['Intercept'])
mass=np.array(plot['Mass'])
temp=np.array(plot['Temp'])
dist=np.array(plot['Distance'])
beta=np.array(plot['Beta'])
c=3e5
H0=70
z=(dist[i]/c)*H0
LSBfl=np.array(plot['LSB Flux'])
LSBfr=np.array(plot['LSB Freq'])
LSBfre=(1+z)*LSBfr
LSBerr=np.array(plot['LSB RMS'])
USBfl=np.array(plot['USB Flux'])
USBfr=np.array(plot['USB Freq'])
USBfre=(1+z)*USBfr
USBerr=np.array(plot['USB RMS'])
SEDflux=plot['SED Flux']
SEDfreq=plot['SED Freq']
SEDerr=np.array(plot['SED RMS'])
SEDdate=plot['SED Date']
LL=plot['LL']
SEDy=np.array(data[SEDflux[[i,j,k]]])
SEDx=np.array(data[SEDfreq[[i,j,k]]])
SEDxe=(1+z)*SEDx
SEDrms=np.array(data[SEDerr[[i,j,k]]])
#SEDyr=data[SEDdate[i]]
x0=np.array(plot['x0'])
y0=np.array(plot['y0'])
h=np.array(plot['h'])
w=np.array(plot['w'])
mm=np.array(plot['1mm flux density (Jy)'])
mmfr=np.array(plot['1mm frequency (Hz)'])
mmfre=(1+z)*mmfr
mmrms=np.array(plot['RMS'])
mcmc=plot['MCMC']
#model=pd.read_csv(mcmc[i], header=None)
#logLH=pd.read_csv(LL[i],header=None)
ffind=plot['FF Index']
ffint=plot['FF Intercept']
ffmass=plot['FF Mass']
fftemp=plot['FF Temp']
ffbeta=plot['FF Beta']
sfr=plot['SFR']

Fig=figure(index[[i,j,k]],inter[[i,j,k]],mass[[i,j,k]],temp[[i,j,k]],dist[[i,j,k]],beta[[i,j,k]],LSBfl[[i,j,k]],LSBfre[[i,j,k]],USBfl[[i,j,k]],USBfre[[i,j,k]],SEDy,SEDxe,x0[[i,j,k]],y0[[i,j,k]],h[[i,j,k]],w[[i,j,k]],SEDrms,LSBerr[[i,j,k]],USBerr[[i,j,k]])
