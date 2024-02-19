import pandas as pd
import numpy as np

data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')

SI=data['Spectral Index']
SIerr=data['New Index Error']

Per=(SIerr/np.abs(SI))*100

print(np.sort(Per))