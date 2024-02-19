import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')

RadioL=data['Radio Luminosity (L_solar)']*3.826e33
RadioLum=RadioL/1.4e9
TotMass=data['Total Mass']

def SFR_function(Radio,Te,fr):
	K=2.18*((Te/1e4)**0.45)*((fr/1e9)**(-0.1))+15.1*((fr/1e9)**(-0.8))
	SFR=1e-27*(1/K)*Radio
	return SFR

SFR=SFR_function(RadioLum,1e4,1.4e9)
tdep=TotMass/SFR
#print(tdep/1e9)
tdepS=np.sort(tdep)
tdepN=tdepS[0:24]
#print(tdepN)

plt.hist(tdepN/1e9)
plt.xlabel('Depletion Time (Gyrs)')
plt.ylabel('Count')
#plt.xlim(0,3)
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/Depletion_time.png',bbox_inches='tight')
plt.close()

