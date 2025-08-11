def greetMorning():
    print("Hello Nishant , Good Morning")

Nishant="Nishant is good boy"
'''
the if __name__ == "__main__" idiom is a common pattern used in Python scripts to determine whether the script is being run 
directly or being imported as a module into another script. It allows you to reuse code from a script by importing it as a 
module into another script, without running the code in the original script.
'''

print(__name__)
if __name__=="__main__":
    greetMorning()

