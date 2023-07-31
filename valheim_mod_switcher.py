"""
Author:         Pravar Kochar
Description:    A program to switch between personal and public server mods.
"""

import os
import shutil


class ModInjector:
    def __init__(self):
        self.mod_storage = 'D:/Valheim mod'
        self.personal_dir_name = 'D:/Valheim mod/personal mods'
        self.public_dir_name = 'D:/Valheim mod/jotenheim mod'
        self.valheim_dest_name = 'D:/Steam/steamapps/common/Valheim'
        self.personal_dir = os.listdir(self.personal_dir_name)
        self.public_dir = os.listdir(self.public_dir_name)
        self.valheim_dest = os.listdir(self.valheim_dest_name)

        self.src = ''
        self.dst = ''

    def pull_back(self, dest_dir: dir, dest_str: str):
        # to pull back the files into the mod folder.
        for file in dest_dir:
            dst_fp = os.path.join(dest_str, file)    # file path in destination.
            if os.path.isfile(dst_fp):
                os.remove(dst_fp)        # Remove the file in dest
            else:
                shutil.rmtree(dst_fp)    # Remove the dir in dest

            # move the new file/dir to dest from source.
            shutil.move(os.path.join(self.valheim_dest_name, file), dest_str)
            print(file, '---->', dest_str)

    def push_out(self, src_dir: dir, src_str: str):
        # breaking here
        # to push out the mod to game folder
        for file in src_dir:
            src_fp = src_str + '/' + file    # fp in src
            if os.path.isfile(src_fp):
                shutil.copy(src_fp, self.valheim_dest_name)
                print('Copied file ', src_fp)
            else:
                shutil.copytree(src_fp, self.valheim_dest_name + '/' + file)
                print('Copied folder ', src_fp)

    def is_personal(self):
        return all(file in self.valheim_dest for file in self.personal_dir)

    def is_public(self):
        return all(file in self.valheim_dest for file in self.public_dir)

    def switch_mods(self):  # function to toggle mods.
        if self.is_personal():  # if personal mods are loaded.
            self.pull_back(self.personal_dir, self.personal_dir_name)
            print("pull back complete")
            self.push_out(self.public_dir, self.public_dir_name)
            print("push out complete")
        elif self.is_public():
            self.pull_back(self.public_dir, self.public_dir_name)
            print("pull back complete")
            self.push_out(self.personal_dir, self.personal_dir_name)
            print("push out complete")
        else:
            print('No previous mod')


if __name__ == '__main__':
    mi = ModInjector()
    mi.switch_mods()
