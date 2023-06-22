import pytest
from app_t.Calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_adding_negative(self):
        assert self.calc.adding(self, 1, 1) == 3

    def test_multiply(self):
        assert self.calc.multiply_(self, 2,2) == 4

    def test_subtraction(self):
        assert self.calc.subtraction(self, 5, 3) == 2

    def test_division_zero(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def test_division(self):
        assert self.calc.division(self, 121, 11) == 11

    def teardown(self):
        print('Running method Teardown')