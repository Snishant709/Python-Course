import pandas as pd

data={
    'CustomerID': [1, 2, 3],
    'CustomerName': ['Amit', 'Ravi', 'Simran']
}

customers=pd.DataFrame(data)

# Orders table
orders = pd.DataFrame({
    'OrderID': [101, 102, 103],
    'CustomerID': [1, 2, 4],   # Note: CustomerID 4 does not exist in Customers
    'Amount': [500, 700, 300]
})


#joins
res=pd.merge(customers,orders,on="CustomerID",how="left")
print(res)



#set operations
data={
    'CustomerID': [1, 2, 3],
    'CustomerName': ['Amit', 'Ravi', 'Simran']
}

data1=pd.DataFrame(data)

# Orders table
data2 = pd.DataFrame({
    'CustomerID': [4, 5, 6],
    'CustomerName': ['Baala', 'Nishant', 'Devdas']
})


res2=pd.concat([data1,data2],ignore_index=True)#by default it takes 0 axis
print("Printing the union keeping the row as true \n",res2)

res2=pd.concat([data1,data2],axis=1,ignore_index=True)
print("Printing the union keeping the column as true \n",res2)