'''
List is a collection which is ordered and changeable.
List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc.
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
If you add new items to a list, the new items will be placed at the end of the list.
A list can have different data types in a single list
'''

list1=[1,2,3,'Nishant',[1,2,3,4],True,8,9,7]
print(len(list1))
print(list1[-3])
#the above print statement is  nothing but list1[len(list1)-3]=list1[3]

if 4 in list1:#this will print no as 4 is their in the inner list 
    print("Yes")
else:
    print("No")


if "Nishant" in list1:
    print("Yes")

if "nit" not in "Nishant":#You can also validate the string is their or not
    print("Yes")
    
print(list1[:])#in this case python will take 0 before ':' and len(variable) after ':' by deafult
print(list1[::2])#Stop and Step is exclusive 
print(list1[::3])
#print(list1[::0])step cannot be zero it will throw error
#List Comprehension
#It is  used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.
list2= [i for i in range(10)]
print(list2)
list2= [i*i for i in range(10)]
print(list2)
list2= [i*i for i in range(10) if i%2==0]
print(list2)


names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)
namesWith_4=[item for item in names if len(item)>4]
print(namesWith_4)


    