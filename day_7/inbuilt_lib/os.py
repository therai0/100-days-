""" The os module is used for file and directory access. You can get the current working directory and create new directories using this module. """

import os 

print(os.getcwd()) # it wll print the current working directory(path)
print(os.listdir()) # Lists all files and directories in the given path (default is current dir).

print(os.listdir('/Volumes/Demo/100 days/day_1')) # it will return the list of files and folder of day_1 folder

""" 
Note: if folder and files are already created then it will throw the error
Error: FileExistsError
"""
os.mkdir("demo") # it will create the demo folder(directory) 
os.makedirs("dummy/dums") # it will create the dummy folder and inside the dummy folder it will create the dums subfolder

print(os.path.exists("demo")) # it will return the boolean value if folder or file exist 


