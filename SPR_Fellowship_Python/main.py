import os

os.chdir("..")
os.getcwd()

csv_paths = []

for (dirpath, dirnames, filenames) in os.walk("SPR_Fellowship/"):
    if filenames[-4:] == ".csv":
        csv_paths.append(dirpath + filenames)




