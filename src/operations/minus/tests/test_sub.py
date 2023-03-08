import allure
from src.operations.minus.sub import Sub


class TestSub:
    @allure.title("This test is about sub operation")
    @allure.step
    @allure.epic("epic_1")
    @allure.feature("feature_2")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_minus(self):
        assert Sub().minus(4, 4) == 1
