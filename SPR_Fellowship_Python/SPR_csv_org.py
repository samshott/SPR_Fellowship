#%%
import os
#from hoboreader import HoboReader
import pandas as pd
import shutil
import matplotlib as mp
import re

#os.chdir("..")
os.chdir("C:\\Users\\samer\\OneDrive - Cal Poly\\Classes\\SPR_Fellowship\\SPR_Fellowship")
os.getcwd()

#%%
def header_fixer(path = ".", col_names = []):
    """
    :param path:
    :param col_names:
    :return:
    """
    csv = pd.read_csv(path, sep="\t")
    #csv = pd.read_csv(list_ex_headers[1],sep="\t")
    #path = list_ex_headers[1]
    if csv.shape[1] < 2:
        serial_Num = re.findall("[0-9]{5,6}", csv.columns[0])
        csv = pd.read_csv(path, header=1, sep="\t")
        csv["Serial Number"] = serial_Num[0]
    else:
        csv = pd.read_csv(path, sep="\t")
        csv["Serial Number"] =  None

    return csv

#%%
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
                paths.append(dirpath + "/" + filename)
    return paths
#%%
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
#%%


##keep serial number if possible
##keep name if available
##
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
            txt_df["File Name"] = txt_file.split()[-1].split(".")[0]
            append_df = append_df.append(txt_df)
        except:
            try:
                #ignore serial number header
                pd.read_csv(txt_file, header=1, sep=sep)
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
#%%
#%%

list_ex_headers = search_filetype(path="LegacyFiles/All_txt/txt_header_examples/", extentension=".txt")
list_txt = search_filetype(path="LegacyFiles/All_txt/", extentension=".txt")


#%%
test_txt_df1 = pd.read_csv(list_txt[1], sep="\t")
test_txt_df2 = pd.read_csv(list_txt[2], sep="\t")
#%%
#test_app_df = []
#test_app_df = combine_txt_df(list_txt[0:50])
#test_txt_df1 = test_txt_df1.rename(columns={test_txt_df1.columns[0]:"Date Time", test_txt_df1.columns[1]:"Bucket Time (in)"})
#blank_df = pd.DataFrame()
#%%
def cumulative_to_individual(dataframe, column_index):
    pass



#blank_df.append(test_txt_df1)


#test_txt_df1.columns = ["foo", "bar", "foo1", "bar1"]

#test_txt_df1.shape[1]


#%%
comb_df = pd.DataFrame()
errors = 0
error_list = []
for path in list_txt:
    try:
        csv = header_fixer(path)
        csv["fileName"] = path.split(sep="/")[-1]
        comb_df = pd.concat([comb_df, csv], ignore_index=True)
    except:
        print(path)
        error_list.append(path)
        errors += 1
print(errors)