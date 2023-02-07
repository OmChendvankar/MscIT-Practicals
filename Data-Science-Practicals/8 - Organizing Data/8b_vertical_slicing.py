# 8A - Vertical Slicing Organize Superstep
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
sSQL="SELECT * FROM [Dim-BMI];"
PersonFrame0=pd.read_sql_query(sSQL, conn1)
print(PersonFrame0.shape)

print(PersonFrame0.head())

sSQL="SELECT \
       Height,\
       Weight,\
       Indicator\
  FROM [Dim-BMI];"
PersonFrame1=pd.read_sql_query(sSQL, conn1)
print(PersonFrame1.shape)

print(PersonFrame1.head())

DimPerson=PersonFrame1
DimPersonIndex=DimPerson.set_index(['Indicator'],inplace=False)

print(DimPersonIndex.head())

sTable = 'Dim-BMI-Vertical'
DimPersonIndex.to_sql(sTable, conn2, if_exists="replace")

sSQL="SELECT * FROM [Dim-BMI-Vertical];"
PersonFrame2=pd.read_sql_query(sSQL, conn2)

print(PersonFrame2.shape)

print('Full Data Set (Rows)   :', PersonFrame0.shape[0])
print('Full Data Set (Columns):', PersonFrame0.shape[1])

print('Vertical Data Set (Rows)   :', PersonFrame2.shape[0])
print('Vertical Data Set (Columns):', PersonFrame2.shape[1])

