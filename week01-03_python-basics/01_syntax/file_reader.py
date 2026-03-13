# File Handing module
import os
from pathlib import Path

# read txt
def read_txt(file_name):
    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, file_name)
    with open(path, "r") as file:
        return file.read()


# Count the number of line in a txt file
def num_line(file_name):
    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, file_name)
    with open(path) as file:
        return len(file.readlines())


# Count words in a txt file
def num_word(file_name):
    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, file_name)
    with open(path) as file:
        return len(file.read())




if __name__ == "__main__":
    print(Path(__file__).parent)
    print(num_word("test.txt"))