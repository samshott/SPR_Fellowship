import os
import parser

import hoboreader
import pandas as pd
import shutil

os.chdir("..")
os.getcwd()

def search_filetype(path = ".", extentension = ""):
    """
    :param path: string, where to search
    :param extentension: string, what files to look for
    :return: list, paths to all files with a matching extension
    """
    paths = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename[-len(extentension):] == extentension:
                paths.append(dirpath + filename)
    return paths

txt_paths = search_filetype(path = "./OneDrive_1_5-6-2022/",extentension=".txt")

csv_paths = search_filetype(extentension=".csv")


def copy_file(search_path=".", copy_dir="", extentension=""):
    for dirpath, dirnames, filenames in os.walk(search_path):
        for filename in filenames:
            if filename[-len(extentension):] == extentension:
                shutil.copyfile(src=dirpath+filename,
                                dst=copy_dir+filename,
                                follow_symlinks=False)

copy_file(search_path=os.getcwd()+"/OneDrive_1_5-6-2022/",
          copy_dir= os.getcwd()+"/LegacyFiles/All_txt/",
          extentension=".txt")

for txt_path in txt_paths:
    shutil.copyfile(txt_path , "./LegacyFiles/All_txt/")

print(csv_paths[1:5])






