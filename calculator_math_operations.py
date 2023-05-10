# ask user to choose math operations between "Addition", "Subtraction", "Multiplication", or "Division"
math_operator = input("Good day! Please choose what math operation you need; 'Addition', 'Subtraction', 'Multiplication' or 'Division'")
# evaluate the chosen math operations
for i in range(len(math_operator)):
    # if input is "Addition"
    math_operator = math_operator.lower()
    if math_operator == "addition":
        # ask for 2 numbers
        addition_number1 = int(input("Please enter 'First Number': "))
        addition_number2 = int(input("Please enter 'Second 'Number': "))
        # calculate
        addition = addition_number1 + addition_number2
        # display result
        print("The sum is: ", addition)
    # if input is "Subtraction"
    elif math_operator == "subtraction":
        # ask for 2 numbers
        subtraction_number1 = int(input("Please enter 'First Number': "))
        subtraction_number2 = int(input("Please enter 'Second 'Number': "))
        # calculate
        # display result
    # if input is "Multiplication"
        # ask for 2 numbers
        # calculate
        # display result
    # if input is "Division"
        # ask for 2 numbers
        # calculate
        # display result
    # else
    else:
        print("I don't understant your input, please choose one only in the four math operators.")
# ----------------------------------------------
# ask user if wants to input again
    # if yes
    # if no
       # display appreciation