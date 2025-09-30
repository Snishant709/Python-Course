import numpy as np
l = [[1,2,3,4,5,6,7,8]]
l1 = np.array(l)
print("Array is \n", l1)
#Reshaping is changing the dimension of the array but values should not change and 
#the specified dimesion would be perfect to do otherwise will throw error
print("Reshaping the array into 2*4 \n",l1.reshape(4,2))