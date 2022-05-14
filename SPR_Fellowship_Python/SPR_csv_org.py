import os

os.chdir("..")
os.getcwd()

csv_paths = []

for dirpath, dirnames, filenames in os.walk(".SPR_Fellowship/"):
    print(filenames)

test




