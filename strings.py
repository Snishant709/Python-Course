#In python anything you pass in single codes or double codes both are considered as an string
# In python strings are immutable 
name="Nishant"
surname="Sharma"
print(name+" "+surname)
print(name[0])
# it will throw an error as array index out of bound print(name[10])
# if i want to write a multiline then i have to use the escape sqe or i have to use triple singlecodes or triple double codes
str='''My name is Nishant Bharat Sharma
My age is 21
'''
print(str)
for characters in str:
    print(characters)
