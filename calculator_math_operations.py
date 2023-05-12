# display start of program
print("Good day! This program is a simple calculator.")
def calculator_math_operations():
    while True:
        # ask user to choose math operations between "Addition", "Subtraction", "Multiplication", or "Division"
        math_operator = input("Please choose what math operation you need: 'Addition', 'Subtraction', 'Multiplication' or 'Division': ")
        # evaluate the chosen math operations
        math_operator = math_operator.lower()
        # if input is in math operator
        if math_operator in ["addition", "subtraction", "multiplication", "division"]:
            try:
                first_number = int(input("Please enter 'First Number': "))
                second_number = int(input("Please enter 'Second 'Number': "))
            except ValueError:
                print("Field cannot include non-integer or non-numerical values or be blank.")
                break
            if math_operator == "addition":
                # calculate
                addition = first_number + second_number
                # display result
                print("The sum is: ", addition)
            # if input is "Subtraction"
            elif math_operator == "subtraction":
                # calculate
                subtraction = first_number - second_number
                # display result
                print("The difference is: ", subtraction)
            # if input is "Multiplication"
            elif math_operator == "multiplication":
                # calculate
                multiplication = first_number * second_number
                # display result
                print("The product is: ", multiplication)
            # if input is "Division"
            elif math_operator == "division":
                try:
                    # calculate
                    division = first_number // second_number
                except ZeroDivisionError:
                    print("Cannot process division, your divisor is zero")
                # display result
                else:
                    print("The quotient is: ", division)
        
        # else
        else:
            print("I don't understant your input, please choose one only in the four math operators.")
            break
        
        # decision statement
        math_operator_2 = (input("Do you want to calculate again? y/n: "))
        if math_operator_2 == "y":
            continue
        elif math_operator_2 == "n":
            print("Thank you for using this program. Have a Good day!")
            break
        else:
            print("Please choose 'y' only if yes or 'n' only if no")
            break
            
# ----------------------------------------------
calculator_math_operations()
