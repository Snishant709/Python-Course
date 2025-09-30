import pandas as pd

data = {
    'Name': ['Amit', 'Ravi', None, 'Simran'],
    'Age': [25, None, 22, 28],
    'Salary': [18000, 25000, None, None]
}

df = pd.DataFrame(data)

#will print True and False for whole dataframe if there is 'None' value 
print(df.isnull())

#will return the sum of all the None values in the column
print(df.isnull().sum())


#droping the rows of None values axis=0 means rows
# df.dropna(axis=0,inplace=True)
# print("Dropping the rows \n",df)


#droping the column of None values axis=1 means columns
# df.dropna(axis=1,inplace=True)
# print("Dropping the columns \n",df)


#dropping the None values from a table
# df.dropna(inplace=True)
# print("Without axis delete \n",df)


#filling the 'None' values with whatever values you want to fill for whole df
# df.fillna(0,inplace=True)
# print(df)


#filling the 'None' values with the mean of age 

df['Age']=df.fillna(df["Age"].mean(), inplace=True)

print(df)