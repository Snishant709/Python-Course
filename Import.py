#Importing in python means loading a code from a module into a current python script
from HelloNishant_import import greetMorning as gm,Nishant as n
#in the above line you are mentioning the functions and variables to import
from HelloNishant_import  import * 
#you can aslo define this to take all the functions and variables used in that module
import HelloNishant_import as hn 
#you can aslo give the whole module an alias and use it by putting dot operator after that alias
import math
gm()
print(n)
print(dir(math))#will show all the functions and variables used in that module in list 
print(type(math.pi))#will print the datatype of the pi

hn.greetMorning()
print(hn.Nishant)

