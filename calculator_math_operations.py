# ask user to choose math operations between "Addition", "Subtraction", "Multiplication", or "Division"
math_operator = input("Good day! Please choose what math operation you need: 'Addition', 'Subtraction', 'Multiplication' or 'Division': ")
# evaluate the chosen math operations
math_operator = math_operator.lower()
for i in range(len(math_operator)):

    # if input is "Addition"
    if math_operator == "addition":
        # ask for 2 numbers
        addition_number1 = int(input("Please enter 'First Number': "))
        addition_number2 = int(input("Please enter 'Second 'Number': "))
        # calculate
        addition = addition_number1 + addition_number2
        # display result
        print("The sum is: ", addition)
        break
    # if input is "Subtraction"
    elif math_operator == "subtraction":
        # ask for 2 numbers
        subtraction_number1 = int(input("Please enter 'First Number': "))
        subtraction_number2 = int(input("Please enter 'Second 'Number': "))
        # calculate
        subtraction = subtraction_number1 - subtraction_number2
        # display result
        print("The difference is: ", subtraction)
        break
    # if input is "Multiplication"
    elif math_operator == "multiplication":
        multiplication_number1 = int(input("Please enter 'First Number': "))
        multiplication_number2 = int(input("Please enter 'Second 'Number': "))
        # calculate
        multiplication = multiplication_number1 * multiplication_number2
        # display result
        print("The product is: ", multiplication)
        break
    # if input is "Division"
    elif math_operator == "division":
        try:
            division_number1 = int(input("Please enter 'First Number': "))
            division_number2 = int(input("Please enter 'Second 'Number': "))
            # calculate
            division = division_number1 // division_number2
            # display result
            print("The quotient is: ", division)
            break
        except ZeroDivisionError:
            print("Cannot process division, your divisor is zero")
            break
    # else
    else:
        print("I don't understant your input, please choose one only in the four math operators.")

# ----------------------------------------------
print("-" * 120)
# ask user if wants to input again
math_operator_2 = input("Do you want to calculate again? y/n: ")
    # if yes
    # if no
       # display appreciation