#strings are immutable they dont change once declared 
name="!!!!Nishant!!!!Nishant!!!!"
surname="Sharma !! ,,"
print(name.upper()) # will convert the whole string into Upper case
print(name.lower()) # will convert the whole string into Lower case
print(name.strip("!"))#will remove the specified parameter from left and right 
print(name.lstrip("!"))#will remove the specified parameter from left
print(name.rstrip("!"))#will remove the specified parameter from right 
print(name.replace("Nishant","Sharma"))#will replace the first parameter with the secod parameter   
print(surname.split(" "))#split will make a list
heading="THis is about me"
print(heading.capitalize())# it will only make the first letter to Capital remaining all the characters into small
print(len(heading))
print(heading.center(50),len(heading.center(50)))#it will add the spaces to specifid limit given in parameter 
print(heading.count("is"))
print(heading.endswith("."))#return boolean value
print(heading.endswith("e",5,len(heading)))#return boolean value you can also specify the limits from where to start checking
print(heading.find("o")) #prints the index of the seraching parameter if their and if not then -1
print(heading.find("wo")) #prints the index of the seraching parameter if their and if not then -1
print(heading.index('o'))# prints the index of the seraching parameter if their and if not then raises error
#print(heading.index('wo'))# prints the index of the seraching parameter if their and if not then raises error substring not found

checking="abc 1234 "
#below all functions will check the whole string or input 
print(checking.isalnum()) #checks A-Z ,a-z ,0-9 
print(checking.isalpha()) #checks A-Z ,a-z
print(checking.isnumeric()) #checks 0-9
print(checking.isprintable())
print(checking.isspace())#if in the string their is only space then only it will return True if in between then false
print(heading.title())#will capitalize every first letter followed by all letters in small
print(heading.istitle())# it will check that each word starts with capital letter followed by small letters
print(heading.swapcase())#will make small character upper and vice a versa
print(heading.startswith("h"))







