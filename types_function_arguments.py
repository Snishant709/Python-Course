def greet(name,age,place):
    print(f"Hello {name}, you are {age} years old and I am from {place}.")



#Positional Arguments (Pass values in order )
greet("Nishant", 25,'Mumbai')

#Keyword Arguments (Specify which parameter gets which value by specifying the variable name)
greet(place='Mumbai', name="Nishant",age=25)

# Default Arguments (Set default value for a parameter if arguments not passed then it will take the deafult parameter value)
def greet(name="Guest"):
    print(f"Hello {name}")

greet()         # Output: Hello Guest (No arguments are given to this function but still it will run)
greet("Zahoor") # Output: Hello Zahoor


#Variable-length Arguments 
# *args (Non-keyworded) (Accepts any number of positional arguments as a tuple)
def total(*numbers):
    print(sum(numbers))

total(10, 20, 30)  # Output: 60



#  **kwargs (Keyworded) (Accepts any number of keyword arguments as a dictionary)
def profile(**info):
    for key, value in info.items():
#The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.
        print(f"{key} = {value}")

profile(name="Nishant", age=25, country="India")


def info2(**profile2):
    for key,value in profile2.items():
        print(f"{key} : {value}")
info2(std="tybscit",year=2025)


