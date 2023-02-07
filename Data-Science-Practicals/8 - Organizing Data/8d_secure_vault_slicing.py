#PRACTICAL 8 – Organizing Data
# Vermullen-4)Secure Vault Slicing
# OM V CHENDVANKAR- 22-NOV-2022
# UNIVERSITY DEPARTMENT OF INFORMATION TECHNOLOGY

import sys
import os
import pandas as pd
import sqlite3 as sq

sDWName ='D:\\M.Sc.IT\\Sem 1\\Data Science\\PRACTICAL\\8 ORGANIZING DATA\\datawarehouse.db'
sDMName ='D:\\M.Sc.IT\\Sem 1\\Data Science\\PRACTICAL\\8 ORGANIZING DATA\\datamart.db'

conn1 = sq.connect(sDWName)
conn2 = sq.connect(sDMName)

print('################')
sTable = 'Dim-BMI'
print('Loading :',sDMName,' Table:',sTable)
sSQL="SELECT * FROM [Dim-BMI];"
PersonFrame0=pd.read_sql_query(sSQL, conn1)

print('################')
sTable = 'Dim-BMI'
print('Loading :',sDMName,' Table:',sTable)

sSQL="SELECT Height,Weight,\
    Indicator,\
    CASE Indicator\
    WHEN 1 THEN 'Pip'\
    WHEN 2 THEN 'Norman'\
    WHEN 3 THEN 'Grant'\
    ELSE 'Sam'\
    END AS Name\
    FROM [Dim-BMI]\
    WHERE Indicator > 2\
    ORDER BY \
    Height,\
    Weight;"
PersonFrame1=pd.read_sql_query(sSQL, conn1)

DimPerson=PersonFrame1
DimPersonIndex=DimPerson.set_index(['Indicator'],inplace=False)
                                    
sTable = 'Dim-BMI-Secure'
print('\n#################################')
print('Storing :',sDMName,'\n Table:',sTable)
print('\n#################################')
DimPersonIndex.to_sql(sTable, conn2, if_exists="replace")
                                    
print('################################')
sTable = 'Dim-BMI-Secure'
print('Loading :',sDMName,' Table:',sTable)
print('################################')
                                    
sSQL="SELECT * FROM [Dim-BMI-Secure] WHERE Name = 'Sam';"                               
PersonFrame2=pd.read_sql_query(sSQL, conn2)
                                    
print('################################')
print('Full Data Set (Rows):', PersonFrame0.shape[0])
print('Full Data Set (Columns):', PersonFrame0.shape[1])
print('################################')
print('Horizontal Data Set (Rows):', PersonFrame2.shape[0])
print('Horizontal Data Set (Columns):', PersonFrame2.shape[1])
print('Only Sam Data')
print(PersonFrame2.head())
print('################################')
