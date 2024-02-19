import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')

radio=data['Excess Radio (erg/s)']/1e38
xray=data['X-ray Luminosity (ergs/s)']/1e40
mass=data['log M_BH']

FP=1.09*np.log10(radio)-0.59*np.log10(xray)


plt.scatter(FP,mass)
plt.xlabel('FP Luminosity')
plt.ylabel('BH Mass')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/FP.png')
