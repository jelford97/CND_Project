import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')

D=data['Distance (Mpc)']
Fr=1.4e9
Telc=1e4


# In[4]:
jet=data[data['Radio Jet']=='Yes']
nonjet=data[data['Radio Jet']=='No']

jetSFRtot=jet['Total Mass']/2e9
nonjetSFRtot=nonjet['Total Mass']/2e9

def radio_flux(SFR,Te,fr):
    radiolum=(SFR/1e-27)*(2.18*(Te/1e4)**0.45*(fr/1e9)**(-0.1)+15.1*(fr/1e9)**-0.8)
    #d=dist*3.086e24
    radio=radiolum*fr
    return radio

jettotrL=radio_flux(jetSFRtot,Telc,Fr)
nonjetL=radio_flux(nonjetSFRtot,Telc,Fr)

jetradiolum=jet['Radio Luminosity (L_solar)']*3.826e33
nonjetradiolum=nonjet['Radio Luminosity (L_solar)']*3.826e33

x=np.logspace(30,40,100)
y=x

plt.loglog(jettotrL,jetradiolum,'o',color='red')
plt.loglog(nonjetL,nonjetradiolum,'o',color='blue')
plt.loglog(x,y,color='black',linestyle='--')
plt.xlabel('Radio Luminosity from SFR (erg/s)')
plt.ylabel('Osberved Radio Luminosity')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/Radio Flux SFRJetTdep.png',bbox_inches='tight')
