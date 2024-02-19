import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')
RadioData=data[['Radio Luminosity (L_solar)','Total Mass']]
RadioDataN=RadioData.dropna()

RadioLum=RadioDataN['Radio Luminosity (L_solar)']*3.826e33
TotMass=RadioDataN['Total Mass']
Mass=np.logspace(6,11,100)
SFR2=Mass/2e9
SFR1=Mass/1e9
SFR3=Mass/3e9
dist=data['Distance (Mpc)']

def radio_flux(SFR,Te,fr):
    radiolum=(SFR/1e-27)*(2.18*(Te/1e4)**0.45*(fr/1e9)**(-0.1)+15.1*(fr/1e9)**-0.8)
    radioL=radiolum*fr
    return radioL

RadioL2=radio_flux(SFR2,1e4,1.4e9)
RadioL1=radio_flux(SFR1,1e4,1.4e9)
RadioL3=radio_flux(SFR3,1e4,1.4e9)

S=stats.spearmanr(TotMass,RadioLum)

print(S)

plt.loglog(TotMass,RadioLum,'o')
plt.loglog(Mass,RadioL2,label='2Gyr')
plt.loglog(Mass,RadioL1,linestyle='dashed',label='1Gyr')
plt.loglog(Mass,RadioL3,linestyle='dotted',label='3Gyr')
plt.xlabel('Total Mass (L_solar)')
plt.ylabel('Global Radio Luminosity (erg/s)')
plt.legend()
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/Global_Radio_SFR.png',bbox_inches='tight')
plt.close()
