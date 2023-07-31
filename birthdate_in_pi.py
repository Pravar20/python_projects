"""
Author:         Pravar Kochar
Date:           //2020
E-mail:         pkochar1@umbc.edu, pravar.kochar@gmail.com
Description:    A program to check if a given birthdate is in the
                one-billionth digit of pi.
"""

import requests


CONNECTOR = '/'
DATE = 'birth_date'
DAY = 'day'
MONTH = 'month'
YEAR = 'year'


class Pi:
    def __init__(self):
        self.pi = 0
        self.get_pi()

    def search_pi_for_date(self, string_to_find):
        """
        To find and return if the given number is pi.
        :param string_to_find: The number to find. (string)
        :return: True/False
        """
        return string_to_find in self.pi

    def get_pi(self):
        """
        A function to get the digits of pi from a site.
        :return: The string version of pi, one-billion digits.
        """
        page = 'https://www.angio.net/pi/digits/pi1000000.txt'
        self.pi = str(requests.get(page).content)


class BirthDate(Pi):
    def __init__(self):
        super().__init__()
        self.birth_date = {
            DATE: '',
            DAY: '',
            MONTH: '',
            YEAR: ''
        }

    def ask_birthday(self):
        """
        A function to ask for the user's birthday and store it without slash.
        """
        bday_str = input('What is your b\'day? (dd/mm/yyyy)\t')

        bday_str = bday_str.split(CONNECTOR)

        self.birth_date[DAY] = bday_str[0]
        self.birth_date[MONTH] = bday_str[1]
        self.birth_date[YEAR] = bday_str[2]

        bday_str = ''.join(bday_str)

        self.birth_date[DATE] = bday_str

    def show_result(self):
        """ A function to tell if date is there in pi. """
        print()
        for number_index in self.birth_date:
            print(f"Your {number_index}\'s ({self.birth_date[number_index]})"
                  f" existence in pi: "
                  f"{self.search_pi_for_date(self.birth_date[number_index])}")


if __name__ == '__main__':
    find_in_pi = BirthDate()
    find_in_pi.ask_birthday()
    find_in_pi.show_result()
