import pandas as pd
import numpy as np

data=pd.read_excel('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/ALMA.xlsx')
rms=data['RMS (mJy)']

print(np.sort(rms))