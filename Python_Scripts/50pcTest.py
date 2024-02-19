import pandas as pd
import numpy as np
import scipy.stats as stats

data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')

test=data[['Excess Radio Log','Mass 50pc']]
testn=test.dropna()
testnn=testn[testn['Excess Radio Log']>0]

Stat=stats.spearmanr(testnn['Mass 50pc'],testnn['Excess Radio Log'])
print(Stat)
