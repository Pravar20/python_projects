"""
Author:         Pravar Kochar
Date:           //2020
E-mail:         pkochar1@umbc.edu, pravar.kochar@gmail.com
Description:    A program to download any type of file from a url.
"""

import requests
import os


URL = 'place'
NAME = 'name'
POS_S = 'position to save as'


def download_jpg(file_name, url, pos_to_save='C:\\Users\\DELL\\Desktop\\UMBC\\FYS'):
    """
    A function that saves the given jpg from a url to local host.
    :param file_name: The name the file is to be saved as.
    :param url: The url containing the .jpg file.
    """
    if not os.path.exists(pos_to_save):
        os.makedirs(pos_to_save)

    file_name = pos_to_save + file_name

    with open(file_name, 'wb') as picture:
        response = requests.get(url, stream=True)

        for block in response.iter_content(1024):
            if not block:
                break

            picture.write(block)


if __name__ == '__main__':
    runs = [
        {
            NAME: 'class#2.mp4',
            URL: '',
            POS_S: 'C:\\Users\\DELL\\Desktop\\UMBC\\FYS\\Day2\\'
        }
    ]

    for each_run in runs:
        download_jpg(each_run[NAME], each_run[URL], each_run[POS_S])
