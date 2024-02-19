import pandas as pd
import numpy as np

data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')

radioerr=data['Radio Luminosity Error (L_solar)']

radioerr_erg=radioerr*3.826e33

data['Radio Luminosity Error (erg/s)']=radioerr_erg

data.to_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv',index=False)