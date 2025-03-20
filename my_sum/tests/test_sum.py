from mysum.sum.sum import MySum

def test_sum_p():
    """Positive test of sum of 2 integers"""

    a = 10
    b = 20
    calculator = MySum()
    result = calculator.sum(a, b)

    assert result == 30, "Sum of 10 and 20 should be 30"