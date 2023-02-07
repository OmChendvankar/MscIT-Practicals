# 5E Drop col where any element are missing
# Executed by Nikhil K Pawanikar
# MScIT Part 1 - Sem 1 
# University Department of Information Technology
# 07-Oct-2022

import sys
import os
import pandas as pd
################################################################

sOutputFileName='/content/anymissing.csv'
sInputFileName='/content/Good-or-Bad.csv'

print('Loading :',sInputFileName)
RawData=pd.read_csv(sInputFileName,header=0)

print('## Raw Data Values')  
print('################################')  
print(RawData)
print('################################')   
print('## Data Profile') 
print('################################')
print('Rows    :',RawData.shape[0])
print('Columns :',RawData.shape[1])

# Drop columns where any value is missing
TestData=RawData.dropna(axis=1, how='any')

################################################################
print('################################')  
print('## Test Data Values')  
print('################################')  
print(TestData)
print('################################')   
print('## Data Profile') 
print('################################')
print('Rows :',TestData.shape[0])
print('Columns :',TestData.shape[1])

TestData.to_csv(sOutputFileName, index = False)

