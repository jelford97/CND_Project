#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math


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


def powerlawplot(m,c,x):
    Y=m*(x-np.median(x))+c
    return Y

def dustpowerlaw(md,cd,xd):
    Yd=md*(xd)+cd
    return Yd
# In[4]:

def forward(x):
	alphaco=4.3/0.7
	return x/alphaco
def back(x):
	alphaco=4.3/0.7
	return x*alphaco

def radio_plot(data,x,y,ymax,ymin,ysfr):
    #mass=np.logspace(5,9,5)
    #alphaco=4.3/0.7
    #LCO=np.round(np.log10(mass/alphaco),1)
    fig1,axs1=plt.subplots(1,3,sharey=True)
    fig1.subplots_adjust(wspace=0)
    fig1.set_figheight(5)
    fig1.set_figwidth(15)
    SI=data['Spectral Index']
    cmap=plt.get_cmap('brg')
    cmap.set_bad('black')
    radiolum=data['Excess Radio Log']
    radiolumerr=data['Excess Radio Log Error']

    axs1[0].scatter(data['Mass 100pc'],radiolum,c='blue',plotnonfinite=True)
    axs1[0].errorbar(data['Mass 100pc'],radiolum,yerr=radiolumerr,xerr=data['Mass 100pc Error'],fmt='None',ecolor='black',zorder=0)
    axs1[0].axhline(0,0,1,color='k',linestyle='--')
    axs1[0].axhspan(-2,0,alpha=0.5,color='grey',zorder=-3)
    axs1[0].set_ylim(-2)
    axs1[0].text(10**7.5,-1,'Star-formation \ndominated')
    #axs1[0].scatter(10**izdata['log(Mdense) Msol'],izdata['Radio Flux'],marker='s',c='grey')
    #axs1[0].plot(x,10**y[0],color='orange')
    #axs1[0].fill_between(x,10**ymax[0],10**ymin[0],color='blue',alpha=0.1)
    #axs1[0].plot(x,10**ysfr[0],color='black')
    #axs1[0].set_yscale('log')
    axs1[0].set_xscale('log')
    axs1[0].set_xlabel('$M_{H_2,100pc} \, (M_{\odot})$')
    axs1[0].set_ylabel(r'$\rm log\left(\frac{L_{\rm 1.4 \, GHz}}{L_{\rm 1.4 \, GHz\,,\,SF}}\right)$')
    #secax=axs1[0].secondary_xaxis('top',functions=(forward,back))
    #secax.set_xscale('log')

    axs1[1].scatter(data['Mass 75pc'],radiolum,c='blue',plotnonfinite=True)
    axs1[1].errorbar(data['Mass 75pc'],radiolum,yerr=radiolumerr,xerr=data['Mass 75pc Error'],fmt='None',ecolor='black',zorder=0)
    axs1[1].axhline(0,0,1,color='k',linestyle='--')
    axs1[1].axhspan(-2,0,alpha=0.5,color='grey',zorder=-3)
    axs1[1].set_ylim(-2)
    axs1[1].text(10**7.4,-1,'Star-formation \ndominated')
    #axs1[1].plot(x,10**y[1],color='orange')
    #axs1[1].fill_between(x,10**ymax[1],10**ymin[1],color='blue',alpha=0.1)
    #axs1[1].plot(x,10**ysfr[1],color='black')
    #axs1[1].set_yscale('log')
    axs1[1].set_xscale('log')
    axs1[1].set_xlabel('$M_{H_2,75pc} \, (M_{\odot})$')
    
    
    im=axs1[2].scatter(data['Mass 50pc'],radiolum,c='blue',plotnonfinite=True)
    axs1[2].errorbar(data['Mass 50pc'],radiolum,yerr=radiolumerr,xerr=data['Mass 50pc Error'],fmt='None',ecolor='black',zorder=0)
    axs1[2].axhline(0,0,1,color='k',linestyle='--')
    axs1[2].axhspan(-2,0,alpha=0.5,color='grey',zorder=-3)
    axs1[2].set_ylim(-2)
    axs1[2].text(10**7,-1,'Star-formation \ndominated')
    #axs1[2].plot(x,10**y[2],color='orange')
    #axs1[2].fill_between(x,10**ymax[2],10**ymin[2],color='blue',alpha=0.1)
    #axs1[2].plot(x,10**ysfr[2],color='black')
    #axs1[2].set_yscale('log')
    axs1[2].set_xscale('log')
    axs1[2].set_xlabel('$M_{H_2,50pc} \, (M_{\odot})$')
    
    #cbar_ax=fig1.add_axes([0.25,0,0.5,0.05])
    #fig1.subplots_adjust(bottom=0.2)
    #fig1.colorbar(im,cax=cbar_ax,label='mm Spectral Index',orientation='horizontal')


