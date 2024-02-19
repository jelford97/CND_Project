from regex import F
from scipy.optimize import fsolve
import numpy as np
import pandas as pd

GB=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/GBData.csv')
Lx=10**GB['X-ray Luminosity']/3.846e33

#Lbol=[]
#for i in range(len(Lx)):
    #X=Lx[i]
    #def func(L):
        #1.54+0.24*(np.log10(L)-12)+0.0012*(np.log10(L)-12)**2-0.0015*(np.log10(L)-12)**3-np.log10(L/X)
    #Lb=fsolve(func,1e35)
    #Lbol.append(Lb)
#print(Lbol)

Lbol=[]
for i in range(len(Lx)):
    X=Lx[i]
    #print(X)
    f=lambda L: 1.54+0.24*(np.log10(L)-12)+0.012*(np.log10(L)-12)**2-0.0015*(np.log10(L)-12)**3-np.log10(L/X)
    Lb=fsolve(f,1e5)
    Lbol.append(Lb)

Lbol_erg=np.round(np.array(Lbol)*3.846e33,2)

GB['Lbol']=Lbol_erg

GB.to_csv('/Users/jelford/Documents/Phd_Work/CND_Project/CSV_Files/GBData.csv',index=False)