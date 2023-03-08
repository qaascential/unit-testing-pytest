import allure
from faker import Faker
from src.operations.sum.add import Add

fake = Faker()


class TestAdd:
    @allure.title(f"This test is about add operation")
    @allure.step
    @allure.epic("epic_1")
    @allure.feature("feature_1")
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_sum(self):
        num1, num2 = fake.random_number(), fake.random_number()
        expected = num1 + num2
        result = Add().sum(num1, num2)
        assert expected == result
