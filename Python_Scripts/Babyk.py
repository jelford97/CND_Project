import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Babyk.csv')

def jet_power(Di,radio):
    dist=Di*3.086e24
    H0=70
    c=3e5
    z=(H0*Di)/c
    v0=1.4e9
    alph=0.8
    rpower=4*math.pi*(dist**2)*((1+z)**(alph-1))*radio*v0
    logpower=0.75*np.log10(rpower/1e40)+1.91
    jpower=10**(logpower)
    power=jpower*1e42
    return power

D=data['Distance (Mpc)']
RFJ=data['1.4 GHz Flux']*1e-3
RF=RFJ*1e-23

JP=jet_power(D,RF)
data['Jet Power']=np.round(JP,2)
data.to_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Babyk.csv')
#print(np.sort(JP))
#plt.hist(np.log10(JP))
#plt.show()