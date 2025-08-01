'''
F-strings are formatted string literals introduced in Python 3.6 that allow variables and expressions to be embedded directly 
in strings using {}. They're faster, more readable, and cleaner compared to .format() or % formatting.
'''
name="Nishant"
num=23.53454534
print(f"My name is {name}")
print(f"My name is {{name}}")#if you want to use '{}' curley braces while printing
print(f"2*3 = {2*3}")
print(f"{num:.2f}")
#Before fstring format was used for printing the vaiable value