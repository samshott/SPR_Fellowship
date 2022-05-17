import os
import hoboreader
import pandas as pd
import shutil
import matplotlib as mp

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

def combine_txt_df(path_list = [], sep = "\t", quiet=False):
    """
    :param path_list: list, paths to txt files
    :param sep: string, how files are parsed
    :return: list, index 0: pandas data.frame of appended files, index 1: error files
    """
    append_df=pd.DataFrame(columns=["Date Time", "Bucket Tip (in)"])
    # append_df.columns["Date Time"] = ""
    # append_df.columns["Rain (in)"] = ""
    # append_df.columns["Temp"] = ""
    # append_df.columns["Station"] = ""
    error_files=[]

    for txt_file in path_list:
        try:
            txt_df = pd.read_csv(txt_file, sep=sep)
            txt_df = txt_df.rename(columns={txt_df.columns[0]:"Date Time", txt_df.columns[1]:"Bucket Tip (in)"})
            for column in txt_df.columns:
                if not (column in append_df.columns):
                    append_df[str(column)] = ""  #for preserving columns from logger. maybe better to assume order
            # if txt_df.shape[1] == 2:
            #     txt_df.columns = ["Date Time", "Rain (in)"]
            #     txt_df["Temp"] = ""
            # elif txt_df.shape[1] == 3:
            #     txt_df.columns = ["Date Time", "Rain (in)", "Temp"]
            txt_df["File Name"] = txt_file.split()[-1].split(".")[0]
            append_df = append_df.append(txt_df)
        except:
            error_files.append(txt_file)
    if not quiet:
        print("Unsuccesfull appends: ", error_files)
    return append_df
#still needed: - columns to title case
#              - whats wrong with 10/15/2005 0:53 file?



# copy_file(search_path="./OneDrive_1_5-6-2022/",
#           copy_dir= "./LegacyFiles/All_txt/",
#           extentension=".txt")

list_txt = search_filetype(path="LegacyFiles/All_txt/", extentension=".txt")



test_txt_df1 = pd.read_csv(list_txt[1], sep="\t")
test_txt_df2 = pd.read_csv(list_txt[2], sep="\t")

test_app_df = []
test_app_df = combine_txt_df(list_txt[0:50])
test_txt_df1 = test_txt_df1.rename(columns={test_txt_df1.columns[0]:"Date Time", test_txt_df1.columns[1]:"Bucket Time (in)"})
blank_df = pd.DataFrame()

blank_df.append(test_txt_df1)


test_txt_df1.columns = ["foo", "bar", "foo1", "bar1"]

test_txt_df1.shape[1]