class Number:
    def __init__(self,num):
        self.num=num
    
    @staticmethod
    def add(n):
        #return self.num+n 
        #This is not allowed the staic method dont have access to  self attributes 
        return n
    
#You can aslo define the staticmethod outside the class    
@staticmethod
def add(a,b):
    return a+b

obj1=Number(2)
print(Number.add(3))
print(obj1.add(3))
#you can also use static method by passing the name of class & with object also
print(add(5,4))
        
    