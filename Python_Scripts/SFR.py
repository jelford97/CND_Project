import pandas as pd
import numpy as np

data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')

Galaxies=['FRL1146','NGC2110','NGC3351','NGC3862','NGC4261','NGC5995']

SFR=[]
for i in range(len(Galaxies)):
    Gal_Data=data[data['Galaxy']==Galaxies[i]]
    Total_Mass=np.array(Gal_Data['Total Mass New'])
    SFRate=Total_Mass/2e9
    SFR.append(np.log10(SFRate))

print(SFR)