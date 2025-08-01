list1=[31,22,3,34,15]
print(list1)
list1.reverse()#this will not do desc instead print the list from end to start
print("Reverse ",list1)
list1.sort()
'''The sort() method sorts the list in asc in-place and returns None, not the sorted list.
You should either sort first and then print, or use sorted() to return a new sorted list.
If you want to print while applying the function thnen use sorted method'''
print("Asscending order ",list1)
list1.sort(reverse=True)#this will print the list in desc
print("Descending order ",list1)
list2=list1
#This is the bad practice never do this because in future if we change the list2 then it will also effect the list1 also below shown
list1[0]=21#see it will chnage the list1 as well as list2
print("Will change list2 even if you had made changes in list1 beacuse you had used list2=list1 ",list1,list2)
list3=list1.copy()#in this case it will not effect the changes done to list1 as list3 is copy of that
list1[0]=4
print("Copy of list1 ",list3)
list3.append(90)#will insert 90 at the end of the list
print("Append ",list3)
list3.pop()#remove the last element from list if nothing is specified in its index parameter po(2) will remove value on index2
print("Pop ",list3)
print("Print the index of 31 : ",list3.index(31))#
list3.insert(0,21)
print("Inserting 21 on the 0 index of list3 ",list3)
print("Count the number of 21 in list3 : ",list3.count(21))
list3.remove(21)
print("Will remove only one occurrence of 21 ",list3)
list1.extend(list3)
print("list1 gets extended by appending the elements from the list3 ",list1)
list4=list1+list2
print("If you dont want to change the original list then use '+' instead of '.extend() ",list4)
