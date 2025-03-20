from mysum.sum.fibonacci import MyFibonacci

def test_fibonacci():
    """Test for calculating the N-th Fibonacci number"""

    n = 5  # N-th element of Fibonacci sequence (0, 1, 1, 2, 3, 5, 8, ...)
    calculator = MyFibonacci()
    result = calculator.calculate(n)

    assert result == 5, "The 5th Fibonacci number should be 5"

def test_fibonacci_zero():
    """Test for Fibonacci when N is 0"""
    
    n = 0
    calculator = MyFibonacci()
    result = calculator.calculate(n)

    assert result == 0, "The 0th Fibonacci number should be 0"

def test_fibonacci_negative():
    """Test for Fibonacci with negative input, should raise ValueError"""
    
    n = -1
    calculator = MyFibonacci()
    try:
        result = calculator.calculate(n)
    except ValueError as e:
        assert str(e) == "n must be a non-negative integer.", "Error message should be 'n must be a non-negative integer.'"
