"""
Author:         Ishanvi Kochar
Date:           25/08/2022
Class:          10-B
E-mail:         03450@asianintlschool.com
Description:    A python program to check if a number is a prime or not.
"""


def is_prime(number):
    """
    A function to check if a number is prime.
    :param number: An integer number to find if it is prime.
    :return: True/False depending on prime or not.
    """
    for each_number in range(2, number):
        # To return true if the number is divisible.
        if number % each_number == 0:
            return False
    return True


if __name__ == '__main__':
    # Ask user for input.
    user_input = int(input("Enter a number to check if it's prime: "))

    # Tell the user if the number is prime using the function.
    if is_prime(user_input):
        print(f"Your number ({user_input}) is prime.")
    else:
        print(f"Your number ({user_input}) is not prime.")
