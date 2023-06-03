# Calculator using Inheritance Concepts
# Phoebe Rhone L. Gangoso | BSCPE 1-4

# Pseaudocode
# Creating class
class CalculatorPhoebe:
    from calcu_operations import Operations
    def CalcOperation(self, first_number, second_number, input_operation):
        # if exponents
        if input_operation == "Exponents":
            return first_number ** second_number