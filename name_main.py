'''
Even if you write the name of module and import it then also if the function is declared outside the main function then it will
get executed even if you dont call it which is wrong so to avoid that make sure that all the functions are callled inside the
main function to avoid it to run autommatically 
'''
import HelloNishant_import as h1
print(__name__)
h1.greetMorning()