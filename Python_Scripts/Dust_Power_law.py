from ltsfit.lts_linefit import lts_linefit
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Dust_Power_Law.csv')
param=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Dust_Power_Law_Parameters.csv')

freq=param['Frequency']
flux=param['Flux']
error=param['Error']
Length=param['Length']
for i in range(len(freq)):
	freqi=freq[i]
	fluxi=flux[i]
	errori=error[i]
	freqD=data[freqi]
	fluxD=data[fluxi]
	errorD=data[errori]
	print(freqD[0:Length[i]])
	p=np.polyfit(np.log10(freqD[0:Length[i]]),np.log10(fluxD[0:Length[i]]),1)
	print(p)
