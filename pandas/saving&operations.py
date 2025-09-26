import pandas as pd

#creating a dinctionary and saving it as a file
data={
    "Name":["Nishant","Chintu","Rohan","Shreyas"],
    "City":["Mumbai","Goa","Bengaluru","Pune"],
    "Age":[21,24,19,31],
    "Salary":[22000.90,10000.45,15000.43,12000.78],
}
df=pd.DataFrame(data)
print(df)
#saving .csv file
df.to_csv("output.csv")#if not given flase then will give index to every rows from 0
#saving .csv file
df.to_excel("output.xlsx",index=False)
#saving .json file
df.to_json("output.json",index=False)

#info()-shape,rows count,column names,data types,null counts,and memory usage of your df.
print("Knowing more about your data",df.info())

#describe()-gives you the statistical info about your data
print("Knowing more about statistical data \n",df.describe())

