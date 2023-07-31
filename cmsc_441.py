"""
Author:         Pravar Kochar
E-mail:         pkochar1@umbc.edu
"""
import math


def fibonacci(number):
    if number in [1, 2]:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


def factorial_loop(number):
    ans = 1
    for i in range(1, number):
        ans = ans * i
    return ans


def factorial_rec(number):
    if number == 0:
        return 1
    return number * factorial_rec(number - 1)


def cut_sheet(n, m, price):
    if n == 0 or m == 0:
        return price[n][m]
    maximum = 0
    for i in range(0, n):
        for j in range(0, m):
            current = cut_sheet(i, j, price) + price[n - i][j] + \
                      price[i][m - j] + price[n - i][m - j]
            if current > maximum:
                maximum = current
    return maximum


def knap_sack(weight, wt_arr, val_arr, length):
    if length == 0 or weight == 0:
        return 0
    if wt_arr[length - 1] > weight:
        return knap_sack(weight, wt_arr, val_arr, length - 1)
    else:
        return max(
            val_arr[length - 1] + knap_sack(weight - wt_arr[length - 1], wt_arr,
                                            val_arr, length - 1),
            knap_sack(weight, wt_arr, val_arr, length - 1))


def cut_rod_cut_cost(price, length, cut_cost, number_of_cuts=0):
    if length <= 0:
        return 0, 0
    max_val = -math.inf - 1
    for i in range(0, length):
        pre_max, number_of_cuts = cut_rod_cut_cost(price, length - i - 1,
                                                   cut_cost, number_of_cuts)
        profit = price[i] + pre_max - number_of_cuts * cut_cost
        max_val = max(max_val, profit)
    return max_val, number_of_cuts + 1


def lcs_memoized(a, b, memo_list, i=0, j=0):
    if i <= len(a) or j <= len(b):
        return 0
    if memo_list[i][j] != -1:
        return memo_list[i][j]
    match = 0
    if a[i] == b[j]:
        if memo_list[i + 1][j + 1] != -1:
            memo_list[i + 1][j + 1] = lcs_memoized(a, b, memo_list, i + 1,
                                                   j + 1)
        match = memo_list[i + 1][j + 1] + 1
    if memo_list[i + 1][j] != -1:
        memo_list[i + 1][j] = lcs_memoized(a, b, memo_list, i + 1, j)
    skip_a = memo_list[i + 1][j]
    if memo_list[i][j + 1] != -1:
        memo_list[i][j + 1] = lcs_memoized(a, b, memo_list, i, j + 1)
    skip_b = memo_list[i][j + 1]
    return max(match, skip_a, skip_b)


def greedy_shopping(prices, money):
    prices = sorted(prices)
    items = 0
    for each_price in prices:
        if each_price <= money:
            money -= each_price
            items += 1
        if money == 0:
            return items
    return items


def greedy_unit_lines(points, unit_len=10):
    number_of_lines = 1
    working_line = unit_len + points[0]
    for each_point in points:
        # if point bigger than previous line make new line
        if each_point > working_line:
            working_line = unit_len + each_point
            number_of_lines += 1
    return number_of_lines


def set_diff(set_):  # helper for on sorted set.
    return set_[len(set_) - 1] - set_[0]


def greedy_small_difference_subset(int_list, set_size):
    # Sort the list.
    int_list = sorted(int_list)

    # Set the first set as greedy set.
    greedy_set = int_list[:set_size]
    greedy_set_diff = set_diff(greedy_set)

    for i in range(1, len(int_list) - set_size + 1):
        # Make the working set
        current_set = int_list[i:i + set_size]
        curr_set_diff = set_diff(current_set)
        # Choose the set with smaller difference.
        if curr_set_diff < greedy_set_diff:
            greedy_set = current_set
            greedy_set_diff = set_diff(greedy_set)

    return greedy_set


def list_preprocess(S, num_max):
    # Create a counting bucket of num_max + 1 elements (0 to num_max)
    M = [0 for i in range(0, num_max + 1)]
    for num in S:
        M[num] += 1
    return M


def counting_in_range(M, a, b):
    count = 0
    for i in range(a, b):
        count += M[i]
    return count


def numbers_in_range(S, a, b, num_max=10):
    M_list = list_preprocess(S, num_max)
    return counting_in_range(M_list, a, b)


if __name__ == '__main__':
    print(numbers_in_range([0, 1, 7, 1, 2, 0, 1, 3, 4, 3, 7, 7, 8, 9], 2, 5))

