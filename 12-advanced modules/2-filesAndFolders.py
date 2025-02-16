########## you can ignore this folder if you have no time
import os
import shutil

currentWorkDirectory = os.getcwd() # detcwd: get current word directory
print(currentWorkDirectory) # C:\Users\abdow\OneDrive\Desktop\My Python stuff\12-advanced modules
print(os.listdir()) # list everything in the current folder
print(os.listdir('C:\\Users')) # list everything in a specific path

# shutil.move('test.txt', './newFolder/test.txt') # move file


"""
- os.unlink(path) which deletes a file at the path your provide
- os.rmdir(path) which deletes a folder (folder must be empty) at the path your provide
- shutil.rmtree(path) this is the most dangerous, as it will remove all files and folders contained in the path. 
- All of these methods can not be reversed! Which means if you make a mistake you won't be able to recover the file.
# pip install send2trash

"""

# os.walk() returs array of tuples, (folder, subFolder, files) to loop through each folder and file

for folder , sub_folders , files in os.walk("Example_Top_Level"):
    
    print("Currently looking at folder: "+ folder)
    print('\n')
    print("THE SUBFOLDERS ARE: ")
    for sub_fold in sub_folders:
        print("\t Subfolder: "+sub_fold )
    
    print('\n')
    
    print("THE FILES ARE: ")
    for f in files:
        print("\t File: "+f)
    print('\n')