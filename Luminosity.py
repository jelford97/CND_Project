import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.stats as stats

data=pd.read_csv('Python.csv')
GBData=pd.read_csv('GBData.csv')
GB200=GBData['SD 200pc']
GB50=GBData['SD 50pc']
GBXraydata=GBData['X-ray Luminosity']

GBSD200=10**(GB200)
GBSD50=10**(GB50)
GBXray=10**(GBXraydata)

GBSDratio=np.log10(GBSD50/GBSD200)

RadioLum=data['Radio Luminosity (erg/s)']
Xraylum=data['X-ray Luminosity (ergs/s)']
sd200pc=data['Mass 200pc']/(math.pi*200**2)
sd50pc=data['Mass 50pc']/(math.pi*50**2)
sdratio=np.log10(sd50pc/sd200pc)
data['Surface Density Ratio']=sdratio

plt.semilogx(RadioLum,sdratio,'o')
#plt.yscale('log')
plt.xlabel('log 1.4 GHz Luminosity (erg/s)')
plt.ylabel('log(SD_50pc/SD_200pc)')
plt.savefig('RadioLumMass.png',bbox_inches='tight')
plt.close()


plt.semilogx(Xraylum,sdratio,'o',color='blue',label='WISDOM')
plt.semilogx(GBXray,GBSDratio,'o',color='red',label='Garcia-Burillo')
#plt.yscale('log')
plt.xlabel('log (2-10) keV X-ray Luminosity (erg/s)')
plt.ylabel('log(SD_50pc/SD_200pc)')
plt.legend()
plt.savefig('XrayLumMass.png',bbox_inches='tight')
plt.close()

Xrayrankdata=data[['Surface Density Ratio','X-ray Luminosity (ergs/s)']]
Radiorankdata=data[['Surface Density Ratio','Radio Luminosity (erg/s)']]

Xrayrankdrop=Xrayrankdata.dropna()
Radiorankdrop=Radiorankdata.dropna()

Xraystat=stats.spearmanr(Xrayrankdrop['X-ray Luminosity (ergs/s)'],Xrayrankdrop['Surface Density Ratio'])
Radiostat=stats.spearmanr(Radiorankdrop['Radio Luminosity (erg/s)'],Radiorankdrop['Surface Density Ratio'])

print(Xraystat)
print(Radiostat)
