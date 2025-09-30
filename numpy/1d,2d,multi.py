#An array in Python is just a way to 
#store multiple values in a single variable, instead of keeping them in separate variables.

#Oned array a list of numbers which will be in rows only
import numpy as np
oned=np.array([1,2,3,4])
print("1d array is \n",oned)#it will print the array without any commas as list gives ',' after each element

#Twod Array a list of numbers which will be in rows and columns
twod=np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])
print("2d array is \n",twod)

#The array having more then two dimensions 
multi_or_matrix=np.array([
    [1,2,3,4],
    [5,6,7,8]
])
print("Multi dimension or Matrix  is \n",multi_or_matrix)
