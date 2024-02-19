import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')

LERG=data[data['LERG']=='Y']
NonLERG=data[data['LERG']=='N']

plt.loglog(LERG['Mass 50pc'],LERG['X-ray Luminosity (ergs/s)'],'o',color='blue',label='LERGS')
plt.loglog(NonLERG['Mass 100pc'],NonLERG['X-ray Luminosity (ergs/s)'],'o',color='red',label='Non LERGS')
plt.xlabel('Mass 75pc Msol')
plt.ylabel('Xray Luminosity (erg/s)')
plt.legend()
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/50pcLERGXray.png',bbox_inches='tight')
plt.close()

plt.loglog(LERG['Mass 50pc'], LERG['Accretion rate (M_solar/yr)'], 'o',color='blue',label='LERGS')
plt.loglog(NonLERG['Mass 100pc'],NonLERG['Accretion rate (M_solar/yr)'],'o',color='red',label='Non LERGS')
plt.xlabel('Mass 75pc Msol')
plt.ylabel('Accretion rate M_sol/yr')
plt.legend()
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/50pcLERGAccRate.png',bbox_inches='tight')
plt.close() 
