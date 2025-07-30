'''
Tuple items are ordered, unchangeable, and allow duplicate values.
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
Can store different types of data types
'''
t1=(1,2,3)
print(type(t1))

t2=(5)#will print type as int as their is one element then python get confused 
print(type(t2))

t3=(7,)#so put ',' after single item then it will give tuple
print(type(t3))

country = ("Spain", "Italy", "India", "England", "Germany")
#            [0]      [1]      [2]       [3]        [4]
print(country[-1]) # Similar to print(country[len(country) - 1])
print(country[-3])
print(country[-4])

if "Germany" in country:
    print("Yes Germany is present")
    
    
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[::2])     #using positive indexes
print(animals[-8:-1:2]) #using negative indexes

animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[1:8:3])


    
