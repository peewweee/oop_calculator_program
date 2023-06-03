# Calculator using Inheritance Concepts
# Phoebe Rhone L. Gangoso | BSCPE 1-4
from calcu_operations import Operations
# Pseaudocode
# Creating class
class CalculatorPhoebe(Operations):
    # if exponents
    def Power(self,  first_number, second_number, input_operation):
        if input_operation == "Exponents":
            return first_number ** second_number
        else:
            return Operations.CalcOperation(self, first_number, second_number, input_operation)