'''
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
'''
info = {'name':'Karan', 'age':19, 'eligible':True,'name':'Karan','age':19}
print(info)#will print only distinct values 
#print(info['name2']) if you pass the key which is not their in dict then it will throw error
print(info.get('name2'))#it will not throw error instead prints None
print(info.keys())#all the keys
print(info.values())#all the values
print(info.items())#
for key,value in info.items():#all keys and values in tuples seperated by commas
    print(f"The key {key} corresponds to {value}")


