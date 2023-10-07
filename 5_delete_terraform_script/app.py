### WINDOWS SCRIPT ###

import glob
import os
import shutil

# Searching pattern inside folders and sub folders recursively
# search all jpg files
pattern = r"C:\Users\Ivan\Desktop\To_delete\**\.terraform"
for item in glob.iglob(pattern, recursive=True):
    # delete file
    print("Deleting:", item)
    shutil.rmtree(item)

pattern = r"C:\Users\Ivan\Desktop\To_delete\**\terraform*"
for item in glob.iglob(pattern, recursive=True):
    # delete file
    print("Deleting:", item)
    os.remove(item)

pattern = r"C:\Users\Ivan\Desktop\To_delete\**\.terraform.*"
for item in glob.iglob(pattern, recursive=True):
    # delete file
    print("Deleting:", item)
    os.remove(item)


### LINUX SCRIPT ###

import glob
import os
import shutil

# Search pattern inside folders and subfolders recursively
# Search all .terraform folders
pattern = "/home/ivan/To_delete/**/.terraform"
for item in glob.glob(pattern, recursive=True):
    # Delete folder
    print("Deleting:", item)
    shutil.rmtree(item)

# Search all terraform* files
pattern = "/home/ivan/To_delete/**/terraform*"
for item in glob.glob(pattern, recursive=True):
    # Delete file
    print("Deleting:", item)
    os.remove(item)

# Search all .terraform.* files
pattern = "/home/ivan/To_delete/**/.terraform.*"
for item in glob.glob(pattern, recursive=True):
    # Delete file
    print("Deleting:", item)
    os.remove(item)
