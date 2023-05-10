# ask user to choose math operations between "Addition", "Subtraction", "Multiplication", or "Division"
math_operator = input("Good day! Please choose what math operation you need; 'Addition', 'Subtraction', 'Multiplication' or 'Division'")
# evaluate the chosen math operations
for i in range(len(math_operator)):
    # if input is "Addition"
    math_operator = math_operator.lower()
    if math_operator == "addition":
        # ask for 2 numbers
        addition_number1 = input("Please enter 'First Number': ")
        addition_number2 = input("Please enter 'Second 'Number': ")
        # calculate
        addition = addition_number1 + addition_number2
        # display result
        print("The sum is: ", addition)
    # if input is "Subtraction"
        # ask for 2 numbers
        # display result
    # if input is "Multiplication"
            # ask for 2 numbers
        # display result
    # if input is "Division"
        # ask for 2 numbers
        # display result
# ----------------------------------------------
# ask user if wants to input again
    # if yes
    # if no
       # display appreciation