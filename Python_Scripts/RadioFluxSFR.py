#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


# In[2]:


data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')


# In[3]:


D=data['Distance (Mpc)']
Fr=1.4e9
Telc=1e4


# In[4]:
jet=data[data['Radio Jet']=='Yes']
nonjet=data[data['Radio Jet']=='No']

jetSFRtot=10**(jet['Tim SFR Log'])
nonjetSFRtot=10**(nonjet['Tim SFR Log'])
#SFRtoterr=2.303*SFRtot*data['Tim SFR Error']

# In[5]:


def radio_flux(SFR,Te,fr):
    radiolum=(SFR/1e-27)*(2.18*(Te/1e4)**0.45*(fr/1e9)**(-0.1)+15.1*(fr/1e9)**-0.8)
    #d=dist*3.086e24
    radio=radiolum*fr
    return radio


# In[6]:


jettotrL=radio_flux(jetSFRtot,Telc,Fr)
nonjetL=radio_flux(nonjetSFRtot,Telc,Fr)
#totrLErr=(SFRtoterr/SFRtot)*totrL

# In[7]:


#data['Radio Luminosity (SFR)']=totrL
#data.to_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv',index=False)

jetradiolum=jet['Radio Luminosity (L_solar)']*3.826e33
nonjetradiolum=nonjet['Radio Luminosity (L_solar)']*3.826e33
#ExRadio=radiolum-totrL
#radiolumerr=(data['Radio Luminosity Error (L_solar)'])*3.826e33
#ExRadioerror=ExRadio*np.sqrt(((radiolumerr/radiolum)**2)+((totrLErr/totrL)**2))
# In[8]:


x=np.logspace(30,40,100)
y=x


# In[9]:


plt.loglog(jettotrL,jetradiolum,'o',color='red')
plt.loglog(nonjetL,nonjetradiolum,'o',color='blue')
plt.loglog(x,y,color='black',linestyle='--')
#plt.errorbar(data['Radio Luminosity (SFR)'],ExRadio/1e35,yerr=ExRadioerror/1e35,fmt='None',ecolor='black',zorder=0)
#plt.yscale('symlog')
plt.xlabel('Radio Luminosity from SFR (erg/s)')
plt.ylabel('Osberved Radio Luminosity')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/Excess Radio Flux SFRJet.png',bbox_inches='tight')



#print(data['Radio Flux (Jy)']/data['Total Radio Flux SFR'])









