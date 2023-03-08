import allure
import random
import time


class TestOthers:
    @allure.step
    def passing_step(self):
        # empty
        pass

    @allure.step
    def flaky_broken_step(self):
        if random.randint(1, 5) != 1:
            raise Exception("Broken!")

    def test_broken_with_randomized_time(self):
        self.passing_step()
        time.sleep(random.randint(1, 3))
        self.flaky_broken_step()
