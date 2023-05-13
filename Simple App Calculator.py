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

        # make subtraction operation
        
        # make multiplication operation

        # make division operation

            # ask the user if they want the form, decimal or fraction

            # make division operation with decimal answer

            # make division operation with fraction answer

        # ask the user if they want to calculate again

        # if no, break the loop
    
    # make the user input again if they inputted wrong string