import pandas as pd
import numpy as np

data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')
mm=data['1mm flux density (Jy)']

mjy=mm/1e-3
data['mjy']=mjy

mjydata=data[['Galaxy','mjy']]

mjy5=mjydata[mjydata['mjy']>5]

print(mjy5)