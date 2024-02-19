import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

Data=pd.read_csv('/Users/jelford/Documents/Phd_Work/CND_Project/CSV_Files/Tim_Data_New.csv')

MBH=10**(Data['log M_BH'])
Ledd=1.26e38*MBH

Lbol=Data['OIII Bolometric Luminosity (erg/s)']

Eddfrac=Lbol/Ledd

Data['Eddington Fraction']=Eddfrac
Data.to_csv('/Users/jelford/Documents/Phd_Work/CND_Project/CSV_Files/Tim_Data_New.csv')
XrayLbol=Data['X-ray Bolometric Luminosity (erg/s)']

XrayEddFrac=XrayLbol/Ledd

EddfracList=np.c_[Eddfrac,XrayEddFrac]

#print(EddfracList)

#plt.hist(np.log10(Eddfrac),fill=False, hatch='/',edgecolor='red')
#plt.show()
#plt.close()

#plt.hist(np.log10(MBH),fill=False,hatch='/',edgecolor='red')
#plt.show()
#plt.close()

#plt.hist(np.log10(Lbol),fill=False,hatch='/',edgecolor='red')
#plt.show()
#plt.close()