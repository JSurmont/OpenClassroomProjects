import pytest

from calculate.operators import Operators


@pytest.mark.parametrize("calculation, result", [("5.5 + 10", 15.5), ("2 + 2 + 10", 14), ("4.8 + 5", 9.8)])
def test_should_make_addition(calculation, result):
    sut = Operators()
    operation = calculation
    expected_value = result
    assert sut.addition(operation) == expected_value


def test_should_make_multiple_addition():
    sut = Operators()
    operation = "5.5 + 10 + 30 + 13.7"
    expected_value = 59.2
    assert sut.addition(operation) == expected_value


@pytest.mark.parametrize("calculation, result", [("5.5 - 10", None), ("2 + 2 * 10", None)])
def test_should_not_make_addition_and_return_none_with_wrong_operator(calculation, result):
    sut = Operators()
    operation = calculation
    expected_value = result
    assert sut.addition(operation) == expected_value


def test_should_not_make_addition_and_return_none_with_wrong_operation():
    sut = Operators()
    operation = "5.5 + 10 - 2"
    expected_value = None
    assert sut.addition(operation) == expected_value


def test_should_not_make_addition_and_return_none_with_non_digit_value():
    sut = Operators()
    operation = "5.5 + 10 + A"
    expected_value = None
    assert sut.addition(operation) == expected_value


@pytest.mark.parametrize("calculation, result", [("5.5 - 10", -4.5), ("10 - 3 - 2", 5), ("5 - 5", 0)])
def test_should_make_subtraction(calculation, result):
    sut = Operators()
    operation = calculation
    expected_value = result
    assert sut.subtraction(operation) == expected_value


def test_should_make_multiple_subtraction():
    sut = Operators()
    operation = "5.5 - 10 - 30 - 13.7"
    expected_value = -48.2
    assert sut.subtraction(operation) == expected_value


@pytest.mark.parametrize("calculation, result", [("5.5 + 10", None), ("2 - 2 * 10", None)])
def test_should_not_make_subtraction_and_return_none_with_wrong_operator(calculation, result):
    sut = Operators()
    operation = calculation
    expected_value = result
    assert sut.subtraction(operation) == expected_value


def test_should_not_make_subtraction_and_return_none_with_wrong_operation():
    sut = Operators()
    operation = "5.5 - 10 + 2"
    expected_value = None
    assert sut.subtraction(operation) == expected_value


def test_should_not_make_subtraction_and_return_none_with_non_digit_value():
    sut = Operators()
    operation = "5.5 - 10 - A"
    expected_value = None
    assert sut.subtraction(operation) == expected_value


@pytest.mark.parametrize("calculation, result", [("5.5 * 10", 55), ("100 * 2 * 4", 800), ("4.8 * 5", 24)])
def test_should_make_multiplication(calculation, result):
    sut = Operators()
    operation = calculation
    expected_value = result
    assert sut.multiplication(operation) == expected_value


def test_should_make_multiple_multiplication():
    sut = Operators()
    operation = "5.5 * 10 * 30 * 13.7"
    expected_value = 22605.0
    assert sut.multiplication(operation) == expected_value


@pytest.mark.parametrize("calculation, result", [("5.5 + 10", None), ("2 * 2 / 10", None)])
def test_should_not_make_multiplication_and_return_none_with_wrong_operator(calculation, result):
    sut = Operators()
    operation = calculation
    expected_value = result
    assert sut.multiplication(operation) == expected_value


def test_should_not_make_multiplication_and_return_none_with_wrong_operation():
    sut = Operators()
    operation = "5.5 * 10 + 2"
    expected_value = None
    assert sut.multiplication(operation) == expected_value


def test_should_not_make_multiplication_and_return_none_with_non_digit_value():
    sut = Operators()
    operation = "5.5 * 10 * A"
    expected_value = None
    assert sut.multiplication(operation) == expected_value


@pytest.mark.parametrize("calculation, result", [("5.5 / 10", 0.55), ("100 / 2 / 10", 5), ("5 / 5", 1)])
def test_should_make_division(calculation, result):
    sut = Operators()
    operation = calculation
    expected_value = result
    assert sut.division(operation) == expected_value


def test_should_make_multiple_division():
    sut = Operators()
    operation = "5.5 / 10 / 10"
    expected_value = 0.055
    assert sut.division(operation) == pytest.approx(expected_value)


def test_should_not_make_division_and_return_none_with_denominator_zero():
    sut = Operators()
    operation = "5.5 / 0"
    expected_value = None
    assert sut.division(operation) == expected_value


@pytest.mark.parametrize("calculation, result", [("5.5 + 10", None), ("2 / 2 + 10", None)])
def test_should_not_make_division_and_return_none_with_wrong_operator(calculation, result):
    sut = Operators()
    operation = calculation
    expected_value = result
    assert sut.division(operation) == expected_value


def test_should_not_make_division_and_return_none_with_wrong_operation():
    sut = Operators()
    operation = "5.5 / 10 + 2"
    expected_value = None
    assert sut.division(operation) == expected_value


def test_should_not_make_division_and_return_none_with_non_digit_value():
    sut = Operators()
    operation = "5.5 / 10 / A"
    expected_value = None
    assert sut.division(operation) == expected_value
