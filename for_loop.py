num =int(input("Enter the number till which you have to print the numbers"))
for i in range(num):#end of loop using 1 argument
     print(i)
'''
range(start, stop, step)
start	Optional. An integer number specifying at which position to start. Default is 0
stop	Required. An integer number specifying at which position to stop (not included).
step	Optional. An integer number specifying the incrementation. Default is 1
'''
print("Using two arguments")
for i in range(2,num+1):#using 2 arguments start,stop
    print(i)
    
print("Using three arguments")
for i in range(2,num+1,2):#using 3 arguments start,stop,step
    print(i)
   
