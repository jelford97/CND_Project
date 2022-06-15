import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')
RadioData=data[['Radio Luminosity (L_solar)','Total Mass']]
RadioDataN=RadioData.dropna()

RadioLum=RadioDataN['Radio Luminosity (L_solar)']*3.826e33
TotMass=RadioDataN['Total Mass']

S=stats.spearmanr(TotMass,RadioLum)

print(S)

plt.loglog(TotMass,RadioLum,'o')
plt.xlabel('Total Mass (L_solar)')
plt.ylabel('Global Radio Luminosity (erg/s)')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/Global_Radio.png',bbox_inches='tight')
plt.close()
