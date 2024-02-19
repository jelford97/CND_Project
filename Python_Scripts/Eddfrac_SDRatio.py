import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')
PlotData=data[['Eddington Fraction','Surface Density Ratio']]
PlotDataN=PlotData.dropna()
#print(PlotDataN)
Eddfrac=np.log10(data['Eddington Fraction'])
SDRatio=data['Surface Density Ratio']



plt.scatter(Eddfrac,SDRatio)
plt.show()
