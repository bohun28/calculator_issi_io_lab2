import pytest

from calculator import Calculator

"""
    Test calculator
"""

class TestCalculator():
    """
        Class TestCalculator
    """
    def test_add(self):
        """
            Test addition
        """
        calculator = Calculator(1, 2)
        assert calculator.sum() == 3

    def test_sub(self):
        """
            Test subtraction
        """
        calculator = Calculator(1, 2)
        assert calculator.subtract() == -1

    def test_multiply(self):
        """
            Test multiplication
        """
        calculator = Calculator(1, 2)
        assert calculator.multiply() == 2

    def test_divide(self):
        """
            Test division
        """
        calculator = Calculator(1, 2)
        assert calculator.divide() == 0.5

    def test_divide_by_zero(self):
        """
            Test division by zero
        """
        calculator = Calculator(1, 0)
        with pytest.raises(ZeroDivisionError):
            calculator.divide()
