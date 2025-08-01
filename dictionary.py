info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
#print(info['name2']) if you pass the key which is not their in dict then it will throw error
print(info.get('name2'))#it will not throw error instead prints None
print(info.keys())#all the keys
print(info.values())#all the values
for key,value in info.items():#all keys and values in tuples 
    print(f"The key {key} corresponds to {value}")
