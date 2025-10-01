import pandas as pd
import numpy as np
#loading dataset
source=pd.read_excel("/workspaces/Python-Course/numpy/project/indian_employee_data.xlsx")
df=pd.DataFrame(source)
#loading the start 5 data from the dataframe
print("First 5 rows drom Data is \n",df.head())
#loading the last 5 data from the dataframe
print("Last 5 rows drom Data is \n",df.tail())


#identifying the nan value from the data
print("Printing the nan values from each column \n",df.isnull().sum())

#filling the nan salary values with the average salary from the salary column
print("Result before replacing the inf and -inf in salary column \n",df)
#but before putting average we have to replace the inf value with nan value so that we dont get the inf as a average
df.replace([np.inf,-np.inf,"inf"],np.nan,inplace=True)
print("After applying the replace function the inf and -inf value is replaced with the nan \n",df)

#now we can replace the nan value with the average of salary column
df['Salary (INR)']=df['Salary (INR)'].fillna(df['Salary (INR)'].mean())
print("After replacing the nan value with the average of salary \n",df)
print(df['Salary (INR)'].dtype)


#now fill na values in performance rating with the median of that column
df['Performance Rating']=df['Performance Rating'].fillna(df['Performance Rating'].median())
print("Replacing the nan values in the performance column with the median \n",df)



#adding the duplicate row so in order to perform the duplicate records deleltion
new_row = {
    "Emp_ID": 101,
    "Name": "Amit Sharma",
    "Age": 27.0,
    "Salary (INR)": 650000.0,
    "Experience (Years)": 4.0,
    "City": "Delhi",
    "Department": "IT",
    "Performance Rating": 4.5
}
df.loc[len(df)] = new_row
print("After concatenating the duplicate row \n",df)


#dropping the duplicates
df.drop_duplicates(inplace=True)
print("Dropping the duplicate values \n",(df))

#replacing the negative value
df['Salary (INR)']=np.where(df['Salary (INR)']<0,df["Salary (INR)"].mean(),df["Salary (INR)"])
print(df)
#so the above statement will replace the 7th id salary with the mean

