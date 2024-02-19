import pandas as pd
import numpy as np

Data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')

Lbol=Data['Bolometric Luminosity (erg/s)']
e=0.1

Macc=0.15*(e/0.1)*(Lbol/1e45)
Maccerr=Macc*0.1

Data['Accretion rate (M_solar/yr)']=Macc
Data['Accretion Rate Error']=Maccerr

Data.to_csv('/Users/jelford/Documents/Phd_Work/CND_Project/CSV_Files/Python.csv',index=False)