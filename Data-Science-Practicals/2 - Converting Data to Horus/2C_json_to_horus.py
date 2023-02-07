
# PRACTICAL 2 - CONVERTING DATA TO HORUS
# 2C. JSON TO HORUS
# OM V CHENDVANKAR - 13-SEP-2022
# UNIVERSITY DEPARTMENT OF INFORMATION TECHNOLOGY


import pandas as pd

# Input Agreement ============================================
sInputFileName='D:\\M.Sc.IT\\Sem 1\\Data Science\\PRACTICAL\\2 CONVERTING DATA TO HORUS\\Country_Code.json'
InputData=pd.read_json(sInputFileName, orient='index', encoding="latin-1")

InputData.head()

# Processing Rules ===========================================
ProcessData=InputData
# Remove columns ISO-2-Code and ISO-3-CODE
ProcessData.drop('ISO-2-CODE', axis=1,inplace=True)
ProcessData.drop('ISO-3-Code', axis=1,inplace=True)
ProcessData.head()

# Rename Country and ISO-M49
ProcessData.rename(columns={'Country': 'CountryName'}, inplace=True)
ProcessData.rename(columns={'ISO-M49': 'CountryNumber'}, inplace=True)
ProcessData.head()

# Set new Index
ProcessData.set_index('CountryNumber', inplace=True)

# Sort data by CurrencyNumber
ProcessData.sort_values('CountryNumber', axis=0, ascending=True, inplace=True)

print(ProcessData)

# Output Agreement ===========================================
OutputData=ProcessData
sOutputFileName='D:\\M.Sc.IT\\Sem 1\\Data Science\\PRACTICAL\\2 CONVERTING DATA TO HORUS\\outputs\\JSON-HORUS.csv'
OutputData.to_csv(sOutputFileName, index = True)
print('JSON to HORUS - Done')

