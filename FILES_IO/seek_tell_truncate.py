with open("helloworld.txt",'r+') as f:
    #f.seek(6) #it starts from 0 , decides from where the pointer of file object should start
    #print(f.tell())#will print the value of seek
    print(f.truncate(6))
    # this will remove the data from the file  specified number passed in argumnet till end ,mode must be in 'w' or 'a' mode  
    print(f.readline())


#r cannot write pointer at 0 only read
#r+ allows you to read and write pointer at 0
#w clears all and starts from 0 cannot read
#w+ useful for reading and writing after can read
#a pointer at last cannot read
#a+ pointer at last can read