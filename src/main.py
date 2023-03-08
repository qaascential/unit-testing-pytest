from operations.sum.add import Add
from operations.sum.tests.test_add import TestAdd
from operations.minus.tests.test_sub import TestSub

if __name__ == "__main__":
    print(f"SUM: {Add().sum(1, 2)}")

    TestAdd().test_sum()
    TestSub().test_minus()
