#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number.

    Parameters:
    n (int): The number for which the factorial is to be calculated.

    Returns:
    int: The factorial of the input number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Calculate the factorial of the number provided as a command-line argument
f = factorial(int(sys.argv[1]))
print(f)

