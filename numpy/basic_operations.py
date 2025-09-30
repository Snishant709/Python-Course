import numpy as np
l1=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
l2=[1,2.5,3.45,4,5]
arr=np.array(l1)
arr2=np.array(l2)
print("Shape of the array arr is ",np.shape(arr))#knowing the shape that is r*c
print("Size of array arr is ",np.size(arr))#size
print("Data type of arr2 is ",arr2.dtype)#data type
print("Dimesion in the array arr is ",arr.ndim)#dimesnion
print("Dimesion in the array arr2 is ",arr2.ndim)
print("Changing the dataype of arr2 ",arr2.astype(int).dtype)#typecast


#so performing any airthemtic operations in array using numpy becomes easy instead of list
print("Adding 10 more to arr2 ",arr2+10)
#if it was list then it would take time as we first have to run loop and then make it to store in variable
print("Adding 10 more to arr2 ",arr2*10)


#aggregation functions in numpy
print("Sum of arr2 is ",arr2.sum())
print("Sum of arr is ",arr.sum())
print("Average of arr2 is ",arr2.mean())

#similarly you can perform any other aggregation function ex -min(),max(),etc




