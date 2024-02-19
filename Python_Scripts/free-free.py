import numpy as np
import pandas as pd
import math

data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')
mmflux=data['1mm flux density (Jy)']
mmfreq=data['1mm frequency (Hz)']
dist=data['Distance (Mpc)']
beammass=data['Mass beam width']
tdep=2e9
beamsfr=beammass/tdep

FFLH=beamsfr/(4.6e-28*((1e4/1e4)**-0.45)*(mmfreq/1e9)**0.1)
FFL=FFLH*mmfreq

mmL=1e-23*4*math.pi*(dist*3.026e24)**2*mmfreq*mmflux

FFper=(FFL/mmL)*100

print(np.sort(FFper))
