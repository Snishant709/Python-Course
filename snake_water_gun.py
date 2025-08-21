import random
score=0
computer_choice=["snake","gun","water"]
player_choice=["snake","gun","water"]
switch = input("Please say 'yes' to start: ").strip().lower()
match switch:
    case 'yes':
        try:
            i=0
            while(True):
                i=i+1
                print(f"\nROUND {i}")
                print("For snake press 0\nFor water press 1\nFor gun press 2")
                p_choice_index=int(input("Enter your choice "))
                if(p_choice_index>3):
                    print("Please enter your choice between 1 and 3")
                    continue
                if(p_choice_index<3 and p_choice_index>=0):
                    p_choice=player_choice[p_choice_index]
                    print("Players choice is ",p_choice)
                c_choice=random.choice(computer_choice)
                if(p_choice_index<3 and p_choice_index>=0):
                    print("Computers Choice is ",c_choice)
                if(p_choice_index<3 and p_choice_index>=0):
                    if(c_choice==p_choice):
                        score=score
                        print("Your score is ",score," because you and computer choose the same object")
                    elif(c_choice=='gun' and p_choice=='water'):
                        score=score+1
                        print("Your score is ",score)
                    elif(c_choice=='snake' and p_choice=='gun'):
                        score=score+1
                        print("Your score is ",score)
                    elif(c_choice=='water' and p_choice=='snake'):
                        score=score+1
                        print("Your score is ",score)
                    else:
                        exit()
        except ValueError:
             print("Please enter integer value between 1 and 3")
        finally:
            print("\nYour final score is ",score)          
    case 'no':
        exit()    
    case _:
        print("Enter valid choice that is 'yes' or 'no' ")    