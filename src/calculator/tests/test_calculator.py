from faker import Faker
from src.calculator.calculator import Calculator
from src.operations.sum.tests.spy_add import SpyAdd
from src.operations.minus.tests.spy_sub import SpySub

fake, add_operation, sub_operation = Faker(), SpyAdd(), SpySub()
calculator = Calculator(add_operation, sub_operation)


class TestCalculator:
    def test_add():
        num1, num2 = fake.random_number(), fake.random_number()
        result = calculator.sum(num1, num2, True)
        # Input Testing
        assert add_operation.sum_attributes["num1"] == num1
        assert add_operation.sum_attributes["num2"] == num2
        # Output Testing
        assert result is not None

    def test_add(bool=False):
        num1, num2 = fake.random_number(), fake.random_number()
        result = calculator.sum(num1, num2, bool)
        # Input Testing
        assert add_operation.sum_attributes == {}
        # Output Testing
        assert result is None

    def test_sub():
        num1, num2 = fake.random_number(), fake.random_number()
        result = calculator.minus(num1, num2, True)
        # Input Testing
        assert sub_operation.minus_attributes["num1"] == num1
        assert sub_operation.minus_attributes["num2"] == num2
        # Output Testing
        assert result is not None

    def test_sub(bool=False):
        num1, num2 = fake.random_number(), fake.random_number()
        result = calculator.minus(num1, num2, bool)
        # Input Testing
        assert sub_operation.minus_attributes == {}
        # Output Testing
        assert result is None
