import numpy as np
l = [[1,2,3,4,5,6,7,8]]
l1 = np.array(l)
print("Array is \n", l1)
#Reshaping is changing the dimension of the array but values should not change and 
#the specified dimesion would be perfect to do otherwise will throw error
#Note reshapping never returns the copy it returns the view means the actual  data changes
print("Reshaping the array into 2*4 \n",l1.reshape(4,2))

#now converting the 2d or multi dimension array into 1d array
l2 = [[1,2,3,4],[5,6,7,8]]
arr = np.array(l2)
print("Converting the 2d arr into 1d array which will return view",arr.ravel())
print("Converting the 2d arr into 1d array which will copy ",arr.flatten())
