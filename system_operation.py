import os
import shutil

def get_file_list(path, keyword) -> list:
    """Return a list of all files in a directory."""
    # if file contains the word 'day' move it to 2022
    files = []
    for file in os.listdir(path):
        if keyword in file: 
            shutil.move(file, '2022')
            files.append(file)
    return files

def main() -> None:
    """Run the main function."""
    get_file_list('.', 'day')

if __name__ == '__main__':
    main()
