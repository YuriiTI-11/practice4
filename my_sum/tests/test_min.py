from mysum.sum.min_element import MyMin

def test_min_element():
    """Test for finding the minimum element in a list of positive numbers."""
    
    numbers = [10, 20, 30, 5, 50]
    calculator = MyMin()
    result = calculator.find_min(numbers)

    assert result == 5, "Minimum element of [10, 20, 30, 5, 50] should be 5"

def test_min_element_empty_list():
    """Test for empty list."""
    
    numbers = []
    calculator = MyMin()
    try:
        result = calculator.find_min(numbers)
    except ValueError as e:
        assert str(e) == "The list cannot be empty.", "Error message should be 'The list cannot be empty.'"

def test_min_element_invalid_numbers():
    """Test for invalid numbers (not all numbers are positive)."""
    
    numbers = [10, 20, -5, 50]
    calculator = MyMin()
    try:
        result = calculator.find_min(numbers)
    except ValueError as e:
        assert str(e) == "All numbers must be positive.", "Error message should be 'All numbers must be positive.'"
