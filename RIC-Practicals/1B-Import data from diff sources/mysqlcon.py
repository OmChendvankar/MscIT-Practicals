import mysql.connector

conn =mysql.connector.connect(
host='localhost',
database='specialshare',
user='root',
password='')
conn.connect
if(conn.is_connected):
    print('###### Connection With MySql EstablishedSuccessfullly ##### ')
else:
    print('Not Connected -- Check Connection Properites')


