import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')

mmflux=data['1mm flux density (Jy)']
STM=data['Stellar Mass (Log)']

plt.semilogy(STM,mmflux,'o')
plt.xlabel('log(Stellar Mass)')
plt.ylabel('mm flux (jy)')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/mmvsStar_mass.png')
plt.close()

WISDOM=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/WISDOM_basic_params.csv')
Sigma_stars=WISDOM['sigma_stars']

Msigma=1.9*(Sigma_stars/200)**5.1
MBH=Msigma*1e8

plt.semilogy(np.log10(MBH),mmflux,'o')
plt.xlabel('SMBH mass (M_sol)')
plt.ylabel('Nuclear mm flux (Jy)')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/mmvsMBH.png')
plt.close()
