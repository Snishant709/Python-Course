#classes -A class is a blueprint for creating objects.
#objects-An object is an instance of the class.

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






