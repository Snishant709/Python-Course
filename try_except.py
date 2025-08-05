'''
The try block lets you test a block of code for errors.
The except block lets you handle the error.
'''

try:
    print("Enter the index number to serach for ")
    n=int(input())
    a=[2,5]
    print(f'Number at {n} index is {a[n]}')
except ValueError as v:
    print(v)
except IndexError as i:
    print(i)
    
    