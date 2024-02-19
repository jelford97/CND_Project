import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')

Tim=data[data['Source']=='Tim']

TimSFR=10**(Tim['Tim SFR Log'])
TimTotMass=Tim['Total Mass']

tdep=TimTotMass/TimSFR
SFE=1/tdep

print(np.sort(np.log10(tdep)))
print(np.sort(np.log10(SFE)))
