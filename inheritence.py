#Single Inheritance
class Person:
    def speak(self):
        print("Person can speak")

class Employee(Person):   # Single inheritance
    def work(self):
        print("Employee works")

e = Employee()
e.speak()   # From Person
e.work()    # From Employee


# Multiple inheritance
class Employee:
    def work(self):
        print("Employee works")

class Programmer:
    def code(self):
        print("Programmer codes")

class Man(Employee, Programmer):   # Multiple inheritance
    pass

m = Man()
m.work()   # From Employee
m.code()   # From Programmer


# Multilevel inheritance
class Person:
    def breathe(self):
        print("Person breathes")

class Employee(Person):
    def work(self):
        print("Employee works")

class Programmer(Employee):   # Multilevel
    def code(self):
        print("Programmer codes")

p = Programmer()
p.breathe()   # From Person
p.work()      # From Employee
p.code()      # From Programmer



#Hierarchical Inheritance
class Person:
    def breathe(self):
        print("Person breathes")

class Employee(Person):
    def work(self):
        print("Employee works")

class Student(Person):
    def study(self):
        print("Student studies")

e = Employee()
s = Student()

e.breathe()   # From Person
s.breathe()   # From Person


#Hybrid Inheritance
class Person:
    def breathe(self):
        print("Person breathes")

class Employee(Person):
    def work(self):
        print("Employee works")

class Programmer(Employee):   # Multilevel
    def code(self):
        print("Programmer codes")

class Manager(Person):   # Hierarchical
    def manage(self):
        print("Manager manages")

p = Programmer()
m = Manager()

p.breathe()   # From Person
p.work()      # From Employee
p.code()      # From Programmer
m.manage()    # From Manager
