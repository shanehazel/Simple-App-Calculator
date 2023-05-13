# pseudocode

# make a loop for trying the program again option
while True:

    # ask user for their desired operation
    input_operation = input(str("\033[0;33;40m Choose one operation (Addition, Subtraction, Multiplication, Division): "))

    # check if the inputs are the given operations
    if input_operation.upper() in ("ADDITION","SUBTRACTION", "MULTIPLICATION", "DIVISION"):
        
        # see if the user inputted the correct value
        try:
            input_number1 = float(input("\033[3;34;40m Enter your first number: "))
            input_number2 = float(input("\033[3;32;40m Enter your second number: "))

        # if not, print the error phrase and will make the user type values again
        except ValueError:
            print("\033[1;31;40m Oops! Try inputting numbers only.")
            continue

        # make addition operation
        if input_operation.upper() == "ADDITION":
            operation_addition = input_number1 + input_number2
            print("Your number is", "\033[1;36;40m ==========", operation_addition, "!", "\033[1;36;40m ==========")

        # make subtraction operation
        elif input_operation.upper() == "SUBTRACTION":
            operation_subtraction = input_number1 - input_number2
            print("Your number is", "\033[1;36;40m ==========", operation_subtraction, "!", "\033[1;36;40m ==========")
        
        # make multiplication operation
        elif input_operation.upper() == "MULTIPLICATION":
            operation_multiplication = input_number1 * input_number2
            print("Your number is", "\033[1;36;40m ==========", operation_multiplication, "!", "\033[1;36;40m ==========")

        # make division operation
        elif input_operation.upper() == "DIVISION":
            
            # ask the user if they want the form, decimal or fraction
            division_method = input("\033[0;33;40m Please choose a format (Decimal/Fraction): ")

            # make division operation with decimal answer
            if division_method.upper() == "DECIMAL":
                operation_division = input_number1 / input_number2
                print("Your number is", "\033[1;36;40m ==========", operation_division, "!", "\033[1;36;40m ==========")

            # make division operation with fraction answer
            elif division_method.upper() == "FRACTION":
                operation_division = float(input_number1) / float(input_number2)
                from fractions import Fraction
                def float_to_fraction(number):
                    return Fraction(number).limit_denominator()
                print("Your number is", "\033[1;36;40m ==========", float_to_fraction(float(operation_division)), "!", "\033[1;36;40m ==========")

        # ask the user if they want to calculate again
        input_tryagain = input(str("\033[0;33;40m Do you want to try again? (Yes or No): "))
        
        # if no, break the loop
        if input_tryagain.upper() == "NO":
                print("\033[1;36;40m Thank you!")
                break
        
    # make the user input again if they inputted wrong string