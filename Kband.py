import pandas as pd
import numpy as np
import math 

data=pd.read_csv('Python.csv')
Kband=data['Kband Flux']
Dist=data['Distance (Mpc)']
Xray=data['X-ray Luminosity (ergs/s)']

KbandLum=(1e-23*4*math.pi*Kband*(Dist*3.086e24)**2*1.38e14)/3.826e33

#print(KbandLum)

LXBLum=(3.3e27*KbandLum)

Ratio=(LXBLum/Xray)*100

print(Ratio)
