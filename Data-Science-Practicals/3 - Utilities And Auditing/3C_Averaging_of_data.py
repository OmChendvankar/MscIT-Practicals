
# PRACTICAL 3 - Utilities and Auditing
# 3C. AVERAGING OF DATA
# Om V Chendvankar - 23-SEP-2022
# UNIVERSITY DEPARTMENT OF INFORMATION TECHNOLOGY

import pandas as pd
################################################################
InputFileName='D:\\M.Sc.IT\\Sem 1\\Data Science\\PRACTICAL\\3 UTILITIES AND AUDITING\\IP_DATA_CORE.csv'

IP_DATA_ALL=pd.read_csv(InputFileName,header=0,low_memory=False, usecols=['Country','Place Name','Latitude','Longitude'], encoding="latin-1")
print(IP_DATA_ALL.shape)
print(IP_DATA_ALL.head())

IP_DATA_ALL.rename(columns={'Place Name': 'Place_Name'}, inplace=True)
print(IP_DATA_ALL.head())

AllData=IP_DATA_ALL[['Country', 'Place_Name','Latitude']]
print(AllData)

MeanData=AllData.groupby(['Country', 'Place_Name'])['Latitude'].mean()
print(MeanData)

