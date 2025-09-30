import numpy as np
#vstack and hstack 

l3 = [[1,2]]
arr3 = np.array(l3)
l4 = [[7,8]]
arr4 = np.array(l4)
print("Horizontal stacking is \n",np.hstack((arr3,arr4)))
print("Vertical stacking is \n",np.vstack((arr3,arr4)))


#spliting the array
arr =np.array( [1,2,3,4,5,6,7,8])
arr1 =np.array( [[1,2,3,4],[5,6,7,8]])
print("spliting the array in 2 equal parts ",np.split(arr,4))
print("spliting the array in 2 equal parts using hsplit",np.hsplit(arr,4))
#print("spliting the array in 2 equal parts using vsplit ",np.vsplit(arr,4))#it will throw error as the vsplit requires 2d array

print("spliting the array in 2 equal parts using vsplit \n",np.vsplit(arr1,1))#it will throw error as the vsplit requires 2d array

