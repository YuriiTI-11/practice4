class MyFibonacci:
    """Calculates the N-th Fibonacci number."""

    def calculate(self, n: int) -> int:
        """Returns the N-th Fibonacci number."""
        if n < 0:
            raise ValueError("n must be a non-negative integer.")
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
