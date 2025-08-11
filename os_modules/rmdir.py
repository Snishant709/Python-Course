import os
import shutil
# For empty folder os.rmdir("empty_folder")

# For folder with files inside shutil.rmtree("folder_with_files")

base_path="os_modules"
folders=os.listdir(base_path)#will show all the files and folders
print(folders)
for folder in folders:
    path=os.path.join(base_path,folder) #basepath/folder this will do
    if os.path.isdir(path):
        print(f"removing paths {path}")
        shutil.rmtree(path)
    #elif os.path.isfile(path):
    #    print(f"Removing file {path}")
    #    os.remove(path) #this will remove all the files 
    #I have files which is used so I wont remove that
