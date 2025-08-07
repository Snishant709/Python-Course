#Enumerate function is used to get the index and value of each element in the list,tuple,string
# index=0
# marks=[2,44,33,56,78,90,89]
# for mark in marks:
#     print(mark)
#     if (index==3):
#         print("You are on middle index")
#     index=index+1

#insetad of writing above code one can use enumerate function

# using it on list
marks=[2,44,33,56,78,90,89]
for index,mark in enumerate(marks):
    print(mark)
    if index==3:
        print("You are on middle index")

#using it on string
words="Nishant"
print("Strings")
for i,str in enumerate(words):
    print(i,str)

#using in tuples
print("Tuples")
tup=(11,2,33,55)
for i,tuples in enumerate(tup):
    print(i,tuples)

