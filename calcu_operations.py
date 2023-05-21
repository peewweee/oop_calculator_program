# Creating a calculator program using OOP concepts
# Phoebe Rhone L. Gangoso | BSCPE 1-4

# Pseudocode (operations class)
# create class operations
class Operations:
    def CalcOperation(self, first_number, second_number, input_operation):
    # if addition
        if input_operation == "Addition":
            return first_number + second_number
    # if subtraction
        if input_operation == "Subtraction":
            return first_number - second_number
    # if multi
        if input_operation == "Multiplication":
            return first_number * second_number
    # if divi
        if input_operation == "Division":
            return first_number / second_number