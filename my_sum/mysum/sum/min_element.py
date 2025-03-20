class MyMin:
    """Finds minimum element in an array of positive numbers."""

    def find_min(self, numbers: list) -> int:
        """Returns the minimum element of a list of positive numbers."""
        if not numbers:
            raise ValueError("The list cannot be empty.")
        min_num = min(numbers)
        if min_num <= 0:
            raise ValueError("All numbers must be positive.")
        return min_num