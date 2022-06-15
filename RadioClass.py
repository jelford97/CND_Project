import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

data=pd.read_csv('Documents/Python.csv')
jet=data[data['Radio Jet']=='Yes']
HERG=jet[jet['Radio Galaxy Class']=='HERG']
LERG=jet[jet['Radio Galaxy Class']=='LERG']
LOIIIH=HERG['Log OIII Lum (erg/s)']
radioH=HERG['Radio Flux (Jy)']
distH=HERG['Distance (Mpc)']
distmH=distH*3.086e22
radioLumH=4*math.pi*(distmH**2)*(radioH*1e-26)
OIIIH=10**(LOIIIH)
OIIIsolH=OIIIH/3.846e33

LOIIIL=LERG['Log OIII Lum (erg/s)']
radioL=LERG['Radio Flux (Jy)']
distL=LERG['Distance (Mpc)']
distmL=distL*3.086e22
radioLumL=4*math.pi*(distmL**2)*(radioL*1e-26)
OIIIL=10**(LOIIIL)
OIIIsolL=OIIIL/3.846e33



x=np.logspace(18,27,100)
c=10**(5.9)
y=c*((x/1e22)**(0.3))

plt.loglog(radioLumH,OIIIsolH,'o',color='blue')
plt.loglog(radioLumL,OIIIsolL,'o',color='orange')
plt.plot(x,y,color='black',linestyle='--')
plt.xlabel('1.4 GHz Radio Emission (W/Hz)')
plt.ylabel('OIII Luminosity (Lsol)')
plt.savefig('HERGvLERGClass.png')
