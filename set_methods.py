s={1,2,5,6}
s2={3,6,7}
print(s.union(s2))#it will do union but will not change the original set
print(s,s2)
print(s.update(s2))#it will print none but it has updated the s1 set so to see it print 's' on below line
print(s)

s3={"Nishant","Bharat","Sharma","Rinki"}
s4={"Nishant","Manu","Bharat"}
print(s3.intersection(s4))#it will do intersection but will not change the original set and prints
s3.intersection_update(s4)#it will updated the s3 set so to see it print 's3' on below line
print(s3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

cities3 = cities.difference(cities2)#elements that are their in cities only not in cities2
print(cities3)

cities3 = cities.symmetric_difference(cities2)#leaving the common element
print(cities3)
#note you can use _update() function after name of operations to make the changes in the original sets

i1={"Nishant"}
i2={"Bharat","Nishant"}
print(i1.isdisjoint(i2))#if any of the element is present and matches with set passed then will Return False else True
print(i2.issuperset(i1))#It returns True if all the items are present, else it returns False.
print(i1.issubset(i2))

i2.add("Manu")#will add the element in set 
print(i2)

print(s3.pop())#will remove any element from set as sets are unordered
print(s3)

s3.clear()#will remove all the items from the set but not delete it
print(s3)

# del s3#will delete the s3 set with all the records
# print(s3) if you print the s3 after this then it will show s3 is not defined

s4.discard("Manu") #it will remove the specified element if not present then dont raise any error it will print none
print(s4)
#s4.remove("Manu")#it will raise error and stop the execution of prorgram






