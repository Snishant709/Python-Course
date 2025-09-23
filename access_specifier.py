#In python there is no such access modifiers unlike other programming languages but 
#through convention '_' is used to depict protected '__' is used to depict private 
# and '.' without underscore is used to depict that it is public

class Person:
    def __init__(self,name,salary):
        self._name=name
        self.__salary=salary

class Employee(Person):
    def show(self):
        print(f"Name of the Employee is {self._name}")

obj1=Employee("Nishant",20000)
obj1.show()
print(dir(obj1))#It will print all the functions and variables that the object have
print(obj1._Person__salary) #This technique you have to use to access pricate attributes



        
        


