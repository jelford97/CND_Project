import numpy as np
import pandas as pd

python=pd.read_csv('Documents/Python.csv')

def mmflux(v,d,T,v0,b,M):
    D=d*3.086e22
    m=M*2e30
    c=3e8
    h=6.626e-34
    kb=1.38e-23
    k0=0.051
    k=k0*(v/v0)**b
    B=(2*h*v**3/c**2)*(1/(np.exp(h*v/(kb*T))-1))
    S=k*m*B/D**2
    sj=S/1e-26
    return sj

gtod=[100,50,200]
i=2
dust100=python['Mass 100pc']/gtod[i]
dust75=python['Mass 75pc']/gtod[i]
dust50=python['Mass 50pc']/gtod[i]

mmflux100=mmflux(3e11,python['Distance (Mpc)'],30,6e11,2,dust100)
mmflux75=mmflux(3e11,python['Distance (Mpc)'],30,6e11,2,dust75)
mmflux50=mmflux(3e11,python['Distance (Mpc)'],30,6e11,2,dust50)

python['mm flux 100']=mmflux100
python['mm flux 75']=mmflux75
python['mm flux 50']=mmflux50

mm100=python[['Mass 100pc','mm flux 100']]
mm75=python[['Mass 75pc','mm flux 75']]
mm50=python[['Mass 50pc','mm flux 50']]

mm100n=mm100.dropna()
mm75n=mm75.dropna()
mm50n=mm50.dropna()

print(np.polyfit(np.log10(mm100n['Mass 100pc']),np.log10(mm100n['mm flux 100']),1))
print(np.polyfit(np.log10(mm75n['Mass 75pc']),np.log10(mm75n['mm flux 75']),1))
print(np.polyfit(np.log10(mm50n['Mass 50pc']),np.log10(mm50n['mm flux 50']),1))

