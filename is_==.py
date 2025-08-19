#is used to compare the identity of the object or address if the two variables are immumtable then it will return True else fale 
#== used to compare the values of variable   

a=3
b=3
print(a is b)
#it will print True as 3 and 3 both are immumtable as well as same so  will dont waste memory for storing it at different address
print(a==b)


a=4
b=67
print(a is b)
#it will print True as 4 and 27 both are immumtable but not same so  will store at different address
print(a==b)

a=[1,2,3]
b=[1,2,3]
print(a is b)#list are mutable so it will use different location for storing
print(a==b)

a="a"
b="a"
print(a is b)#strings are immutable so it will use same location for storing
print(a==b)

a=(2,4,5)
b=(2,4,5)
print(a is b)
#tuples are immutable so it will use same location for storing but if any value gets changed then it will say False i.e b=(2,4,6)
print(a==b)