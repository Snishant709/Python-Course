import os
folders=os.listdir("os_modules")
for folder in folders:
    print(folder)
    print(os.listdir(f"os_modules/{folder}"))
   