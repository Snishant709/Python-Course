'''
Sets is a collection of well defined object.
Sets are unordered
Sets do not contain duplicate items
Sets are unchangeable means once created you cant change it
Sets can have different data types
Python does not give the same ordered vale in output.The order will chaange everytime.Python does not maintain order of that.
'''
Nishant=set()
print(type(Nishant))#This will print type as set
Sharma={}
print(type(Sharma))#This will print type as dict as Dictionary also starts and ends with {}

mysets={3,4,"Nishant",True,3}
for item in mysets:
    print(item)