# ask user to choose math operations between "Addition", "Subtraction", "Multiplication", or "Division"
math_operator = input("Good day! Please choose what math operation you need: 'Addition', 'Subtraction', 'Multiplication' or 'Division': ")
# evaluate the chosen math operations
math_operator = math_operator.lower()
# ask for 2 numbers
first_number = int(input("Please enter 'First Number': "))
second_number = int(input("Please enter 'Second 'Number': "))
for i in range(math_operator):
    # if input is "Addition"
    if math_operator == "addition":
        # calculate
        addition = first_number + second_number
        # display result
        print("The sum is: ", addition)
    # if input is "Subtraction"
    elif math_operator == "subtraction":
        # calculate
        subtraction = subtraction_number1 - subtraction_number2
        # display result
        print("The difference is: ", subtraction)
    # if input is "Multiplication"
    elif math_operator == "multiplication":
        # calculate
        multiplication = multiplication_number1 * multiplication_number2
        # display result
        print("The product is: ", multiplication)
    # if input is "Division"
    elif math_operator == "division":
        try:
            # calculate
            division = division_number1 // division_number2
            # display result
            print("The quotient is: ", division)
        except ZeroDivisionError:
            print("Cannot process division, your divisor is zero")
    # else
    else:
        print("I don't understant your input, please choose one only in the four math operators.")

# ----------------------------------------------
print("-" * 120)
# ask user if wants to input again
# if yes repeat step 1
# if no
   # display appreciation