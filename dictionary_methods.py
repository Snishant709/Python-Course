info = {'name':'Karan', 'age':19, 'eligible':True,'name':'Karan','age':19}
print(info.update({'surname':'Sharma'}))#will give none but dict info is updated
print(info)
info.clear()
print(info)#will clear all the items from the dict info 
info.update({'name':'Nishant'})
info.update({'surname':'Sharma'})
print(info)
info.pop('name')#will throw an error if specified key is not present and takes key as argumnet
print(info)
info.update({'name':'Nishant'})
info.update({'surname':'Sharma'})
info.update({'age':21})
info.update({'lives':'Mumbai'})
print(info)
info.popitem()#acts as a pop remove the last item from the list that is last key and value pair
print(info)
#del info   will delete the entire dict info
del info['name']#will delete the key and value for specified key if you give key which is not their then will throw error
print(info)


