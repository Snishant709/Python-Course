'''
Sign of using docstring is ''' ''' three open and closed single inverted commas .
Docstrings are the description about the functions that is not ignored like comments.
It is defined right below the function declartion and just above the function body if it is declared other
than this mentioned format then it is not considered as an docstrings.
Printing the docstrings involves (function_name.__doc__)
'''
def square(n):
    '''It takes one parameter and prints its square'''
    print(f"Square of {n} is {n*n}" )
    

square(3)
print(square.__doc__)

'''
Python enhancement proposal pep8
PEP8 means it will show  Zen of Python which is written by Tim Peteres
which help you know that how your code must be it is an poem to know what is written in PEP8
Use import this command on terminal
'''


