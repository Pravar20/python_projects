"""
AD coding competition problem
"""


def is_divisor(possible_divisor: int, number: int) -> bool:
    return not bool(number % possible_divisor)


def count_divisor_num(number: int, divisor_list):
    number_of_divisor = 0
    for i in range(1, number + 1):
        if is_divisor(i, number) and (i not in divisor_list):
            divisor_list.append(i)
            number_of_divisor += 1

    return number_of_divisor


def count_divisor_for_array(num_array):
    divisor_array = []
    divisor_used = []
    for each_elem_i in num_array:
        divisor_array.append(count_divisor_num(each_elem_i, divisor_used))

    return divisor_array


def get_input():
    # Ask for number of inputs.
    number_of_input = int(input(''))

    # Ask for the array of numbers.
    array_input = input('').split(' ')
    array_input = array_input[: number_of_input]

    # Convert and make an integer list of the desired length.
    int_array_return = []
    for each_elem in array_input:
        int_array_return.append(int(each_elem))

    return int_array_return


if __name__ == '__main__':
    output_array = count_divisor_for_array(get_input())
    for each_output in output_array:
        print(each_output, end=' ')
    print()
