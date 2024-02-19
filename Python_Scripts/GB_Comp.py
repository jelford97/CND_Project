import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')

xray=data['Adjusted X-ray Luminosity (Lsolar)']*3.846e33
Mass100pc=data['Mass 100pc']
Mass75pc=data['Mass 75pc']
Mass50pc=data['Mass 50pc']

NewDataDict={'Xray (erg/s)':np.array(xray),'Mass100pc':Mass100pc,'Mass75pc':Mass75pc,'Mass50pc':Mass50pc}
NewData=pd.DataFrame(NewDataDict)

GB_Data_X=NewData[NewData['Xray (erg/s)'].between(1e38,1e44)]
GB_Data_100=GB_Data_X[GB_Data_X['Mass100pc'].between(1e6,1e10)]

plt.loglog(GB_Data_100['Mass100pc'],GB_Data_100['Xray (erg/s)'],'o')
plt.xlabel('Mass 100pc')
plt.ylabel('X-ray Lum')
plt.show()