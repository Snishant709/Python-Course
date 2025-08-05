for i in range(5):
    print(i)
else:
    print("In else block")
#In the above code the else block will be executed as there is no if statement

for i in range(6):
    print(i)
    if i==4:
        break
else:
    print("Else block ")    