print("Let's start KBC! Are you ready?")
switch = input("Please say 'yes' to start: ").strip().lower()

options = [15, 26, "Delhi", "Mumbai"]
count = 0

if switch == "yes":
    # Q1
    print("Here is the first question: What is the capital of India?")
    print("1:", options[0], "2:", options[1], "3:", options[2], "4:", options[3])
    answer1 = int(input("Enter option number (1-4): "))
    if options[answer1 - 1] == "Delhi":
        count += 1
    else:
        print("Oops,", options[answer1 - 1], "was not the right answer.")
        print("Your final score is", count)
        exit()

    # Q2
    print("Second question: When did India get independence?")
    print("1:", options[0], "2:", options[1], "3:", options[2], "4:", options[3])
    answer2 = int(input("Enter option number (1-4): "))
    if options[answer2 - 1] == 15:
        count += 1
    else:
        print("Oops,", options[answer2 - 1], "was not the right answer.")
        print("Your final score is", count)
        exit()

    # Q3
    print("Third question: When is Republic Day celebrated?")
    print("1:", options[0], "2:", options[1], "3:", options[2], "4:", options[3])
    answer3 = int(input("Enter option number (1-4): "))
    if options[answer3 - 1] == 26:
        count += 1
    else:
        print("Oops,", options[answer3 - 1], "was not the right answer.")
        print("Your final score is", count)
        exit()

    # Q4
    print("Fourth question: What is the financial capital of India?")
    print("1:", options[0], "2:", options[1], "3:", options[2], "4:", options[3])
    answer4 = int(input("Enter option number (1-4): "))
    if options[answer4 - 1] == "Mumbai":
        count += 1
    else:
        print("Oops,", options[answer4 - 1], "was not the right answer.")
        print("Your final score is", count)
        exit()

    # Final score
    print("Congratulations! You answered all correctly.")
    print("Your final score is", count)

else:
    print("Game not started. Please enter 'yes' next time.")
