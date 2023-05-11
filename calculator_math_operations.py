# ask user to choose math operations between "Addition", "Subtraction", "Multiplication", or "Division"
math_operator = input("Good day! Please choose what math operation you need: 'Addition', 'Subtraction', 'Multiplication' or 'Division': ")
# evaluate the chosen math operations
math_operator = math_operator.lower()

def calculator_math_operations():
    while True:
        # if input is in math operator
        if math_operator in ["addition", "subtraction", "multiplication", "division"]:
             # ask for 2 numbers
            first_number = int(input("Please enter 'First Number': "))
            second_number = int(input("Please enter 'Second 'Number': "))
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
            print("Field cannot include non-integer or non-numerical values or be blank.")

# ----------------------------------------------
print("-" * 120)
# ask user if wants to input again
math_operator2 = input("Do you want to calculate again? y/n: ")
# if yes repeat step 1
if math_operator2 == "y":
    calculator_math_operations()
else:
    print("Thank you for using this program! Have a good day!")
# if no
# display appreciation