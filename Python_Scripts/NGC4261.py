import numpy as np

freq=[2.29e11,2.31e11,2.45e11,2.47e11]
flux=[0.190,0.188,0.182,0.181]

m,c=np.polyfit(np.log10(freq),np.log10(flux),1)

print(m)
