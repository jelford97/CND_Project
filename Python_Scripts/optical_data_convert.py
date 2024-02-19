import numpy as np
import pandas as pd

data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Optical_data.csv')

Galaxies=data['Galaxy']
Dist=data['Distance (Mpc)']

OIIIUnits=data['OIII Units']
OIIIValue=data['OIII Value']

NIIUnits=data['NII Units']
NIIValue=data['NII Value']

HbetaUnits=data['Hbeta Units']
HbetaValue=data['Hbeta Value']

HalphaUnits=data['Halpha Units']
HalphaValue=data['Halpha Value']

OIIILum=[]
for i in range(len(Galaxies)):
    if OIIIUnits[i]=='e-20 W/m^2':
        OIII=OIIIValue[i]*1e-20
        OIIIerg=OIII*1e7
        OIIIergLum=OIIIerg*4*np.pi*(Dist[i]*3.086e22)**2
        OIIILum.append(np.log10(OIIIergLum))
    if OIIIUnits[i]=='log (erg/s)':
        OIIILum.append(OIIIValue[i])
    if OIIIUnits[i]=='None':
        OIIILum.append(np.NaN)

NIILum=[]
for j in range(len(Galaxies)):
    if NIIUnits[j]=='e-20 W/m^2':
        NII=NIIValue[j]*1e-20
        NIIerg=NII*1e7
        NIIergLum=NIIerg*4*np.pi*(Dist[j]*3.086e22)**2
        NIILum.append(np.log10(NIIergLum))
    if NIIUnits[j]=='e-15 erg/s/cm^2':
        NII=NIIValue[j]*1e-15
        NIIergLum=NII*4*np.pi*(Dist[j]*3.086e24)**2
        NIILum.append(np.log10(NIIergLum))
    if NIIUnits[j]=='None':
        NIILum.append(np.NaN)

HbetaLum=[]
for k in range(len(Galaxies)):
    if HbetaUnits[k]=='e-20 W/m^2':
        Hbeta=HbetaValue[k]*1e-20
        Hbetaerg=Hbeta*1e7
        HbetaergLum=Hbetaerg*4*np.pi*(Dist[k]*3.086e22)**2
        HbetaLum.append(np.log10(HbetaergLum))
    if HbetaUnits[k]=='log (erg/s)':
        HbetaLum.append(HbetaValue[k])
    if HbetaUnits[k]=='None':
        HbetaLum.append(np.NaN)

HalphaLum=[]
for l in range(len(Galaxies)):
    if HalphaUnits[l]=='e-20 W/m^2':
        Halpha=HalphaValue[l]*1e-20
        Halphaerg=Halpha*1e7
        HalphaergLum=Halphaerg*4*np.pi*(Dist[l]*3.086e22)**2
        HalphaLum.append(np.log10(HalphaergLum))
    if HalphaUnits[l]=='e-15 erg/s/cm^2':
        Halpha=HalphaValue[l]*1e-15
        HalphaergLum=Halpha*4*np.pi*(Dist[l]*3.086e24)**2
        HalphaLum.append(np.log10(HalphaergLum))
    if HalphaUnits[l]=='None':
        HalphaLum.append(np.NaN)

BPT_Data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/BPT_Data.csv')
BPT_Galaxies=BPT_Data['Galaxy']

OIIILumNL=10**(np.array(OIIILum))
NIILumNL=10**(np.array(NIILum))
HbetaLumNL=10**(np.array(HbetaLum))
HalphaLumNL=10**(np.array(HalphaLum))


OIII_Hbeta=[]
NII_Halpha=[]
for r in range(len(BPT_Galaxies)):
    if r==2:
        O_HB=-0.79
        OIII_Hbeta.append(O_HB)
        N_HA=-0.37
        NII_Halpha.append(N_HA)
    elif r==15:
        O_HB=np.log10(1.82)
        OIII_Hbeta.append(O_HB)
        N_HA=np.log10(1.12)
        NII_Halpha.append(N_HA)
    elif r==19:
        O_HB=0.39
        OIII_Hbeta.append(O_HB)
        N_HA=0.41
        NII_Halpha.append(N_HA)
    else:
        O_HB=OIIILumNL[r]/HbetaLumNL[r]
        OIII_Hbeta.append(np.log10(O_HB))
        N_HA=NIILumNL[r]/HalphaLumNL[r]
        NII_Halpha.append(np.log10(N_HA))


BPT_Data['log(OIII/H_beta)']=OIII_Hbeta
BPT_Data['log(NII/H_alpha)']=NII_Halpha

BPT_Data.to_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/BPT_Data.csv',index=False)
