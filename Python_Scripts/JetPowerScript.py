import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import scipy.stats as stats

plt.rcParams['font.family'] = 'Latin Modern Roman'
plt.rcParams.update({'font.size': 10})
plt.rcParams['legend.fontsize'] = 14
plt.rcParams['axes.linewidth'] = 1.5
plt.rcParams['xtick.labelsize'] = 12;
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['xtick.major.size'] = 10;
plt.rcParams['ytick.major.size'] = 10
plt.rcParams['xtick.major.width'] = 2;
plt.rcParams['ytick.major.width'] = 2
plt.rcParams['xtick.minor.size'] = 5;
plt.rcParams['ytick.minor.size'] = 5
plt.rcParams['xtick.minor.width'] = 1;
plt.rcParams['ytick.minor.width'] = 1
plt.rcParams['xtick.direction'] = 'in';
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['xtick.bottom'] = True
plt.rcParams['ytick.left'] = True
params = {'mathtext.default': 'regular'}
plt.rcParams.update(params)
plt.rcParams['axes.labelsize'] = 16
plt.rcParams['ytick.right']=True
plt.rcParams['xtick.top']=True

data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')
#ATLAS=pd.read_csv('Documents/ATLAS3D.csv')

radio=data['Excess Radio (erg/s)']
D=data['Distance (Mpc)']
radioflux=radio/(4*math.pi*(D*3.086e24)**2*1.4e9)
#print(radioflux)

#ATLASmjy=np.array(ATLAS['1.4 GHz Flux'])
#ATLASflux=ATLASmjy*1e-3
#ATLASerg=ATLASflux*1e-23
#ATLASdist=np.array(ATLAS['Distance (Mpc)'])

def jet_power(Di,radio):
    dist=Di*3.086e24
    H0=70
    c=3e5
    z=(H0*Di)/c
    v0=1.4e9
    alph=0.8
    rpower=4*math.pi*(dist**2)*((1+z)**(alph-1))*radio*v0
    logpower=0.75*np.log10(rpower/1e40)+1.91
    jpower=10**(logpower)
    power=jpower*1e42
    return power

power=jet_power(D,radioflux)
#print(power)
data['Jet Power']=power
data.to_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')
#ATLASpower=jet_power(ATLASdist,ATLASerg)
#ATLASLM=np.array(ATLAS['log(Mmol)'])
#ATLASmass=10**ATLASLM

mass=np.logspace(5,12,100)
babyk=1e39*(mass/1e5)**(1.25)

mass100=data['Mass 100pc']
mass75=data['Mass 75pc']
mass50=data['Mass 50pc']
totalmass=data['Total Mass']

plt.loglog(mass100,power,'o')
plt.xlabel('$M_{H2, 100pc} (M_{\odot})$')
plt.ylabel('Jet Power (erg/s)')
#plt.plot(mass,babyk,'--',color='black')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/JetPower100pc.png')
plt.close()

r100=data[['Mass 100pc','Jet Power']]
r100n=r100.dropna()
print(stats.spearmanr(r100n['Mass 100pc'],r100n['Jet Power']))

plt.loglog(mass75,power,'o')
plt.xlabel('$M_{H2, 75pc} (M_{\odot})$')
plt.ylabel('Jet Power (erg/s)')
#plt.plot(mass,babyk,'--',color='black')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/JetPower75pc.png')
plt.close()

r75=data[['Mass 75pc','Jet Power']]
r75n=r75.dropna()
print(stats.spearmanr(r75n['Mass 75pc'],r75n['Jet Power']))

plt.loglog(mass50,power,'o')
plt.xlabel('$M_{H2, 50pc} (M_{\odot})$')
plt.ylabel('Jet Power (erg/s)')
#plt.plot(mass,babyk,'--',color='black')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/JetPower50pc.png')
plt.close()

r50=data[['Mass 50pc','Jet Power']]
r50n=r50.dropna()
print(stats.spearmanr(r50n['Mass 50pc'],r50n['Jet Power']))

plt.loglog(totalmass,power,'o')
#plt.loglog(babykmass,babykpower,'o')
plt.xlabel('$M_{H2, Total} (M_{\odot})$')
plt.ylabel('Jet Power (erg/s)')
plt.plot(mass,babyk,'--',color='black')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/TotalMassJetPower.png')
plt.close()

plt.loglog(power,totalmass,'o')
#plt.loglog(ATLASpower,ATLASmass,'o')
plt.ylabel('$M_{H2, Total} (M_{\odot})$')
plt.xlabel('Jet Power (erg/s)')
plt.plot(babyk,mass,'--',color='black')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/JetPowerTotalMass.png')
plt.close()

