# Creating a calculator program using OOP concepts
# Phoebe Rhone L. Gangoso | BSCPE 1-4

import calcu_ui
calcu_ui.Header()

# Pseudocode (main program)
# import operations file
import calcu_operations

# create class calculator
class Calculator:

    # method for instance of operation class
    def __init__(self):
        self.operations = calcu_operations.Operations()

    # method for inputting values and calculation
    def calculation(self):
        try:
            # Ask user to choose and input math operation
            print("\033[0;36m")
            input_operation = input(" Choose one math operation (Addition, Subtraction, Multiplication, Division): ")
            # Ask user to input two numbers
            first_number = float(input("\033[0;35m Enter your first number: "))
            second_number = float(input(" Enter your second number: "))
            # perform calculation using operations
            result_number = self.operations.CalcOperation(first_number, second_number, input_operation)

            if input_operation not in ['Addition', 'Subtraction', 'Multiplication', 'Division']:
                raise ValueError("\033[0;31m Invalid math operation")

            # display result
            calcu_ui.Loading()
            print(" \N{tulip}\033[0;33m Answer:", result_number)

            # ask user if they want to try again or not
            retry_input = input("\033[0;32m Do you want to try again? (Yes/No): ")
            # if yes repeat
            if retry_input == "Yes":
                Calculator.calculation(self)
            else:
                calcu_ui.Exit()
                print("\033[0;33m Thank you for using this calculator!")

        # catch exceptions
        except ValueError as e:
            print(f"\033[0;31m Error:{e}. Please try again.")
            Calculator.calculation(self)
        except ZeroDivisionError:
            print("\033[0;31m Error: Cannot divide by zero. Please try again.")
            Calculator.calculation(self)

# call calculation method
calculator = Calculator()
calculator.calculation()