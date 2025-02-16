## Create Files to Compress
f = open("new_file.txt",'w+')
f.write("Here is some text")
f.close()

f2 = open("new_file2.txt",'w+')
f2.write("Here is some text")
f2.close()


## Zipping Files
## The zipfile library is built in to Python, we can use it to compress folders or files.

import zipfile
comp_file = zipfile.ZipFile('comp_file.zip','w')
comp_file.write("new_file.txt",compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('new_file2.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()


## Extracting from Zip Files
zip_obj = zipfile.ZipFile('comp_file.zip','r')
zip_obj.extractall("extracted_content") # unzip the com_file.zip to extracted_content folder (it will create it if not exist)





## when dealing with files and folders, shutil is better than zipfile
## Using shutil library
import shutil
import os
directory_to_zip= os.getcwd()
print(directory_to_zip)


# Creating a zip archive
output_filename = 'example'
shutil.make_archive(output_filename,'zip',directory_to_zip)


# Extracting a zip archive
# Notice how the parameter/argument order is slightly different here
shutil.unpack_archive('example.zip','final_unzip','zip')