# In[10]:


def mm_plot(data,x,y100,y50,y200):
    fig1,axs1=plt.subplots(1,3,sharey=True)
    fig1.subplots_adjust(wspace=0)
    fig1.set_figheight(5)
    fig1.set_figwidth(15)
    dect=data[data['Detection']=='Yes']
    nodect=data[data['Detection']=='No']
    dectmm=dect[dect['mm']=='Yes']
    dectnomm=dect[dect['mm']=='No']
    SI=dectmm['Spectral Index']
    cmap=plt.get_cmap('brg')
    cmap.set_bad('black')

    dectmmfreq=dectmm['1mm frequency (Hz)']
    dectmmdist=dectmm['Distance (Mpc)']
    dectmmflux=dectmm['1mm flux density (Jy)']
    dectmmcgs=dectmmflux*1e-23
    dectmmlum=4*math.pi*(dectmmdist*3.086e24)**2*dectmmcgs*dectmmfreq
    dectmmrms=dectmm['RMS']
    dectmmlumerr=dectmmlum*(dectmmrms/dectmmflux)
    
    dectnommfreq=dectnomm['1mm frequency (Hz)'] 
    dectnommdist=dectnomm['Distance (Mpc)']
    dectnommflux=dectnomm['1mm flux density (Jy)']
    dectnommcgs=dectnommflux*1e-23
    dectnommlum=4*math.pi*(dectnommdist*3.086e24)**2*dectnommcgs*dectnommfreq
    dectnommrms=dectnomm['RMS']
    dectnommlumerr=dectnommlum*(dectnommrms/dectnommflux)

    nodectfreq=nodect['1mm frequency (Hz)']
    nodectdist=nodect['Distance (Mpc)']
    nodectflux=nodect['1mm flux density (Jy)']
    nodectcgs=nodectflux*1e-23
    nodectlum=4*math.pi*(nodectdist*3.086e24)**2*nodectcgs*nodectfreq
    
    axs1[0].scatter(dectmm['Mass 100pc'],dectmmlum,c='blue')#,cmap=cmap,plotnonfinite=True)
    axs1[0].errorbar(dectmm['Mass 100pc'],dectmmlum,yerr=dectmmlumerr,xerr=dectmm['Mass 100pc Error'],fmt='None',ecolor='black',zorder=0)
    axs1[0].scatter(nodect['Mass 100pc'],nodectlum,marker='v',c='grey')
    #axs1[0].errorbar(nodect['Mass 100pc'],nodect['1mm flux density (Jy)'],yerr=nodect['RMS'],xerr=nodect['Mass 100pc Error'],fmt='None',ecolor='black',zorder=0)
    axs1[0].scatter(dectnomm['Mass 100pc'], dectnommlum,marker='s',c='blue')#['crimson','black'])
    axs1[0].errorbar(dectnomm['Mass 100pc'],dectnommlum,yerr=dectnommlumerr,xerr=dectnomm['Mass 100pc Error'],fmt='None',ecolor='black',zorder=0)
    axs1[0].plot(x,10**y50[0],color='blue',linestyle='dashed',label='Gas-to-dust ratio of 200')
    axs1[0].plot(x,10**y100[0],color='black',linestyle='dashed',label='Gas-to-dust ratio of 100')
    axs1[0].plot(x,10**y200[0],color='red',linestyle='dashed',label='Gas-to-dust ratio of 50')    
    leg=axs1[0].legend(prop={'size':10},frameon=False,loc='upper left')
    axs1[0].set_yscale('log')
    axs1[0].set_xscale('log')
    axs1[0].set_xlabel('$M_{H_2,100pc} \, (M_{\odot})$')
    axs1[0].set_ylabel('$L_{mm} \, (erg\,s^{-1})$')
        
    axs1[1].scatter(dectmm['Mass 75pc'],dectmmlum,c='blue')#,cmap=cmap,plotnonfinite=True)
    axs1[1].errorbar(dectmm['Mass 75pc'],dectmmlum,yerr=dectmmlumerr,xerr=dectmm['Mass 75pc Error'],fmt='None',ecolor='black',zorder=0)
    axs1[1].scatter(nodect['Mass 75pc'],nodectlum,marker='v',c='grey')
    #axs1[1].errorbar(nodect['Mass 75pc'],nodect['1mm flux density (Jy)'],yerr=nodect['RMS'],xerr=nodect['Mass 75pc Error'],fmt='None',ecolor='black',zorder=0)
    axs1[1].scatter(dectnomm['Mass 75pc'], dectnommlum,marker='s',c='blue')#['crimson','black'])
    axs1[1].errorbar(dectnomm['Mass 75pc'],dectnommlum,yerr=dectnommlumerr,xerr=dectnomm['Mass 75pc Error'],fmt='None',ecolor='black',zorder=0)
    axs1[1].plot(x,10**y100[1],color='black',linestyle='dashed')
    axs1[1].plot(x,10**y50[1],color='blue',linestyle='dashed')
    axs1[1].plot(x,10**y200[1],color='red',linestyle='dashed')    
    axs1[1].set_yscale('log')
    axs1[1].set_xscale('log')
    axs1[1].set_xlabel('$M_{H_2,75pc} \, (M_{\odot})$')   
    
    
    im=axs1[2].scatter(dectmm['Mass 50pc'],dectmmlum,c='blue')#,cmap=cmap,plotnonfinite=True)
    axs1[2].errorbar(dectmm['Mass 50pc'],dectmmlum,yerr=dectmmlumerr,xerr=dectmm['Mass 50pc Error'],fmt='None',ecolor='black',zorder=0)
    axs1[2].scatter(nodect['Mass 50pc'],nodectlum,marker='v',c='grey')
    #axs1[2].errorbar(nodect['Mass 50pc'],nodect['1mm flux density (Jy)'],yerr=nodect['RMS'],xerr=nodect['Mass 50pc Error'],fmt='None',ecolor='black',zorder=0)
    axs1[2].scatter(dectnomm['Mass 50pc'], dectnommlum,marker='s',c='blue')#'crimson','black'])
    axs1[2].errorbar(dectnomm['Mass 50pc'],dectnommlum,yerr=dectnommlumerr,xerr=dectnomm['Mass 50pc Error'],fmt='None',ecolor='black',zorder=0)
    axs1[2].plot(x,10**y100[2],color='black',linestyle='dashed')
    axs1[2].plot(x,10**y50[2],color='blue',linestyle='dashed')
    axs1[2].plot(x,10**y200[2],color='red',linestyle='dashed')    
    axs1[2].set_yscale('log')
    axs1[2].set_xscale('log')
    axs1[2].set_xlabel('$M_{H_2,50pc} \, (M_{\odot})$')
    
    #cbar_ax=fig1.add_axes([0.25,0,0.5,0.05])
    #fig1.subplots_adjust(bottom=0.2)
    #fig1.colorbar(im,cax=cbar_ax,label='mm Spectral Index',orientation='horizontal')


