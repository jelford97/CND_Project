import pandas as pd
import numpy as np

Data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')

OIII=10**(Data['Log OIII Lum (erg/s)'])
Hbeta=10**(Data['log Hbeta (erg/s)'])

Ratio=OIII/Hbeta
print(Ratio)

Data['OII/Hbeta ratio']=Ratio

Data.to_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv',index=False)