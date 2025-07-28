i=int(input("Enter number "))
while(i<20):
    print(i)
    i=i+1
    
'''
In python we do not have do while loop 
'''

#Implementation of do while loop
while True:
    num = int(input("Enter a positive number: "))
    
    if num > 0:
        print("Thank you!")
        break
    else:
        print("Try again.")