# In[11]:


def xray_plot(data):
    fig1,axs1=plt.subplots(1,3,sharey=True)
    fig1.subplots_adjust(wspace=0)
    fig1.set_figheight(5)
    fig1.set_figwidth(15)
    SI=data['Spectral Index']
    cmap=plt.get_cmap('brg')
    cmap.set_bad('black')
    xray=data['Adjusted X-ray Luminosity (Lsolar)']*3.846e33
    xray_err=(data['Adjusted X-ray Flux Uncertainty']/data['Adjusted X-ray Flux (Jy)'])*xray
    
    axs1[0].scatter(data['Mass 100pc'],xray,c='blue',plotnonfinite=True)
    axs1[0].errorbar(data['Mass 100pc'],xray,yerr=xray_err,xerr=data['Mass 100pc Error'],fmt='None',ecolor='black',zorder=0)
    #axs1[0].scatter(10**izdata['log(Mdense) Msol'],10**izdata['log(L(2-10) )(erg/s)'],marker='s',c='grey')
    axs1[0].set_yscale('log')
    axs1[0].set_xscale('log')
    axs1[0].set_xlabel('$M_{H_2,100pc} \, (M_{\odot})$')
    axs1[0].set_ylabel('$L_{x,2-10} \, (erg\,s^{-1})$')
    
    axs1[1].scatter(data['Mass 75pc'],xray,c='blue',plotnonfinite=True)
    axs1[1].errorbar(data['Mass 75pc'],xray,yerr=xray_err,xerr=data['Mass 75pc Error'],fmt='None',ecolor='black',zorder=0)
    axs1[1].set_yscale('log')
    axs1[1].set_xscale('log')
    axs1[1].set_xlabel('$M_{H_2,75pc} \, (M_{\odot})$')
    
    
    im=axs1[2].scatter(data['Mass 50pc'],xray,c='blue',plotnonfinite=True)
    axs1[2].errorbar(data['Mass 50pc'],xray,yerr=xray_err,xerr=data['Mass 50pc Error'],fmt='None',ecolor='black',zorder=0)
    axs1[2].set_yscale('log')
    axs1[2].set_xscale('log')
    axs1[2].set_xlabel('$M_{H_2,50pc} \, (M_{\odot})$')
    
    #cbar_ax=fig1.add_axes([0.25,0,0.5,0.05])
    #fig1.subplots_adjust(bottom=0.2)
    #fig1.colorbar(im,cax=cbar_ax,label='mm Spectral Index',orientation='horizontal')


