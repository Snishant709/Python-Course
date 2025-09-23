#classes -A class is a blueprint for creating objects.
#objects-An object is an instance of the class.

'''
Four Pillars

1. Encapsulation
Definition:
Encapsulation is the process of binding data (attributes) and methods (functions) that 
operate on that data into a single unit (class). It also involves restricting direct access 
to some of an object’s components, usually through access modifiers 
(public, protected, private).

Abstraction
Definition:
Abstraction means hiding the implementation details and exposing only the essential features 
of an object. In Python, this can be done using abstract classes or methods.

Inheritance
Definition:
Inheritance allows a class (child/derived class) to reuse properties and methods of another
class (parent/base class). This promotes code reusability.

Polymorphism
Definition:
Polymorphism means one name, many forms. It allows objects to take on multiple forms—the 
same function name can be used for different types of objects.


Summary:

Encapsulation → Hides data by bundling it inside a class.

Abstraction → Hides implementation, shows only necessary details.

Inheritance → Reuses code by inheriting from a parent class.

Polymorphism → Same method, different behaviors depending on the object.

'''

class Person:
    name='Nishant'
    roll='6483'
    section='TYIT'

    def info(self):
        print(f'Name is {self.name} , roll is {self.roll} , section  is {self.section}')

a= Person()
print(a.name)
a.info()

b=Person()
b.name='Sharma'
b.info()






