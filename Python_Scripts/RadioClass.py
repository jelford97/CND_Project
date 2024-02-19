import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')
jet=data[data['Radio Jet']=='Yes']
#HERG=jet[jet['Radio Galaxy Class']=='HERG']
#LERG=jet[jet['Radio Galaxy Class']=='LERG']
LOIIIH=jet['Log OIII Lum (erg/s)']
radioH=jet['Radio Flux (Jy)']
distH=jet['Distance (Mpc)']
distmH=distH*3.086e22
radioLumH=4*math.pi*(distmH**2)*(radioH*1e-26)
OIIIH=10**(LOIIIH)
OIIIsolH=OIIIH/3.846e33

#LOIIIL=LERG['Log OIII Lum (erg/s)']
#radioL=LERG['Radio Flux (Jy)']
#distL=LERG['Distance (Mpc)']
#distmL=distL*3.086e22
#radioLumL=4*math.pi*(distmL**2)*(radioL*1e-26)
#OIIIL=10**(LOIIIL)
#OIIIsolL=OIIIL/3.846e33

#print(HERG['Radio Flux (Jy)'])


x=np.logspace(18,27,100)
c=10**(5.9)
y=c*((x/1e22)**(0.3))

plt.loglog(radioLumH,OIIIsolH,'o',color='blue')
#plt.axhline(7.50e5)
#plt.loglog(radioLumL,OIIIsolL,'o',color='orange')
plt.plot(x,y,color='black',linestyle='--')
plt.xlabel('1.4 GHz Radio Emission (W/Hz)')
plt.ylabel('OIII Luminosity (Lsol)')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/HERGvLERGClass.png')
plt.show()