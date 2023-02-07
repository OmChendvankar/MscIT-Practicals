# 8A - Horizontal Slicing Organize Superstep
# Om V Chendvankar
# MScIT Part 1 - Sem 1 
# University Department of Information Technology
# 11-Oct-2022

import sys
import os
import pandas as pd
import sqlite3 as sq

sDWName ='D:\\M.Sc.IT\\Sem 1\\Data Science\\PRACTICAL\\8 ORGANIZING DATA\\datawarehouse.db'
sDbName ='D:\\M.Sc.IT\\Sem 1\\Data Science\\PRACTICAL\\8 ORGANIZING DATA\\datamart.db'

conn1 = sq.connect(sDWName)
conn2 = sq.connect(sDbName)

sTable = 'Dim-BMI'
print('Loading into :',sDbName,' Table:',sTable)
print('From :',sDWName)
sSQL="SELECT * FROM [Dim-BMI];"
PersonFrame0=pd.read_sql_query(sSQL, conn1)

print("Profile")
print(PersonFrame0.shape)

PersonFrame0

sSQL="SELECT PersonID,\
       Height,\
       Weight,\
       bmi,\
       Indicator\
  FROM [Dim-BMI]\
  WHERE \
  Height > 1.5 \
  and Indicator = 1\
  ORDER BY  \
       Height,\
       Weight;"
PersonFrame1=pd.read_sql_query(sSQL, conn1)

#PersonFrame1.head()
print(PersonFrame1.shape)

print(PersonFrame1)

DimPerson=PersonFrame1
DimPersonIndex=DimPerson.set_index(['PersonID'],inplace=False)

sTable = 'Dim-BMI-Horizontal'
print('\n#################################')
print('Storing in:',sDbName,'\n Table:',sTable)
print('\n#################################')
DimPersonIndex.to_sql(sTable, conn2, if_exists="replace")

sSQL="SELECT * FROM [Dim-BMI-Horizontal];"
PersonFrame2=pd.read_sql_query(sSQL, conn2)

print(PersonFrame2)

print('Full Data Set (Rows)   :', PersonFrame0.shape[0])
print('Full Data Set (Columns):', PersonFrame0.shape[1])
print('################################')
print('Horizontal Data Set (Rows)   :', PersonFrame2.shape[0])
print('Horizontal Data Set (Columns):', PersonFrame2.shape[1])
print('################################')

