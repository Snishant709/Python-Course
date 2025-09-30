import numpy as np
l3 = [[1,2]]#(1,2)
arr3 = np.array(l3)
l4 = [[7,8]]#(1,2)
arr4 = np.array(l4)
l5 = [[7,8,9]]#(1,3)
arr5 = np.array(l5)
print("Multiplication of arr3 and arr4 is ",arr3*arr4)#element wise multiplication 
print("Multiplication of arr4 and arr5 is ",arr4*arr5)#this will throw error as the dimensions are not same 

