# ask user to choose math operations between "Addition", "Subtraction", "Multiplication", or "Division"
math_operator = input("Good day! Please choose what math operation you need; 'Addition', 'Subtraction', 'Multiplication' or 'Division': ")
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
        subtraction = subtraction_number1 - subtraction_number2
        # display result
        print("The difference is: ", subtraction)
    # if input is "Multiplication"
    elif math_operator == "multiplication":
        multiplication_number1 = int(input("Please enter 'First Number': "))
        multiplication_number2 = int(input("Please enter 'Second 'Number': "))
        # calculate
        multiplication = multiplication_number1 * multiplication_number2
        # display result
        print("The product is: ", multiplication)
    # if input is "Division"
    elif math_operator == "division":
        division_number1 = int(input("Please enter 'First Number': "))
        division_number2 = int(input("Please enter 'Second 'Number': "))
        # calculate
        division = division_number1 / division_number2
        # display result
        print("The quotient is: ", division)
    # else
    else:
        print("I don't understant your input, please choose one only in the four math operators.")
# ----------------------------------------------
# ask user if wants to input again
    # if yes
    # if no
       # display appreciation