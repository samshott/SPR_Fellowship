import os
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


def copy_file(search_path=".", copy_dir="", extentension="",show_errors = True):
    """
    :param search_path: string, directory to search
    :param copy_dir: string, directory to copy files to
    :param extentension: string, type of files to copy - include the '.'
    :param show_errors: bool, whether to print files that did not copy succesfully or not
    :return: a list of files that did not copy successfully
    """
    error_files = []
    for dirpath, dirnames, filenames in os.walk(search_path):
        for filename in filenames:
            if filename[-len(extentension):] == extentension:
                full_path = dirpath+"/"+filename
                try:
                    shutil.copy2(src=full_path,dst=copy_dir+filename,follow_symlinks=False)
                except:
                    error_files.append(full_path)
    if show_errors:
        print(error_files)
    return (error_files)


copy_file(search_path="./OneDrive_1_5-6-2022/",
          copy_dir= "./LegacyFiles/All_txt/",
          extentension=".txt")







