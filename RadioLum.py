import pandas as pd
import numpy as np
import math

data=pd.read_csv('Documents/Python.csv')

radioF=data['Radio Flux (Jy)']
radioerr=data['Radio Flux Uncertainty (Jy)']
dist=data['Distance (Mpc)']

radioFL=radioF*1e-23
distcm=dist*3.086e24

radioL=4*math.pi*(distcm)**2*radioFL*1.4e9
radioLsol=radioL/3.846e33
radiosol=np.around(radioLsol,0)

radiosolerr=radiosol*(radioerr/radioF)

data['Radio Luminosity (L_solar)']=radiosol
data['Radio Luminosity Error (L_solar)']=radiosolerr
data.to_csv('Documents/Python.csv',index=False)



