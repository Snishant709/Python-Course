cases=int(input("Please enter your choice between 1 to 3 : "))
match cases:
    case 1:
        print("You matched the case 1")
    case 2:
        print("You matched the case 2")
    case 3:
        print("You matched the case 3")
    case _ if cases==0:
        print(f"Please enter the valid choice you had entered {cases}")
    case _:
        print("Please enter the valid choice between 1 and 3")
                
                
'''
You can aslo use the if and else ladder in the deafult case also the default case is 
'_' and yes their is no use of break statement in python as it assusmes after each case
their is a break unlike C,C++
'''
        