"""
Author:         Pravar Kochar
Date:           5/12/2020
E-mail:         pkochar1@umbc.edu
Description:    A program to remember some weird features of python.
"""

import re

DASH = '-' * 10
NULL_TYPE_VALUES = [None, [], 0, '']
HEX_CHART = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'a': '1010',
    'b': '1011',
    'c': '1100',
    'd': '1101',
    'e': '1110',
    'f': '1111'
}
INSTRUCTION_TYPE = ['R', 'I', 'J']


def diff_null_values():
    """
    A function to show the difference between all the possible null values.
    """
    for each_null in NULL_TYPE_VALUES:

        print(f"{DASH} If == None {DASH}")
        # if each_null is None:
        if each_null is None:
            print(each_null, ':- True')
        else:
            print(each_null, ':- False')

        print(f"{DASH} If not each_null {DASH}")
        if not each_null:
            print(each_null, ':- True')
        else:
            print(each_null, ':- False')

        print()


def diff_while_for():
    """
    A function that shows the difference between while and for loops.
    """
    list_ = [0, 0, 0]
    print(list_)
    """
    Will cause an infinite loop as len(list_) changes each run.
    i = 0
    while i <= len(list_):
        i += 1
    """
    # Will run the initial len times (3 here), irrespective of the change in
    # the list_ because range makes an numbered list (I guess).
    for i in range(len(list_)):
        input(f'loop#{i + 1}')
        list_.append(0)
        print(list_)
    print(list_)


def remove_underscore(line):
    line_return = ""

    for each_letter in line:
        if each_letter != '_':
            line_return += each_letter
            if each_letter == '.':
                line_return += '\n'

    return line_return


def split_feature(string: str):
    split = string.split('/')
    print(split[-1][: -4])


def lowercase_to_uppercase(sentence: str) -> str:
    """
    A function that turns all lowercase to uppercase.
    """
    return_string = ""          # String to return
    # Loop through all letters.
    for each_letter in sentence:
        # If lowercase make it uppercase.
        if each_letter.islower():
            each_letter = each_letter.upper()
        # Write in return string.
        return_string += each_letter
    # Return the return_string
    return return_string


def regular_expression():
    string_ = "1we@the_domain.edu"
    reg_ex = "([a-z]|[A-Z])+(\d|[a-z]|[A-Z]|-)*@(([a-z]|[A-Z]|\d)+\.)+edu"

    if re.search(reg_ex, string_):
        print('Found it!')
    else:
        print('did not find it.')

    print(re.search(reg_ex, string_))


def count_letters(string):
    return len(string)


def hex_to_bin(hex_val):
    binary_val = ''
    for each_byte in hex_val:
        binary_val = binary_val + HEX_CHART[each_byte]
    print(binary_val, len(binary_val))
    return binary_val


def mips_instruction_format(ins_type, bin_in):
    if ins_type not in INSTRUCTION_TYPE:
        return "Incorrect instruction type."
    if ins_type == INSTRUCTION_TYPE[0]:     # R-type
        return str(bin_in[:6]) + ' ' + str(bin_in[6:11]) \
               + ' ' + str(bin_in[11:16]) + ' ' + str(bin_in[16:21]) \
               + ' ' + str(bin_in[21:26]) + ' ' + str(bin_in[26:])
    if ins_type == INSTRUCTION_TYPE[1]:     # I-type
        return str(bin_in[:6]) + ' ' + str(bin_in[6:11]) \
               + ' ' + str(bin_in[11:16]) + ' ' + str(bin_in[16:20]) \
               + '|' + str(bin_in[20:24]) + '|' + str(bin_in[24:28]) \
               + '|' + str(bin_in[28:])
    if ins_type == INSTRUCTION_TYPE[2]:     # J-type
        return str(bin_in[:6]) + ' ' + str(bin_in[6:8]) \
               + '|' + str(bin_in[8:12]) + '|' + str(bin_in[12:16]) \
               + '|' + str(bin_in[16:20]) + '|' + str(bin_in[20:24]) \
               + '|' + str(bin_in[24:28]) + '|' + str(bin_in[28:])


def sort_list(list_):
    list_ = list_.sort()
    return list_


if __name__ == '__main__':
    # diff_null_values()
    # diff_while_for()
    # line_to_remove_underscore = ""
    # print(remove_underscore(line_to_remove_underscore))
    # split_feature('https://www2.cs.uic.edu/~i101/SoundFiles
    # /BabyElephantWalk60.wav')
    # print(lowercase_to_uppercase("a | b | c | d | e | f | g | h | i | j | k
    # | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z"))
    # regular_expression()
    # print(count_letters("00000000000000000000000000010110"))
    # print(mips_instruction_format(INSTRUCTION_TYPE[1], hex_to_bin(
    # "adac0016")))
    lst = [42, 6, 9, 7, 2, 4, 5, 8, 97, 32, 41, 17, 12, 5, 28, 3, 9, 15, 35, \
          1729, 3, 101]
    sort_list(lst)
    print(len(lst), lst)
    pass