# In[12]:


def acc_rate(data,x,y):
    fig1,axs1=plt.subplots(1,3,sharey=True)
    fig1.subplots_adjust(wspace=0)
    fig1.set_figheight(5)
    fig1.set_figwidth(15)
    SI=data['Spectral Index']
    cmap=plt.get_cmap('brg')
    cmap.set_bad('black')
    
    axs1[0].scatter(data['Mass 100pc'],data['Accretion rate (M_solar/yr)'],c='blue',plotnonfinite=True)
    axs1[0].errorbar(data['Mass 100pc'],data['Accretion rate (M_solar/yr)'],yerr=data['Accretion Rate Error'],xerr=data['Mass 100pc Error'],fmt='None',ecolor='black',zorder=0)
    #axs1[0].scatter(data['Mass 100pc']*0.1,data['Accretion rate (M_solar/yr)'],marker='*',c=SI,cmap=cmap,plotnonfinite=True)
    #axs1[0].scatter(10**izdata['log(Mdense) Msol'],10**izdata['log(Mdot) (Msol/yr)'],marker='s',c='grey')
    #axs1[0].plot(x,10**y,color='black',linestyle='dashed')
    axs1[0].set_yscale('log')
    axs1[0].set_xscale('log')
    axs1[0].set_xlabel('$M_{H_2,100pc} \, (M_{\odot})$')
    axs1[0].set_ylabel('$\dot{M}_{acc,X-ray} \, (M_{\odot}\,yr^{-1}$)')
    
    axs1[1].scatter(data['Mass 75pc'],data['Accretion rate (M_solar/yr)'],c='blue',plotnonfinite=True)
    axs1[1].errorbar(data['Mass 75pc'],data['Accretion rate (M_solar/yr)'],yerr=data['Accretion Rate Error'],xerr=data['Mass 75pc Error'],fmt='None',ecolor='black',zorder=0)
    axs1[1].set_yscale('log')
    axs1[1].set_xscale('log')
    axs1[1].set_xlabel('$M_{H_2,75pc} \, (M_{\odot})$')
    
    
    im=axs1[2].scatter(data['Mass 50pc'],data['Accretion rate (M_solar/yr)'],c='blue',plotnonfinite=True)
    axs1[2].errorbar(data['Mass 50pc'],data['Accretion rate (M_solar/yr)'],yerr=data['Accretion Rate Error'],xerr=data['Mass 50pc Error'],fmt='None',ecolor='black',zorder=0)
    axs1[2].set_yscale('log')
    axs1[2].set_xscale('log')
    axs1[2].set_xlabel('$M_{H_2,50pc} \, (M_{\odot})$') 
    
    #cbar_ax=fig1.add_axes([0.25,0,0.5,0.05])
    #fig1.subplots_adjust(bottom=0.2)
    #fig1.colorbar(im,cax=cbar_ax,label='mm Spectral Index',orientation='horizontal')


# In[8]:


data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')
#izumi=pd.read_csv('Documents/IzumiCND.csv')
#int_data=izumi[izumi['Sample']=='Int']
x=np.logspace(5,9,100)
y100=powerlawplot(1.68,37.29,np.log10(x))
y100max=powerlawplot(1.89,37.40,np.log10(x))
y100min=powerlawplot(1.47,37.18,np.log10(x))
y75=powerlawplot(1.69,37.13,np.log10(x))
y75max=powerlawplot(1.95,37.26,np.log10(x))
y75min=powerlawplot(1.43,37.00,np.log10(x))
y50=powerlawplot(1.77,37.20,np.log10(x))
y50max=powerlawplot(2.11,37.36,np.log10(x))
y50min=powerlawplot(1.43,37.04,np.log10(x))
Ysfr100=powerlawplot(0.28,-5.82,np.log10(x))
Ysfr75=powerlawplot(0.45,-7.14,np.log10(x))
Ysfr50=powerlawplot(0.42,-7.03,np.log10(x))


# In[9]:


