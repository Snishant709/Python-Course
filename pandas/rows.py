import pandas as pd

#on vs code you have to specify the encoding=utf8 or encoding-latin1 on 2nd parameter
df=pd.read_excel("/workspaces/Python-Course/pandas/excel_file.xlsx")
#if no value is passed as n then it will take 5 as default for head()
print("Displaying the first 10 rows \n",df.head(10))#dispalys the first 10 records
#if no value is passed as n then it will take 5 as default for tail()
print("Displaying the last 10 rows \n",df.tail(10))#dispalys the first 10 records




