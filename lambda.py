cube=lambda x : x*x*x
print(cube(3))

def lambda_app(fn,value):#you can also pass the  function or lambda function as an argument of function
    return 2+fn(value)
#Lambda is an short hand function which is used for defining the small functions

print(lambda_app(cube,2))
print(lambda_app(lambda x : x*x*x,2))#above and below gets evaluated to same value
