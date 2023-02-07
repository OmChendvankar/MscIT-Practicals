import sqlite3 as sq
import pandas as pd

DatabaseName="D:\\M.Sc.IT\\Sem 1\\RIC\\Practicals\\RIC-Pracitcal_Data\\Practical-01\\Vermeulen.db"
conn =sq.connect(DatabaseName)

FileName='D:\\M.Sc.IT\\Sem 1\\RIC\\Practicals\\RIC-Pracitcal_Data\\Practical-01\\Retrieve_IP_DATA.csv'
print('Loading :',FileName)
IP_DATA_ALL_FIX=pd.read_csv(FileName,header=0,low_memory=False)
IP_DATA_ALL_FIX.index.names = ['RowIDCSV']
print(IP_DATA_ALL_FIX)
Table='IP_DATA_ALL'
print('Storing :',DatabaseName,' Table:',Table)
