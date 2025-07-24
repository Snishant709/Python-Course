name="Nishant"
print(len(name))
print(name[0:1])
print(name[:])#if you wont specif the parameter it will take first as 0 and last as length of a string 
print(name[len(name)-1:len(name)-3]) 
print(name[-1:-3])# this will not print anything as it starts from 6 and ends on 4 
print(name[-7:-2])


# string slicing takes two parameteres frm where to start and where to end 