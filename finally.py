'''
The finally block lets you execute code, regardless of the result of the try- and except blocks.
The main thing is that finally block will execute even you write the
'''
def finally_function():
    try:
        print("Enter index to know number at that index")
        i = int(input())
        l = [22, 13, 54, 75]
        print(f"Number at index {i} is {l[i]}")
        return 1
    except:
        print("Some error occurred")
        return 0
    finally:
        print("Finally block will execute even after return statement")

finally_function()