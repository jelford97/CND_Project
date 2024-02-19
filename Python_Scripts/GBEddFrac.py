import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

GBdata=pd.read_csv('/Users/jelford/Documents/Phd_Work/CND_Project/CSV_Files/GBData.csv')

GBLbol=GBdata['Lbol']
MBH=10**GBdata['MBH']

Eddlum=1.26e38*MBH

Eddfrac=GBLbol/Eddlum

GBdata['Eddington Fraction']=Eddfrac
print(Eddfrac)
GBdata.to_csv('/Users/jelford/Documents/Phd_Work/CND_Project/CSV_Files/GBData.csv')

#plt.hist(np.log10(GBLbol))
#plt.show()
#plt.close()

#plt.hist(np.log10(MBH))
#plt.show()
#plt.close()

#plt.hist(np.log10(Eddfrac))
#plt.show()
#plt.close()