import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')

RadioSFR=data['Total Radio Flux SFR']*1e-23
RadioLum=data['Radio Luminosity (L_solar)']*3.826e33
D=data['Distance (Mpc)']*3.086e24
Mass100=data['Mass 100pc']
Mass75=data['Mass 75pc']
Mass50=data['Mass 50pc']
TotMass=data['Total Mass']
TotMasserr=data['Total Mass Error']
Tdep=2e9
Tdeperr=1e9
RadioLumErr=data['Radio Luminosity Error (L_solar)']*3.826e33

SFRLum=4*math.pi*((D)**2)*RadioSFR*1.4e9

SFR=TotMass/Tdep

SFRerr=SFR*np.sqrt((TotMasserr/TotMass)**2+(Tdeperr/Tdep)**2)


#print(RadioLum)
#print(SFRLum)
ExRadio=(RadioLum-SFRLum)/1e35
#print(ExRadio)

dSFRL=SFRLum*(SFRerr/SFR)

dExRadio=(np.sqrt((RadioLumErr**2)+(dSFRL**2)))/1e35


plt.loglog(Mass50,ExRadio,'o')
plt.yscale('symlog')
plt.errorbar(Mass50,ExRadio,yerr=dExRadio,ecolor='black',fmt='none',zorder=1)
plt.xlabel('MH2_Mass 50pc M_Solar')
plt.ylabel('Excess 1.4GHz Flux (10^35 ergs/s)')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/Excess_Radio_50pc.png',bbox_inches='tight')
plt.close()


