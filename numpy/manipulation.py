import numpy as np
l2 = [[1,2],[3,4]]
arr = np.array(l2)


#you can insert values by specifying the index number and values based on the axis
print(np.insert(arr,1,[9,10],axis=1))#column wise
print(np.insert(arr,1,[9,10],axis=0))#row wise
print(np.insert(arr,2,[9,10]))#flatten or series wise

#append the array
l2 = [[1,2]]
arr2 = np.array(l2)
print("Appended array is ",np.append(arr2,[3,4]))

#concatenate two array
l3 = [[1,2]]
arr3 = np.array(l3)
l4 = [[7,8]]
arr4 = np.array(l4)
print("Concatenate horizontally\n",np.concatenate((arr3,arr4),axis=1))#horizontal stacking
print("Concatenate vertically\n",np.concatenate((arr3,arr4),axis=0))#vertical stacking


#deleting 1d array element
l5 = [[4,5]]
arr5 = np.array(l5)
print("Array befor the delete operation ",arr5)
print("Deleting the 1d array element present at the index 1 ",np.delete(arr5,1))


#deleting the 2d array element
print("Array befor the delete operation \n",arr)
print("Deleting the 2d array element present at the index 2 \n",np.delete(arr,2))




