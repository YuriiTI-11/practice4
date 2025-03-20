import argparse
from mysum.sum.sum import MySum
from mysum.sum.min_element import MyMin
from mysum.sum.sum_negative import MySumNegative
from mysum.sum.fibonacci import MyFibonacci
from mysum.sum.current import MyCurrent

def sum_ints(a: int, b: int):
    """Sums 2 integers from user"""
    calculator = MySum()
    c = calculator.sum(a, b)
    # Print the result
    print(f"{a} + {b} = {c}")


def find_min_element(numbers: list):
    """Finds minimum element in a list of positive numbers."""
    calculator = MyMin()
    try:
        result = calculator.find_min(numbers)
        print(f"Minimum element: {result}")
    except ValueError as e:
        print(f"Error: {e}")


def sum_negative_elements(numbers: list):
    """Sums elements in a list that consists of only negative numbers."""
    calculator = MySumNegative()
    try:
        result = calculator.sum_negative(numbers)
        print(f"Sum of negative elements: {result}")
    except ValueError as e:
        print(f"Error: {e}")


def fibonacci(n: int):
    """Calculates the N-th Fibonacci number."""
    calculator = MyFibonacci()
    try:
        result = calculator.calculate(n)
        print(f"The {n}-th Fibonacci number is: {result}")
    except ValueError as e:
        print(f"Error: {e}")


def current_in_circle(radius: float, voltage: float, resistance: float):
    """Calculates current in a segment of a circle."""
    calculator = MyCurrent()
    try:
        result = calculator.calculate_current(radius, voltage, resistance)
        print(f"Current in the circle: {result} Amps")
    except ValueError as e:
        print(f"Error: {e}")


def main():
    """Main function to run the correct functionality"""
    # First, we parse the main argument to determine which function to run
    parser = argparse.ArgumentParser(description='Choose an algorithm to run')
    parser.add_argument('-f', '--function', type=int, required=True, help='Function number (1 for sum, 2 for min, 3 for sum_negative, 4 for fibonacci, 5 for current)')

    # Parse the arguments
    args, unknown = parser.parse_known_args()

    if args.function == 1:
        # Sum functionality
        sum_parser = argparse.ArgumentParser(description='Sum of 2 integers')
        sum_parser.add_argument('-a', dest='a', required=True, type=int, help='The first integer')
        sum_parser.add_argument('-b', dest='b', required=True, type=int, help='The second integer')
        sum_args = sum_parser.parse_args(unknown)  # Pass the unknown arguments to this parser
        sum_ints(sum_args.a, sum_args.b)

    elif args.function == 2:
        # Min functionality
        min_parser = argparse.ArgumentParser(description='Find minimum element in an array of positive integers')
        min_parser.add_argument('--numbers', type=int, nargs='+', required=True, help='List of positive integers')
        min_args = min_parser.parse_args(unknown)  # Pass the unknown arguments to this parser
        find_min_element(min_args.numbers)

    elif args.function == 3:
        # Sum of negative elements
        sum_neg_parser = argparse.ArgumentParser(description='Sum of negative integers')
        sum_neg_parser.add_argument('--numbers', type=int, nargs='+', required=True, help='List of negative integers')
        sum_neg_args = sum_neg_parser.parse_args(unknown)  # Pass the unknown arguments to this parser
        sum_negative_elements(sum_neg_args.numbers)

    elif args.function == 4:
        # Fibonacci functionality
        fib_parser = argparse.ArgumentParser(description='Calculate the N-th Fibonacci number')
        fib_parser.add_argument('-n', type=int, required=True, help='The index N of the Fibonacci sequence')
        fib_args = fib_parser.parse_args(unknown)  # Pass the unknown arguments to this parser
        fibonacci(fib_args.n)

    elif args.function == 5:
        # Current in the circle
        current_parser = argparse.ArgumentParser(description='Calculate current in a segment of a circle')
        current_parser.add_argument('-r', type=float, required=True, help='Radius of the circle')
        current_parser.add_argument('-v', type=float, required=True, help='Voltage applied')
        current_parser.add_argument('-res', type=float, required=True, help='Resistance of the circuit')
        current_args = current_parser.parse_args(unknown)  # Pass the unknown arguments to this parser
        current_in_circle(current_args.r, current_args.v, current_args.res)

    else:
        print("Invalid function number! Please choose 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()
