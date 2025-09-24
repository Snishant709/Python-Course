class myclass:
    car="Nano"
    def show(self):
        print(f"Name is {self.name} and comapany is {self.car}")
    @classmethod
    def changecar(cls,newcar):#it will change the class variable
        cls.car=newcar

obj1=myclass()
obj1.name="Nishant"
obj1.show()
obj2=myclass()
obj2.name="Sharma"
obj2.changecar('Tesla')
obj2.show()
print(obj2.car)