import pandas as pd
data = {
    'Name': ['Amit', 'Ravi', None, 'Simran', 'Amit', 'Ravi', 'Simran', 'Amit', None, 'Ravi'],
    'Age':  [35, None, 30, 40, 10, 25, 40, 10, 30, None],
    'Salary': [100, 50, 75, 25, 100, 60, 25, 120, 75, 50]
}


#sorting the values on the basis of their age and name
df=pd.DataFrame(data)
df.sort_values(by=['Name','Age'], ascending=[True, True],inplace=True)
print(df)


#agregating the salary
avg=df['Salary'].mean()
print("Average salary is ",avg)


#grouping age and name and then aggregating the salary
avg_group_wise=df.groupby(["Age",'Name'])['Salary'].mean()
print("Group wise Average of salary is ",avg_group_wise)
