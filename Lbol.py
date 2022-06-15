import pandas as pd
import numpy as np

data=pd.read_csv('Documents/Python.csv')

Lbol=data['OIII Lbol']

print(np.sort(Lbol))
