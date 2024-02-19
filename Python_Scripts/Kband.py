import pandas as pd
import numpy as np
import math 
import matplotlib.pyplot as plt

data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')
Chandra=data[data['X-ray Telescope']=='Chandra']
XMM=data[data['X-ray Telescope']=='XMM']
ROSAT=data[data['X-ray Telescope']=='ROSAT']
ASCA=data[data['X-ray Telescope']=='ASCA']
Einstein=data[data['X-ray Telescope']=='Einstein']

CKband=Chandra['Kband Mag']
CDist=Chandra['Distance (Mpc)']
CXray=Chandra['X-ray Luminosity (ergs/s)']

XKband=XMM['Kband Mag']
XDist=XMM['Distance (Mpc)']
XXray=XMM['X-ray Luminosity (ergs/s)']

RKband=ROSAT['Kband Mag']
RDist=ROSAT['Distance (Mpc)']
RXray=ROSAT['X-ray Luminosity (ergs/s)']

AKband=ASCA['Kband Mag']
ADist=ASCA['Distance (Mpc)']
AXray=ASCA['X-ray Luminosity (ergs/s)']

EKband=Einstein['Kband Mag']
EDist=Einstein['Distance (Mpc)']
EXray=Einstein['X-ray Luminosity (ergs/s)']

KbandList=np.logspace(8,13,100)
LXBLumList=0.2e30*KbandList
LXBSpiral1=5.4e27*KbandList
LXBSpiral2=6.8e28*KbandList

def KbandLum(Kband, Dist):
        KbandAbs=Kband-5*np.log10(Dist*1e6)+5
        KbandLum=10**(0.4*(4.85-KbandAbs))
        return KbandLum
CKbandLum=KbandLum(CKband,CDist)
XKbandLum=KbandLum(XKband,XDist)
RKbandLum=KbandLum(RKband,RDist)
AKbandLum=KbandLum(AKband,ADist)
EKbandLum=KbandLum(EKband,EDist)
#Ratio=(LXBLum/Xray)*100

#for a,b,c in zip(np.log10(LXBLum),np.log10(Xray),Ratio):
	#print(a,b,c)

plt.loglog(CKbandLum,CXray,'o',label='Chandra')
plt.loglog(XKbandLum,XXray,'o',label='XMM')
plt.loglog(RKbandLum,RXray,'o',label='Rosat')
plt.loglog(AKbandLum,AXray,'o',label='ASCA')
plt.loglog(EKbandLum,EXray,'o',label='Einstein')
plt.plot(KbandList,LXBLumList,label='ETG')
plt.plot(KbandList,LXBSpiral1,label='Spiral LB')
plt.plot(KbandList,LXBSpiral2,label='Spiral UB')
plt.legend()
plt.xlabel('Lk')
plt.ylabel('Lx')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/LkvsLX.png')
plt.close()

ETG=data[data['Galaxy Type']=='ETG']
Spiral=data[data['Galaxy Type']=='Spiral']
Dwarf=data[data['Galaxy Type']=='Dwarf']

ETGKband=ETG['Kband Mag']
ETGDist=ETG['Distance (Mpc)']
ETGXray=ETG['X-ray Luminosity (ergs/s)']

SKband=Spiral['Kband Mag']
SDist=Spiral['Distance (Mpc)']
SXray=Spiral['X-ray Luminosity (ergs/s)']

DKband=Dwarf['Kband Mag']
DDist=Dwarf['Distance (Mpc)']
DXray=Dwarf['X-ray Luminosity (ergs/s)']

EKBandLum=KbandLum(ETGKband, ETGDist)
SKbandLum=KbandLum(SKband, SDist)
DKbandLum=KbandLum(DKband,DDist)

plt.loglog(EKBandLum,ETGXray,'o',label='ETG')
plt.loglog(SKbandLum,SXray,'s',label='Spiral')
plt.loglog(DKbandLum,DXray,'*',label='Dwarf')
plt.plot(KbandList,LXBLumList,label='ETG')
plt.plot(KbandList,LXBSpiral1,label='Spiral LB')
plt.plot(KbandList,LXBSpiral2,label='Spiral UB')
plt.legend()
plt.xlabel('Lk')
plt.ylabel('LX')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/LkvsLX_Galaxy_type.png')
plt.close()
