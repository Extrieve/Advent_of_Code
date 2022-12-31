import os
import shutil

def get_file_list(path):
    """Return a list of all files in a directory."""
    # if file contains the word 'day' move it to 2022
    for file in os.listdir(path):
        if 'day' in file:
            print(file)
            shutil.move(file, '2022')


if __name__ == '__main__':
    get_file_list('.')
