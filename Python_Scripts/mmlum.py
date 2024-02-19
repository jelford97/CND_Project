import pandas as pd
import numpy as np
import math

data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')
mmflux=data['1mm flux density (Jy)']
mmfreq=data['1mm frequency (Hz)']
dist=data['Distance (Mpc)']
rms=data['RMS']
mmcgs=mmflux*1e-23

mmlum=mmcgs*mmfreq*(dist*3.086e24)**2*4*math.pi
mmlumerr=mmlum*(rms/mmflux)

data['mm Luminosity (erg/s)']=mmlum
data['mm Luminosity Uncertainty (erg/s)']=mmlumerr

data.to_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv',index=False)
