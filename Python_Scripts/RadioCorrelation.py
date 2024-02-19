import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')

Radiodata100=data[['Mass 100pc','Radio Luminosity (L_solar)']]
Radiodata75=data[['Mass 75pc','Radio Luminosity (L_solar)']]
Radiodata50=data[['Mass 50pc','Radio Luminosity (L_solar)']]

Radio100n=Radiodata100.dropna()
Radio75n=Radiodata75.dropna()
Radio50n=Radiodata50.dropna()

Radio100S=Radio100n.sort_values(by=['Radio Luminosity (L_solar)'])
Radio75S=Radio75n.sort_values(by=['Radio Luminosity (L_solar)'])
Radio50S=Radio50n.sort_values(by=['Radio Luminosity (L_solar)'])
#print(RadioS) 

Radio100Lum=np.array(Radio100S['Radio Luminosity (L_solar)'])
Mass100=np.array(Radio100S['Mass 100pc'])

Radio75Lum=np.array(Radio75S['Radio Luminosity (L_solar)'])
Mass75=np.array(Radio75S['Mass 75pc'])

Radio50Lum=np.array(Radio50S['Radio Luminosity (L_solar)'])
Mass50=np.array(Radio50S['Mass 50pc'])

Mass75SH=Mass75.shape
Mass75A=np.array(Mass75SH)

Mass50SH=Mass50.shape
Mass50A=np.array(Mass50SH)

Radio100H=Radio100Lum[3:28]*3.826e33
Mass100H=Mass100[3:28]

Radio75H=Radio75Lum[3:Mass75A[0]]*3.826e33
Mass75H=Mass75[3:Mass75A[0]]

Radio50H=Radio50Lum[3:Mass50A[0]]*3.826e33
Mass50H=Mass50[3:Mass50A[0]]

#print(RadioLumH)
#print(Mass100H)

S100=stats.spearmanr(Mass100H,Radio100H)
print(S100)

plt.loglog(Mass100H,Radio100H,'o')
plt.xlabel('Mass 100pc')
plt.ylabel('Radio Luminosity')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/High_RadioLum_Mass.png',bbox_inches='tight')
plt.close()

S75=stats.spearmanr(Mass75H,Radio75H)
print(S75)

plt.loglog(Mass75H,Radio75H,'o')
plt.xlabel('Mass 75pc')
plt.ylabel('Radio Luminosity')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/High_RadioLum_Mass75.png',bbox_inches='tight')
plt.close()

S50=stats.spearmanr(Mass50H,Radio50H)
print(S50)

plt.loglog(Mass50H,Radio50H,'o')
plt.xlabel('Mass 50pc')
plt.ylabel('Radio Luminosity')
plt.savefig('/Users/jelford/Documents/PhD_Work/CND_Project/Plots/High_RadioLum_Mass50.png',bbox_inches='tight')
plt.close()
