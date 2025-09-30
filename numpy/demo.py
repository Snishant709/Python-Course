import numpy as np

#using lists and loop for calc average
l1=[1,2,3,4,5]
total=0
for temp in l1:
    total+=temp
print("Average temperature is ",total/len(l1))

#using numpy library without using the loop and list approach intead using array for big data
arr=np.array(l1)
avg=np.mean(arr)
print("Average using numpy library mean method is ",avg)

