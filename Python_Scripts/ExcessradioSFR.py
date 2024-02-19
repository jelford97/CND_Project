import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def radio_flux(SFR,Te,fr):
    radiolum=(SFR/1e-27)*(2.18*(Te/1e4)**0.45*(fr/1e9)**(-0.1)+15.1*(fr/1e9)**-0.8)
    #d=dist*3.086e24
    radio=radiolum*fr
    return radio

data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')
SFR=10**(data['Tim SFR Log'])
SFRerr=2.303*SFR*data['Tim SFR Error']

radiolum=radio_flux(SFR,1e4,1.4e9)
radiolumerr=(SFRerr/SFR)*radiolum

obsradio=data['Radio Luminosity (L_solar)']*3.826e33
obsraderr=data['Radio Luminosity Error (L_solar)']*3.826e33

exradio=np.log10(obsradio)-np.log10(radiolum)
exradioerg=obsradio-radiolum
data['Excess Radio (erg/s)']=exradioerg
data['Excess Radio Log']=exradio

logobsraderr=0.434*(obsraderr/obsradio)
logSFRraderr=0.434*(radiolumerr/radiolum)

exraderr=np.sqrt((logobsraderr)**2+(logSFRraderr)**2)
data['Excess Radio Log Error']=exraderr

data.to_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv', index=False)
Mass100=data['Mass 100pc']
plt.semilogx(Mass100,exradio,'o')
plt.xlabel('Mass 100pc')
plt.ylabel('Excess radio (erg/s)')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/Exradio100pcapp.png')
