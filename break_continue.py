print("implementation of break")    
num=5
for i in range(1,15):
    print("5 x",i,"=",5*i)
    if i==8:
        break
    
for i in range(9):
  if i == 3:
    continue
  print(i)
        
'''
The break keyword is used to break out a for loop, or a while loop.
The continue keyword is used to end the current iteration in a for loop (or a while loop), and continues to the next iteration.
'''