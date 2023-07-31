"""
Author:         Rohan Patel
Date:           3/6/2020
Description:    A program to find the factorial of a given number recursively.
"""

# Global constants for recursion.
BASE_CASE_RETURN = 1
FACTORIAL_BASE_CASES = [0, 1]
FACTORIAL_ERROR = -1


def recursion_factorial(number: int) -> int:
    """
    A function to find the factorial of a number recursively.
    :param number: Number to find the factorial for.
    :type number: int
    :return: Factorial error/ [1, range of integers]
    """

    # To return an error if the user asks for a negative factorial.
    if number < FACTORIAL_BASE_CASES[0]:
        return FACTORIAL_ERROR

    # Base case: fact(0) = 1, fact(1) = 1.
    if number in FACTORIAL_BASE_CASES:
        return BASE_CASE_RETURN

    # Recursive case: Return and call the recursive call.
    else:
        return number * recursion_factorial(number - 1)


if __name__ == '__main__':
    # Get the number to print it's factorial.
    factorial_find = int(input('Enter number to find factorial: '))
    # Get the factorial answer.
    factorial = recursion_factorial(factorial_find)

    # Print the factorial or factorial error cause.
    if factorial != FACTORIAL_ERROR:
        print(f"The factorial of the chosen number {factorial_find} is : "
              f"{factorial}")
    else:
        print(f"Cannot find the factorial of {factorial_find}.")
