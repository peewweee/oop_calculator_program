# Creating a calculator program using OOP concepts
# Phoebe Rhone L. Gangoso | BSCPE 1-4

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
        # Ask user to choose and input math operation
        input_operation = input("Choose one math operation (Addition, Subtraction, Multiplication, Division): ")
        # Ask user to input two numbers
        first_number = 2
        second_number = 4
        # perform calculation using operations
        result_number = self.operations.CalcOperation(first_number, second_number, input_operation)
        # display result
        print("Answer:", result_number)
# call calculation method
calculator = Calculator()
calculator.calculation()