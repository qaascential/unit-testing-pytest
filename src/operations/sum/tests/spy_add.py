from faker import Faker

fake = Faker()


class SpyAdd:
    def __init__(self):
        self.sum_attributes = {}

    def sum(self, num1, num2):
        self.sum_attributes["num1"] = num1
        self.sum_attributes["num2"] = num2
        return fake.random_number()
