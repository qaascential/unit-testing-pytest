class Calculator:
    def __init__(self, add, sub):
        self.add = add
        self.sub = sub

    def sum(self, num1, num2, op):
        if op:
            return self.add.sum(num1, num2)
        return None

    def minus(self, num1, num2, op):
        if op:
            return self.sub.minus(num1, num2)
        return None
