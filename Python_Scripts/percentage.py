import pandas as pd
import numpy as np

python=pd.read_csv('Documents/Python.csv')
WISDOM=pd.read_csv('Documents/WISDOM_basic_params(1).csv')

TotalMass=python['Total Mass']
WISDOMMass=WISDOM['MH2']

diff=TotalMass/WISDOMMass

print(diff)
