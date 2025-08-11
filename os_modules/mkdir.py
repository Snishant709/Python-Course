import os
if (not os.path.exists("os_modules/data")):
    os.mkdir("os_modules/data")

for i in range(0,100):
    os.mkdir(f"os_modules/data{i+1}")