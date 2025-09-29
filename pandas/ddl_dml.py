import pandas as pd

data={
    "Name":["Nishant","Chintu","Rohan","Shreyas"],
    "City":["Mumbai","Goa","Bengaluru","Pune"],
    "Age":[21,24,19,31],
    "Salary":[22000.90,10000.45,15000.43,12000.78],
}

df=pd.DataFrame(data)
print(df)


#if you just want to add the column at end where position of column doesn't matter
df["Bonus+10%"]=df['Salary']*0.1+df["Salary"]
print(df)

#if you want to add the column where position of column matters
df.insert(0,"ID",[100,200,300,400])
print(df)

#update the specific record from the table 
df.loc[[0,2],'Salary']=40000
print(df)

#update the whole record from the table 
df["Salary"]=df["Salary"]*1.05 #incremet the whole salary by 5%
print(df)


#deleting the column from a table
df.drop(columns=['Bonus+10%','ID'],inplace=True)#inplace is given to make sure the main df is effected
print("After deleting the column \n",df)


