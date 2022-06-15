import numpy as np
import pandas as pd
import math

data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')

RF=data['Radio Flux (Jy)']
SFRF=data['Total Radio Flux SFR']
D=data['Distance (Mpc)']*3.086e24
TM=data['Total Mass']
SFR=data['Star Formation Rate']

dRF=RF-SFRF
dRFF=dRF*1e-23
dRFE=dRFF*(4*math.pi*(D)**2)

K=2.18*((1e4/1e4)**0.45)*((1.4e9/1e9)**-0.1)+(15.1*((1.4e9/1e9)**-0.8))
dSFR=1e-27*(1/K)*dRFE

#print(dSFR/SFR)

dTde=2e9*(dSFR/SFR)

print(dTde/2e9)
