import numpy as np
import pandas as pd
import math

data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')

FRL49=data[data['Galaxy']=='FRL49']

mmflux=FRL49['1mm flux density (Jy)']
mmfreq=FRL49['1mm frequency (Hz)']
dist=FRL49['Distance (Mpc)']
SI=FRL49['Spectral Index']
z=0.02

BASSL=((230e9*4*math.pi*(dist*3.086e24)**2)/((1+z)**(1+SI)))*(230e9/mmfreq)**SI*(1e-23*mmflux)

myLum=1e-23*mmflux*4*math.pi*(dist*3.086e24)**2*mmfreq

print(BASSL)
print(myLum)
