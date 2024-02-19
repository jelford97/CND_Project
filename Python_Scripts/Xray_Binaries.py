import pandas as pd
import numpy as np
import math 
import matplotlib.pyplot as plt

data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')

NoBiData=data[data['Bi Sample']=='No']

Kband=NoBiData['Kband Mag']
Dist=NoBiData['Distance (Mpc)']
Xray=NoBiData['X-ray Luminosity (ergs/s)']


print(len(NoBiData['Galaxy']))

def KbandLum(Kband, Dist):
        KbandAbs=Kband-5*np.log10(Dist*1e6)+5
        KbandLum=10**(0.4*(4.85-KbandAbs))
        return KbandLum

KbandL=KbandLum(Kband,Dist)

KbandList=np.logspace(8,13,100)
LXBLum=0.2e30*KbandList
LXBLumB=1e29*KbandList

LXBpred=0.2e30*KbandL
LXBCont=(LXBpred/Xray)*100
print(LXBCont)
#plt.loglog(KbandL,Xray,'o')
#plt.plot(KbandList,LXBLum,label='KF04')
#plt.plot(KbandList,LXBLumB,label='B11')
#plt.xlabel('Lk')
#plt.ylabel('Lx')
#plt.legend()
#plt.show()

SFR=10**NoBiData['Tim SFR Log']

HMXBpred=SFR*6.7e39

HMXBCont=(HMXBpred/Xray)*100
print(HMXBCont)
#SFRList=np.logspace(-5,5,100)

#HMXBLum=SFRList*6.7e39

#plt.loglog(SFR,Xray,'o')
#plt.plot(SFRList,HMXBLum)
#plt.xlabel('SFR')
#plt.ylabel('Lx')
#plt.show()