import pandas as pd
#for csv 
#df=pd.read_csv("/workspaces/Python-Course/pandas/csv_file.csv")
#for excel
#pip install openpyxl -run this command to read the excel file
#df=pd.read_excel("/workspaces/Python-Course/pandas/excel_file.xlsx")
#gcsfs fo reading dat from cloud
df=pd.read_json("/workspaces/Python-Course/pandas/sample4.json")
print(df)

