#A decorator in Python is just a function that
#takes another function as input, adds some extra behavior, and returns a new function.

def greet(func):
    def mainfunc(*args,**kwargs):
        print("Good Morning")
        func(*args,**kwargs)
        print("Thank you for your time")
    return mainfunc

@greet
def hello():
    print("Hello Dear")


hello()
#the baove syntax is same  as below
#greet(hello)()


@greet
def add(n1,n2):
    print(n1+n2)


add(1,2)
#the baove syntax is same  as below
#greet(add)(1,2)

import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b