radio_plot(data,x,[y100,y75,y50],[y100max+0.59,y75max+0.60,y50max+0.67],[y100min-0.59,y75min-0.60,y50min-0.67],[Ysfr100,Ysfr75,Ysfr50])
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/Paper_Plots/RadioPlotTest.pdf',bbox_inches='tight')
plt.close()
# In[14]:


ydust100=dustpowerlaw(1,30.79,np.log10(x))
ydust75=dustpowerlaw(1,30.79,np.log10(x))
ydust50=dustpowerlaw(1,30.79,np.log10(x))
ydust100_50=dustpowerlaw(1,31.09,np.log10(x))
ydust75_50=dustpowerlaw(1,31.09,np.log10(x))
ydust50_50=dustpowerlaw(1,31.09,np.log10(x))
ydust100_200=dustpowerlaw(1,30.49,np.log10(x))
ydust75_200=dustpowerlaw(1,30.49,np.log10(x))
ydust50_200=dustpowerlaw(1,30.49,np.log10(x))


# In[15]:


mm_plot(data,x,[ydust100,ydust75,ydust50],[ydust100_50,ydust75_50,ydust50_50],[ydust100_200,ydust75_200,ydust50_200])
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/Paper_Plots/mmDust.pdf',bbox_inches='tight')
plt.close()

# In[16]:


xray_plot(data)
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/Paper_Plots/XrayPlot.pdf',bbox_inches='tight')
plt.close()

# In[17]:


izfit=powerlawplot(1.41,-13.45,np.log10(x))


# In[18]:


acc_rate(data,x,izfit)
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/Paper_Plots/AccRate.pdf',bbox_inches='tight')
plt.close()

# In[19]:


def OIIIacc_rate(data):
    fig1,axs1=plt.subplots(1,3,sharey=True)
    fig1.subplots_adjust(wspace=0)
    fig1.set_figheight(5)
    fig1.set_figwidth(15)
    SI=data['Spectral Index']
    cmap=plt.get_cmap('brg')
    cmap.set_bad('black')
    
    axs1[0].scatter(data['Mass 100pc'],data['OIII Accretion rate'],c='blue',plotnonfinite=True)
    axs1[0].errorbar(data['Mass 100pc'],data['OIII Accretion rate'],yerr=data['OIII Accretion rate error'],xerr=data['Mass 100pc Error'],fmt='None',ecolor='black',zorder=0)
    #axs1[0].scatter(data['Mass 100pc']*0.1,data['Accretion rate (M_solar/yr)'],marker='*',c=SI,cmap=cmap,plotnonfinite=True)
    #axs1[0].scatter(10**izdata['log(Mdense) Msol'],10**izdata['log(Mdot) (Msol/yr)'],marker='s',c='grey')
    #axs1[0].plot(x,10**y,color='black',linestyle='dashed')
    axs1[0].set_yscale('log')
    axs1[0].set_xscale('log')
    axs1[0].set_xlabel('$M_{H_2,100pc} (M_{\odot})$')
    axs1[0].set_ylabel('$\dot{M}_{acc,[OIII]} \, (M_{\odot}\,yr^{-1}$)')
    
    axs1[1].scatter(data['Mass 75pc'],data['OIII Accretion rate'],c='blue',plotnonfinite=True)
    axs1[1].errorbar(data['Mass 75pc'],data['OIII Accretion rate'],yerr=data['OIII Accretion rate error'],xerr=data['Mass 75pc Error'],fmt='None',ecolor='black',zorder=0)
    axs1[1].set_yscale('log')
    axs1[1].set_xscale('log')
    axs1[1].set_xlabel('$M_{H_2,75pc} \, (M_{\odot})$')
    
    
    im=axs1[2].scatter(data['Mass 50pc'],data['OIII Accretion rate'],c='blue',plotnonfinite=True)
    axs1[2].errorbar(data['Mass 50pc'],data['OIII Accretion rate'],yerr=data['OIII Accretion rate error'],xerr=data['Mass 50pc Error'],fmt='None',ecolor='black',zorder=0)
    axs1[2].set_yscale('log')
    axs1[2].set_xscale('log')
    axs1[2].set_xlabel('$M_{H_2,50pc} \, (M_{\odot})$') 
    
    #cbar_ax=fig1.add_axes([0.25,0,0.5,0.05])
    #fig1.subplots_adjust(bottom=0.2)
    #fig1.colorbar(im,cax=cbar_ax,label='mm Spectral Index',orientation='horizontal')


# In[20]:


OIIIacc_rate(data)
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/Paper_Plots/OIIIAccRate.pdf',bbox_inches='tight')
plt.close()

# In[ ]:




