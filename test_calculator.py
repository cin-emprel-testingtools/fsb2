import pytest
from calculator import Calculator

class TestCalculator():
    
    def test_addition(self):
        self.calc = Calculator()
        assert self.calc.addition(2,2) == 4
    
    def test_subtraction(self):
        self.calc = Calculator()
        assert self.calc.subtraction(10,1) == 9, "Esperava 3, mas o resultado foi {}".format(self.calc.subtraction(10,1))
    
    def test_multiplication(self):
        self.calc = Calculator()
        assert self.calc.multiplication(3,4) == 12
    
    def test_division(self):
        self.calc = Calculator()
        assert self.calc.division(10,2) == 5

    def test_division_by_zero(self):
        self.calc = Calculator()
        with pytest.raises(ZeroDivisionError):
            self.calc.division(10,0)