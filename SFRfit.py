import numpy as np
import pandas as pd
import math

python=pd.read_csv('Documents/Python.csv')

SFR100=python['Mass 100pc']/2e9
SFR75=python['Mass 75pc']/2e9
SFR50=python['Mass 50pc']/2e9

def radio_flux(SFR,Te,fr,dist):
    radiolum=(SFR/1e-27)*(2.18*(Te/1e4)**0.45*(fr/1e9)**(-0.1)+15.1*(fr/1e9)**-0.8)
    d=dist*3.086e24
    radio=radiolum/(4*math.pi*(d)**2)
    radioflux=radio/1e-23
    return radioflux

radioflux100=radio_flux(SFR100,1e4,1.4e9,python['Distance (Mpc)'])
radioflux75=radio_flux(SFR75,1e4,1.4e9,python['Distance (Mpc)'])
radioflux50=radio_flux(SFR50,1e4,1.4e9,python['Distance (Mpc)'])

python['Radio 100']=radioflux100
python['Radio 75']=radioflux75
python['Radio 50']=radioflux50

radio100=python[['Radio 100','Mass 100pc']]
radio75=python[['Radio 75','Mass 75pc']]
radio50=python[['Radio 50','Mass 50pc']]

radio100n=radio100.dropna()
radio75n=radio75.dropna()
radio50n=radio50.dropna()

print(np.polyfit(np.log10(radio100n['Mass 100pc']),np.log10(radio100n['Radio 100']),1))
print(np.polyfit(np.log10(radio75n['Mass 75pc']),np.log10(radio75n['Radio 75']),1))
print(np.polyfit(np.log10(radio50n['Mass 50pc']),np.log10(radio50n['Radio 50']),1))

