# PRACTICAL 2 - CONVERTING DATA TO HORUS
# 2A. CSV TO HORUS
# OM V CHENDVANKAR - 13-SEP-2022
# UNIVERSITY DEPARTMENT OF INFORMATION TECHNOLOGY

# IMPORTING LIBRARIES 
import pandas as pd

# OPEN FILE
fname='D:\\M.Sc.IT\\Sem 1\\Data Science\\PRACTICAL\\2 CONVERTING DATA TO HORUS\\Country_Code.csv'
fname

# reading data in file 
in_data = pd.read_csv(fname,encoding='latin-1')

print('Input Data Values ===================================')
print(in_data)
print('=====================================================')

process_data = in_data
process_data

# Process

# drop coloumns
process_data.drop('ISO-3-Code', axis=1, inplace=True)
process_data.drop('ISO-2-CODE', axis=1, inplace=True)

process_data

# rename existing coloumns
process_data.rename(columns={'Country': 'CountryName'}, inplace=True)
process_data.rename(columns={'ISO-M49': 'CountryNumber'}, inplace=True)

process_data

process_data.set_index('CountryNumber', inplace=True)
process_data.sort_values('CountryNumber', axis=0, ascending=True, inplace=True)
print(process_data)

process_data.sort_values('CountryName', axis=0, ascending=True, inplace=True)
print(process_data)

# Output agreement

OutputData=process_data
sOutputFileName='D:\\M.Sc.IT\\Sem 1\\Data Science\\PRACTICAL\\2 CONVERTING DATA TO HORUS\\HORUS-CSV-Country.csv'
OutputData.to_csv(sOutputFileName, index = False)
