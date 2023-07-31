"""
Author:         Pravar Kochar
E-mail:         pkochar1@umbc.edu
Description:    A program to store passwords using hash and salt in multiple
                files with each file having a single password.
"""

import os
import hashlib
import csv
import sqlite3 as sqll
import tabulate

NEW_PASS = {'1', 'new pass', 'new'}
EDIT_PASS = {'2', 'edit pass', 'edit'}
GET_PASS = {'3', 'get pass', 'get'}
EXIT_CONDITION = {'4', 'exit', 'exit'}

"""
def get_file_name() -> str:
    file_name = input("Enter file name: ")
    if CSV_EXT not in file_name:
        file_name += CSV_EXT
    return file_name
"""
"""
def new_pass():
    file_name = get_file_name()
    pass_to_save = encrypt(get_pass())

    data = {'site_name': file_name[:3], 'password': pass_to_save}
    with open(file_name, 'w', newline='') as csv_file:
        pass
"""


class SqlStorage:
    def __init__(self, db_file='Storage.db', tb_name='Sites'):
        """
        Class constructor
        :param db_file: The database file name.
        :param tb_name: The table name.
        """
        self.tb_name = tb_name

        self.NN = 'NOT NULL'
        self.MUTABLE_VAL = "\'Site_name\', \'Site_link\', \'Password\'"

        self._db_file = db_file

        self.sql_db = sqll.connect(db_file)
        print("Database connection: Established")

        self._table_found = self.check_table_existence()
        if self._table_found:
            print("\tTable status: Found")
        else:
            self._create_table()
            print("\tTable created")
            self._table_found = self.check_table_existence()

    def check_table_existence(self) -> bool:
        """
        A function to return if the table exists or not.
        :return: true/false: depending on if table exists or not.
        """
        data = self.sql_db.cursor().execute(
            f"SELECT count(*) FROM sqlite_master WHERE type='table'"
            f"AND name='{self.tb_name}';"
        )
        for row in data:
            # print(row)
            if row[0] == 0:
                return False
            else:
                return True

    def _create_table(self):
        """
        A function to create the table or skip the creation if table exists.
        """
        self.sql_db.execute(
            f"CREATE TABLE IF NOT EXISTS {self.tb_name}"
            f"(ID INTEGER PRIMARY KEY AUTOINCREMENT {self.NN},"
            f"Site_name TEXT {self.NN},"
            f"Site_link BLOB,"
            f"Password BLOB);"
        )

    def insert_data(self, site_name, site_link, encrypt_pass):
        """
        A function to insert data into the table.
        :param site_name: The name of the site.
        :param site_link: The link for the site.
        :param encrypt_pass: The encrypted password to be stored into the db.
        """
        print(f"\t\tInserting data: {site_name} ({encrypt_pass})")
        with self.sql_db:
            self.sql_db.cursor().execute(
                f"INSERT INTO {self.tb_name}({self.MUTABLE_VAL}) "
                f"VALUES ('{site_name}', '{site_link}', '{encrypt_pass}');"
            )

    def _display_full_table(self):
        """
        A hidden function that prints the whole table.
        """
        with self.sql_db:
            out = self.sql_db.cursor().execute(f"SELECT * FROM {self.tb_name};")
            for row in out:
                print(type(row), row)

    def __drop_table(self):
        self.sql_db.execute(f"DROP TABLE {self.tb_name};")

    def __del__(self):
        if self._table_found:
            self.sql_db.commit()
            self.sql_db.close()
            print("Database connection: Terminated")


def get_pass() -> str:
    pass


def decrypt(hash: str) -> str:
    pass


def encrypt(password: str) -> str:
    pass


def new_pass():
    pass


def edit_pass():
    pass


def menu():
    user_input = input("Options:\n1. New pass\n2. Edit pass\n3. Get pass\n4. "
                       "Exit")
    while user_input not in EXIT_CONDITION:
        if user_input in NEW_PASS:
            new_pass()
        elif user_input in EDIT_PASS:
            edit_pass()
        elif user_input in GET_PASS:
            get_pass()
        else:
            print("Please enter a valid input.")

        user_input = input("Options:\n1. New pass\n2. Edit pass\n3. Get "
                           "pass\n4. Exit")


if __name__ == '__main__':
    # menu()
    st = SqlStorage()
    # st.insert_data("test1", "httpsserver", "asdasd")
    st._display_full_table()
