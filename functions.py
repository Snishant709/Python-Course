'''
Functions are the block of code that is written so that it could be called whenever required
while executing the program.

The terms parameter and argument can be used for the same thing: information that are passed into a function.
From a function's perspective:
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that is sent to the function when it is called.

In python a function is defined using def keyword
'''

def helloWorld():
    print("Hello World")
    
helloWorld()

def passfunction():
    pass #just definning the function not body so use pass keyword to avoid error 



def addition(a,b):
    add=a+b
    return add


print(addition(2,4))
helloWorld()
passfunction()


