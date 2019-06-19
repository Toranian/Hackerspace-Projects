import os
import random

def rename_files():
    file_list = os.listdir("./message")
    os.chdir("./message")

    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
        # os.rename(file_name, str(random.randint(1, 9999)) + file_name)

rename_files()
