"""
Here we will learn more about file path 
"""
import os 
from pathlib import Path

# print(os.getcwd()) #/Volumes/Demo/100 days

# os.mkdir("/Volumes/Demo/100 days/day_7/filehanding/files") #it will create the file


with open("/Volumes/Demo/100 days/day_7/filehanding/password.txt",'w') as file:
    file.write("hi this is me Hero\n")
    file.write("hi this is me Hero\n")
    file.write("hi this is me Hero\n")
    file.write("hi this is me Hero\n")


# check file exit of not
print(os.path.exists("/Volumes/Demo/100 days/day_7/filehanding/password.txt")) #true

# is isfile or folder
print(os.path.isfile("/Volumes/Demo/100 days/day_7/filehanding/password.txt")) #ture

# check is folder
print(os.path.isdir("/Volumes/Demo/100 days/day_7/filehanding/password.txt")) #False


# removing the dir(folder)
folder_path = Path("/Volumes/Demo/100 days/day_7/filehanding/files")
if folder_path.exists(): #if file exist
    folder_path.rmdir() #remove the dif(folder)
    print("Folder deleted successfully")
else:
    print("Folder doesn't exist")


# removing the file
file_path = Path("/Volumes/Demo/100 days/day_7/filehanding/demo.txt")

if file_path.exists(): #if file exist
    file_path.unlink() # delete the file
    print("file has been deleted")
else:
    print("File doesn't exist")


