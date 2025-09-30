import numpy as np
l5 = [[7,8,9,np.nan,np.nan]]#dont write None here it wont work
arr5 = np.array(l5)
print(np.isnan(arr5))#evaluates True and False for whole array
#replace the nan with 50
print("Replace the nan value with any value you want ",np.nan_to_num(arr5,nan=50))

l6 = [[7,8,9,np.inf,-np.inf]]#dont write None here it wont work
arr6 = np.array(l6)
print("Evaluate True or False if it is infinity ",np.isinf(arr6))


print("Replace the infinite value with ",np.nan_to_num(arr6,posinf=8,neginf=-8))


