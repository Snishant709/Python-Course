from functools import reduce

#Remember if you use only map,filter then it will return their object map,filter 
#so you have to type cast it in iterable object like list,tuples
#Map
#The map function applies function to each element in a sequence and returns a new sequence containing the transformed elements. 
cube=lambda x:x*x*x
l=[1,2,3,4,5,4,6]
newl=[]
# for item in l:
#     newl.append(cube(item))
# print(newl)
newl=list(map(cube,l)) #so instead of running loop use map function
#map function takes function or lambda function as an 1st argument and second the iterable object to iterate i.e list,tuple
print(newl)

#Filter
#The filter function filters a sequence of elements based on a given predicate or condtion (a function that returns a boolean 
#value) and returns a new sequence containing only the elements that meet the predicate.
def less_then4(num):
    return num>4
print(list(filter(less_then4,l)))


#Reduce
#The reduce function return as single value and takes two parameters function and the iterable object like list,tuples
result=(reduce(lambda n1,n2 :n1+n2,l))
print(result)
#you have to use  from functools import reduce