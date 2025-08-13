# Open the file "myself.txt" in read mode ('r')
# This returns a file object, not the file content itself
f = open("myself.txt", 'r') #even if you dont pass the read mode then also it will work as read is default mode

# Print the file object
# This will NOT print the file's content.
# Instead, it prints the default string representation of the file object,
# which usually looks like:
# <_io.TextIOWrapper name='myself.txt' mode='r' encoding='UTF-8'>
# Here:
#   _io.TextIOWrapper → The internal Python class handling the file
#   name='myself.txt' → The file's name
#   mode='r'          → The mode in which the file was opened (read mode)
#   encoding='UTF-8'  → The text encoding Python is using to read the file
print(f)

# If you actually want the file's text content, use:
print(f.read())

f1=open("helloworld.txt",'a')#you can make new file using 'a' mode and 'w' mode if it dont exist and write it using write fn
f1.write("Hello World !")
f1.close() #'a' mode will append the file menas 
#if we are using the open mode then we have to close it to make all the things written in that file means close is mandatory


#with open this will allow to write read or append the file and even if you dont close the file it will close automatically
with open("helloworld.txt",'w') as f:#this mode will remove all the lines and then write from the start

    f.write("Hello World !")

    







