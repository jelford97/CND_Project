import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Iz=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/IzumiCND.csv')

Mdot=10**(Iz['log(Mdot) (Msol/yr)'])
MBH=10**(Iz['MBH'])

Lbol=(Mdot*0.1/(0.15*0.1))*1e45

Iz['Lbol']=Lbol

Ledd=1.26e38*MBH

EddFrac=Lbol/Ledd

Iz['Eddington Fraction']=EddFrac
Iz.to_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/IzumiCND.csv')

#plt.hist(np.log10(Lbol))
#plt.show()
#plt.close()
#plt.hist(np.log10(MBH))
#plt.show()
#plt.close()
#plt.hist(np.log10(EddFrac))
#plt.show()
#plt.close()