import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')
WISDOM=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/WISDOM_basic_params.csv')

Totmass=data['Total Mass']
WISDOMtotmass=WISDOM['MH2']
#print(np.log10(WISDOMtotmass))
x=np.logspace(5,11,100)
y=x
print(Totmass/WISDOMtotmass)

plt.loglog(WISDOMtotmass,Totmass,'o')
plt.loglog(x,y,'--',color='black')
plt.xlabel('Total Mass WISDOM M_sol')
plt.ylabel('My Total Mass M_sol')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/TotalMass.png')
plt.close()
