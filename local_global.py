num1=5 #local variable
def myfun():
    global num1 #global variable
    num1=2
    
    print(num1)

myfun()
print(num1)
# In this case it will give precedence to the local variable whcih is declared inside the function not to the global variable.

