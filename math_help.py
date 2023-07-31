"""
Author:         Pravar Kochar
Date:           MATH 151-2020/MATH 152 2021
E-mail:         pkochar1@umbc.edu
Description:    A program to help in math calculations.
"""

import math


def quadratic_probing(probe_pos, probe_base, table_length, amount_of_probes=10):
    for i in range(0, amount_of_probes):
        print((probe_pos + pow(probe_base, i)), end=' _ ')
    print()


def newton_method(x):
    for i in range(10):
        print(f"x_{i + 1}:\t{x}")
        # f_numerator = x
        f_x = x
        f_prime_x = 1
        x = x - (f_x / f_prime_x)


def reimenn_sum(n=0):
    r_sum = 0
    for i in range(1, n + 1):
        x = i / 2
        print(i, x)
        r_sum += fn(x)
        # print(i, r_sum)
    print(r_sum)


def left_endpoint_rule(a, b, n):
    # (upper - lower)/n
    del_x = (b - a) / n
    x = a
    left_endpoint_sum = 0
    # To compute the midpoint sum
    for i in range(n):
        # Get the function value.
        fn_val = fn(x)
        left_endpoint_sum += fn_val

        # increase x by del_x
        x += del_x

    return left_endpoint_sum * del_x


def right_endpoint_rule(a, b, n):
    # (upper - lower)/n
    del_x = (b - a) / n
    x = a + del_x
    right_endpoint_sum = 0
    # To compute the midpoint sum
    for i in range(n):
        # Get the function value.
        fn_val = fn(x)
        right_endpoint_sum += fn_val

        # increase x by del_x
        x += del_x

    return right_endpoint_sum * del_x


def midpoint_rule(a, b, n):
    # (upper - lower)/n
    del_x = (b - a) / n
    midpoint_sum = 0
    # To find the midpoint.
    mid_point = (2 * a + del_x) / 2

    # To compute the midpoint sum
    for i in range(n):
        # Get the function value.
        fn_val = fn(mid_point)

        midpoint_sum += fn_val
        # increase the midpoint by del_x
        mid_point += del_x

    return midpoint_sum * del_x


def trapezoid_rule(a, b, n):
    # (upper - lower)/n
    del_x = (b - a) / n
    x = a
    trap_sum = 0

    # To compute the trapezoid sum
    for i in range(n + 1):
        # Get the function value.
        fn_val = fn(x)
        # To multiply each value by 2 except for the extremes.
        if x not in [a, b]:
            fn_val *= 2

        trap_sum += fn_val
        # Update the x value with del_x.
        x += del_x

    return (del_x / 2) * trap_sum


def simpsons_rule(a, b, n):
    # Simpson's rule not possible for non even n.
    if n % 2 != 0:
        return -1

    # (upper - lower)/n
    del_x = (b - a) / n
    x = a
    simpson_sum = 0
    # print("Del_x = ", del_x)

    # To compute the simpson's sum
    for i in range(n + 1):
        # Get the function value.
        # print("x used : ", x, end='\t\t')
        fn_val = fn(x)
        # To multiply each value by 2 or 4 except for the extremes.
        if x not in [a, b]:
            if i % 2 == 0:
                fn_val *= 2
                # print("mult by 2", end='\t')
            else:
                fn_val *= 4
                # print("mult by 4", end='\t')

        # print("function value : ", fn_val)
        simpson_sum += fn_val
        # Update the x value with del_x.
        x += del_x

    simpson_sum = simpson_sum * del_x / 3
    return simpson_sum


def midpoint_error_bound(k, a, b, n):
    if k == 0:
        return -1
    return (k * (b - a) ** 3) / (24 * (n ** 2))


def trapezoid_error_bound(k, a, b, n):
    if k == 0:
        return -1
    return (k * (b - a) ** 3) / (12 * (n ** 2))


def simpsons_error_bound(k, a, b, n):
    if k == 0:
        return -1
    return (k * (b - a) ** 5) / (180 * (n ** 4))


def fn(x):
    # For function
    return math.sqrt(1 + math.sqrt(x))


def integration_approx():
    """ **********************************************************************
        Important:  Make sure you have updated the fn() to be specific to
                    the question.
    ********************************************************************** """

    # Parameters to change.
    upper_limit = 4
    lower_limit = 0
    number_of_divisions = 8
    k_trap_mid = 0
    k_simpson = 0

    # Left endpoint rule
    print("\nLeft endpoint rule = ", left_endpoint_rule(lower_limit,
                                                        upper_limit,
                                                        number_of_divisions))
    # Right endpoint rule
    print("Right endpoint rule = ", right_endpoint_rule(lower_limit,
                                                        upper_limit,
                                                        number_of_divisions))

    # Midpoint rule
    print("\nMidpoint rule = ", midpoint_rule(lower_limit, upper_limit,
                                              number_of_divisions))
    print("\tError Bound = ", midpoint_error_bound(k_trap_mid, lower_limit,
                                                   upper_limit,
                                                   number_of_divisions))

    # Trapezoid rule
    print("\nTrapezoid rule = ", trapezoid_rule(lower_limit, upper_limit,
                                                number_of_divisions))
    print("\tError Bound = ", trapezoid_error_bound(k_trap_mid, lower_limit,
                                                    upper_limit,
                                                    number_of_divisions))

    # Simpson's rule
    print("\nSimpson\'s rule = ", simpsons_rule(lower_limit, upper_limit,
                                                number_of_divisions))
    print("\tError Bound = ", simpsons_error_bound(k_simpson, lower_limit,
                                                   upper_limit,
                                                   number_of_divisions))


def recursion_ci(n=12):
    if n == 0:
        return 10000
    else:
        fn_val = round(1.03 * recursion_ci(n-1), 2)
        print(f"S_{n} = 1.03 * previous =  {fn_val}")
        return fn_val


if __name__ == '__main__':
    # newton_method(2)
    # reimenn_sum(6)
    # integration_approx()
    quadratic_probing(0, 2, 8)
    pass
