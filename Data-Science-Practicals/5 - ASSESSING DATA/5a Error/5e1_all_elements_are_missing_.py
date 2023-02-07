# 5E Drop col where all values are missing
# Executed by Nikhil K Pawanikar
# MScIT Part 1 - Sem 1 
# University Department of Information Technology
# 07-Oct-2022

import sys
import os
import pandas as pd

sOutputFileName='D:\\M.Sc.IT\\Sem 1\\Data Science\\PRACTICAL\\5 ASSESSING DATA\\5a Error\\allmissing.csv'

sFileName='D:\\M.Sc.IT\\Sem 1\\Data Science\\PRACTICAL\\5 ASSESSING DATA\\5a Error\\Good-or-Bad.csv'
print('Loading :',sFileName)
RawData=pd.read_csv(sFileName,header=0)

RawData.shape[0]

print('## Raw Data Values')  
print('################################')  
print(RawData)
print('################################')   
print('## Data Profile') 
print('################################')
print('Rows :',RawData.shape[0])
print('Columns :',RawData.shape[1])

# Remove columns with all missing values
TestData=RawData.dropna(axis=1, how='all')

TestData

print('## Test Data Values')  
print('################################')  
print(TestData)
print('################################')   
print('## Data Profile') 
print('################################')
print('Rows :',TestData.shape[0])
print('Columns :',TestData.shape[1])

TestData.to_csv(sOutputFileName, index = False)



