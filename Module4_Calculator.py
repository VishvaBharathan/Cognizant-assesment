import pytest

# -------------------------
# Arithmetic Functions
# -------------------------

def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    if y == 0:
        raise ValueError("Division by zero is not allowed")
    return x / y


# -------------------------
# Fixture
# -------------------------

@pytest.fixture
def values():
    return {"num1": 20, "num2": 10}


# -------------------------
# Test Cases
# -------------------------

def test_addition(values):
    assert addition(values["num1"], values["num2"]) == 30


def test_subtraction(values):
    assert subtraction(values["num1"], values["num2"]) == 10


def test_multiplication(values):
    assert multiplication(values["num1"], values["num2"]) == 200


def test_division(values):
    assert division(values["num1"], values["num2"]) == 2


def test_negative_addition():
    assert addition(-5, -5) == -10


def test_negative_subtraction():
    assert subtraction(-5, -3) == -2


def test_zero_multiplication():
    assert multiplication(10, 0) == 0


def test_decimal_division():
    assert division(7, 2) == 3.5


def test_zero_division():
    with pytest.raises(ValueError):
        division(10, 0)


def test_addition_with_zero():
    assert addition(0, 0) == 0


def test_negative_multiplication():
    assert multiplication(-2, 5) == -10
