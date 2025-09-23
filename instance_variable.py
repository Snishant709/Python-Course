class Department:
    no_employees=0#it is class instance not the var
    def __init__(self,name):
        self.name=name#instance variable
        self.no_employees+=1
    def show(self):
        print(f"Name of the Employee is {self.name} and joining number is {self.no_employees}")
        

obj1=Department("Nishant")
obj1.show()


obj2=Department("Sharma")
obj2.no_employees=4 
#the above wont throw eroor but it wont update as it is instance variable
Department.no_employees=4#This will work
obj2.show()