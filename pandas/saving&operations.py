import pandas as pd

#Series is 1d array consists of single column which is indexed
#Dataframe is 2d array consists of column and rows which both together are indexed

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

#get the rows where slary is above 20000
print(df[df['Salary']>20000])

#get only the name and salary of the employee whoose salary is less then 20000
print(df.loc[df['Salary']<20000,['Name','Age']])
#the below one will not work as here precendence of '<' and '>' is less then bitwise operator '&'
#print(df.loc[df['Salary']<20000 & df['Salary']>10000 ,['Name','Salary']])

#so use the below code
print(df.loc[(df['Salary']<20000) & (df['Salary']>10000) ,['Name','Salary']])
# or
print(df.loc[df['Salary'].between(10000,20000),['Name','Salary']])



