
#Interpolation helps in maintaining the data series
# Avoid dropping of rows
# Numeric data with trends
# It doesn't work on categorial data or object datatype
 #It cant be always correct
import pandas as pd

data = {
    'Name': ['Amit', 'Ravi', None, 'Simran'],
    'Age': [10, None, 30, 40],
    'Salary': [18000, 25000, None, None]
}

df = pd.DataFrame(data)
print(df)

#Their are different methods for interpolate which one of them is linear,time,polynomial,etc
df['Age'] = df['Age'].interpolate(method="linear")
print(df)




