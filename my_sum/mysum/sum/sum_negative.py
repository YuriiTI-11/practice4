class MySumNegative:
    """Sums only negative numbers from the list."""

    def sum_negative(self, numbers: list) -> int:
        """Returns the sum of negative numbers in a list."""
        if not all(num < 0 for num in numbers):
            raise ValueError("All numbers must be negative.")
        return sum(numbers)
