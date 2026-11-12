import pytest
import calculator


def test_calculator_sum():
    calc = calculator.Calculator(2,3)
    assert calc.sum() == 5

def test_calculator_subtract():
    calc = calculator.Calculator(2,3)
    assert calc.subtract() == -1

def test_calculator_multiply():
    calc = calculator.Calculator(2,3)
    assert calc.multiply() == 6

def test_calculator_divide():
    calc = calculator.Calculator(6,3)
    assert calc.divide() == 2

def test_calculator_divide_by_zero():
    calc = calculator.Calculator(6,0)
    with pytest.raises(ZeroDivisionError):
        calc.divide()