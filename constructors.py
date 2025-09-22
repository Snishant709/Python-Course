#Constructors-This are the special type of methods which are used to initialize the object 
#as they are created.They are of two types default and parameterized
class employee:
    def __init__(self, name=None, department=None):
        if name is None and department is None:
            print("Default Constructor: Object created")
        else:
            self.name = name
            self.department = department
            print(f"Parameterized Constructor: {self.name} works in {self.department}")

        


Nishant=employee()
Sharma=employee("Nishant","IT")