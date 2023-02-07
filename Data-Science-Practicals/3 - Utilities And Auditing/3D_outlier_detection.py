# PRACTICAL 3 - Utilities and Auditing
# 3D. OUTLIER DETECTION
# Om V Chendvankar - 27-SEP-2022
# UNIVERSITY DEPARTMENT OF INFORMATION TECHNOLOGY

import pandas as pd

InputFileName='D:\\M.Sc.IT\\Sem 1\\Data Science\\PRACTICAL\\3 UTILITIES AND AUDITING\\IP_DATA_CORE.csv'
OutputFileName='D:\\M.Sc.IT\\Sem 1\\Data Science\\PRACTICAL\\3 UTILITIES AND AUDITING\\Outlier.csv'

IP_DATA_ALL=pd.read_csv(InputFileName,header=0,low_memory=False,
  usecols=['Country','Place Name','Latitude','Longitude'], encoding="latin-1")
IP_DATA_ALL.rename(columns={'Place Name': 'Place_Name'}, inplace=True)

print(IP_DATA_ALL.head())

LondonData=IP_DATA_ALL.loc[IP_DATA_ALL['Place_Name']=='London']
print(LondonData.shape)

AllData=LondonData[['Country', 'Place_Name','Latitude']]
print('All Data')
print(AllData)

MeanData=AllData.groupby(['Country', 'Place_Name'])['Latitude'].mean()
StdData=AllData.groupby(['Country', 'Place_Name'])['Latitude'].std()

print('Mean Data')
print(MeanData)

print('Std Data')
print(StdData)

UpperBound=float(MeanData+StdData)

LowerBound=float(MeanData-StdData)

print('Lower than ', LowerBound)
OutliersLower=AllData[AllData.Latitude<LowerBound]
print(OutliersLower)

print('Greater than ', UpperBound)
OutliersUpper=AllData[AllData.Latitude>UpperBound]
print(OutliersUpper)

OutliersUpper.shape

print('Not Outliers')
OutliersNot=AllData[(AllData.Latitude>=LowerBound) & (AllData.Latitude<=UpperBound)]
print(OutliersNot)
######################



