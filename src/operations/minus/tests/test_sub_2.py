import pytest
from src.operations.minus.sub import Sub

sub_operation = Sub()


class TestSub2:
    @pytest.mark.parametrize("num1, num2, result",
        [
            (6, 5, 1),
            (5, 5, 1),
            (4, 5, -1),
            (2, 2, 0)
        ]
    )
    def test_minus_2(self, num1, num2, result):
        assert sub_operation.minus(num1, num2) == result
