from calculator.calculator import Calculator
from operations.sum.add import Add
from operations.minus.sub import Sub
import re

if __name__ == "__main__":
    calculator = Calculator(Add(), Sub())
    sum   = calculator.sum(2, 5, True)
    minus = calculator.minus(5, 3, False)
    word  = ".test"
    # regex = re.compile("[@_!#$%^&*()<>?/\|}{~:]")
    regex = re.compile("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$")
    email = "test@test.com"

print(sum)
print(minus)
print("True" if str(word[:1]).__contains__(".") else "False")
print("Ok!" if regex.search(email) else "Error!")
# assert str(word[:1]).__contains__(".") == False
assert regex.search(email) == False
