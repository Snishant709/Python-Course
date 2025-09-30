#createing the array using array function from numpy library
import numpy as np
l1=[1,2,3,4,5]
arr=np.array(l1)
print("Array using array function in numpy is ",l1)

#creating a 1d array with zeros default
arr2=np.zeros((3)) #pass the dimension taht is r*c in tuples
print("1d array with default value zero is ",(arr2))

#creating a 2d array with ones default
arr3=np.ones((3,2))
print("2d array with default value one is \n",(arr3))

#creating an 2d array with any value of your choice using full function
arr4=np.full((3,3),8)
print("creating an 2d array with any value of your choice \n",arr4)

#creating the range of values in array using arange function
arr5=np.arange(1,10,2)
print("Using arrange function creating array with start and end and interval as 2\n",arr5)

#creating the identity matrix
arr6=np.eye(3)
print("Identity matrix using eye function \n",arr6)

