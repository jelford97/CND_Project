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

SFRLum=4*math.pi*((D)**2)*RadioSFR*1.4e9

#print(RadioLum)
#print(SFRLum)
ExRadio=RadioLum-SFRLum
#print(ExRadio)

plt.loglog(Mass100,ExRadio,'o')
#plt.yscale('symlog')
plt.xlabel('MH2_Mass 100pc M_Solar')
plt.ylabel('Excess 1.4GHz Flux (ergs/s)')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/Excess_Radio_100pc.png',bbox_inches='tight')
plt.close()


