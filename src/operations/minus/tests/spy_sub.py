from faker import Faker

fake = Faker()


class SpySub:
    def __init__(self):
        self.minus_attributes = {}

    def minus(self, num1, num2):
        self.minus_attributes["num1"] = num1
        self.minus_attributes["num2"] = num2
        return fake.random_number()
