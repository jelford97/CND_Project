import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

Data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')

SFR=10**(Data['Tim SFR Log'])
Xray=Data['X-ray Luminosity (ergs/s)']
Radio=Data['Excess Radio (erg/s)']
mm=Data['mm Luminosity (erg/s)']

plt.loglog(Xray,SFR,'o')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/XraySFR.png')
plt.close()

plt.loglog(Radio,SFR,'o')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/RadioSFR.png')
plt.close()

plt.loglog(mm,SFR,'o')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/mmSFR.png')
plt.close()