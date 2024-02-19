import pandas as pd
import numpy as np
import math

data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/WISDOM_basic_params.csv')

sigma=data['sigma_stars']

M=1.9*(sigma/200)**5.1
MBH=M*1e8
MSMBH=np.log10(MBH)

python=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')

python['log M_BH']=MSMBH

python.to_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv',index=False)
