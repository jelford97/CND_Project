import pandas as pd
import numpy as np
import math

data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')
RF=data['Radio Flux (Jy)']
RFcgs=RF*1e-23
dist=data['Distance (Mpc)']*3.086e24
freq=1.4e9

RL=4*math.pi*freq*RFcgs*dist**2
#print(RL)

data['New RL']=RL
print(data[['New RL','Radio Luminosity (erg/s)']])