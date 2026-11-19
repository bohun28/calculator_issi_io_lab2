"""
    Calculator
"""

class Calculator:
    """
        Class Calculator
    """
    def __init__(self, op1:float, op2:float):
        self.op1 = op1
        self.op2 = op2

    def sum(self) -> float:
        """
            Sum of two numbers
        """
        return self.op1 + self.op2

    def subtract(self) -> float:
        """
            Subtract two numbers
        """
        return self.op1 - self.op2

    def multiply(self) -> float:
        """
            Multiply two numbers
        """
        return self.op1 * self.op2

    def divide(self) -> float:
        """
            Divide two numbers
        """
        if self.op2 == 0:
            raise ZeroDivisionError('Division by zero!')
        return self.op1 / self.op2
