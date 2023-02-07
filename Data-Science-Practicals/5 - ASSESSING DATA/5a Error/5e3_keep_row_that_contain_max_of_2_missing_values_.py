
# 5E Drop rows where more than 2 values are missing
# Executed by Nikhil K Pawanikar
# MScIT Part 1 - Sem 1 
# University Department of Information Technology
# 07-Oct-2022

import sys
import os
import pandas as pd

sInputFileName='/content/Good-or-Bad.csv'
sOutputFileName='/content/morethan2missing.csv'

print('Loading :',sInputFileName)
RawData=pd.read_csv(sInputFileName,header=0)

print('## Raw Data Values')  
print('################################')  
print(RawData)
print('################################')   
print('## Data Profile') 
print('################################')
print('Rows :',RawData.shape[0])
print('Columns :',RawData.shape[1])

# Drop rows where more than 2 values are missing
TestData=RawData.dropna(thresh=2)

print('## Test Data Values')  
print('################################')  
print(TestData)
print('################################')   
print('## Data Profile') 
print('################################')
print('Rows :',TestData.shape[0])
print('Columns :',TestData.shape[1])

TestData.to_csv(sOutputFileName, index = False)