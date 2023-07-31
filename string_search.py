"""
Author:         Pravar Kochar
Date:           3/6/2020
Description:    A program to find the smaller string in the bigger string.
"""

START_INDEX_KEY = 'start'
END_INDEX_KEY = 'end'
STRING_FOUND = 'string_found'
DEFAULT_INDEX_RETURN = -1


def search_string(string_1: str, string_2: str) -> dict:
    return_dictionary = {
        STRING_FOUND: False,
        START_INDEX_KEY: DEFAULT_INDEX_RETURN,
        END_INDEX_KEY: DEFAULT_INDEX_RETURN
    }

    # If the string 1 is bigger.
    if len(string_1) > len(string_2):
        find_return = string_1.find(string_2)
        if find_return != -1:
            return_dictionary[STRING_FOUND] = True
            return_dictionary[START_INDEX_KEY] = find_return
            return_dictionary[END_INDEX_KEY] = return_dictionary[
                                               START_INDEX_KEY] + len(string_2)
        else:
            return_dictionary[STRING_FOUND] = False
    # If the string 2 is bigger
    else:
        find_return = string_2.find(string_1)
        if find_return != -1:
            return_dictionary[STRING_FOUND] = True
            return_dictionary[START_INDEX_KEY] = find_return
            return_dictionary[END_INDEX_KEY] = return_dictionary[
                                                START_INDEX_KEY] + len(string_1)
        else:
            return_dictionary[STRING_FOUND] = False

    # Dictionary with required returns.
    return return_dictionary


def string_compare():
    str1 = input('Enter string 1: ')
    str2 = input('Enter string 2: ')

    fn_return_dictionary = search_string(str1, str2)
    if fn_return_dictionary[STRING_FOUND]:
        if len(str1) > len(str2):
            print(f"The smaller string \'{str2}\' was found in bigger string"
                  f" \'{str1}\' at the position ["
                  f"{fn_return_dictionary[START_INDEX_KEY]} to "
                  f"{fn_return_dictionary[END_INDEX_KEY]}].")
        else:
            print(f"The smaller string \'{str1}\' was found in bigger string"
                  f" \'{str2}\' at the position ["
                  f"{fn_return_dictionary[START_INDEX_KEY]} to "
                  f"{fn_return_dictionary[END_INDEX_KEY]}].")
    else:
        print("The smaller string was not found in the bigger string.")


def print_quadratic_probing():
    table_len = int(input("Table len: "))
    pos = int(input("Position to probe: ")) % (table_len+1)

    for probe_ctr in range(0, 100):
        print((pos + probe_ctr ** 2) % (table_len+1), end='\t')
        if probe_ctr % 10 == 9:
            print()


if __name__ == '__main__':
    print_quadratic_probing()
