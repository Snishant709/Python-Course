import numpy as np
l = [[1,2,3,4,5,6,7,8]]
l1 = np.array(l)
print("Array is \n", l1)

# indexing
print("Indexing:", l1[0][2])    

# slicing
print("Slicing:", l1[0][0:3])    

# fancy indexing
print("Fancy Indexing:", l1[0, [0, 3, 2]])  

# conditional filtering
print("Conditional Filtering:", l1[l1 > 2])
