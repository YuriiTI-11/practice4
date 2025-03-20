from mysum.sum.sum_negative import MySumNegative

def test_negative_sum():
    """Test for summing negative numbers in a list."""
    
    numbers = [-1, -2, -3, -4]
    calculator = MySumNegative()
    result = calculator.sum_negative(numbers)

    assert result == -10, "Sum of [-1, -2, -3, -4] should be -10"

def test_negative_sum_invalid_numbers():
    """Test for invalid numbers (not all numbers are negative)."""
    
    numbers = [-1, -2, 3, -4]
    calculator = MySumNegative()
    try:
        result = calculator.sum_negative(numbers)
    except ValueError as e:
        assert str(e) == "All numbers must be negative.", "Error message should be 'All numbers must be negative.'"
