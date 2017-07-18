import sys
import os
from collections import Counter


def find_duplicate(folder):

    files_list = []
    file_names = []
    duplicates_list = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            files_list.append([file, os.path.getsize(file_path), file_path])
            file_names.append(file)
    
    duplicate_name = [x for x in Counter(file_names) if Counter(file_names)[x] > 1]

    for filename in files_list:
        if filename[0] in duplicate_name:
            duplicates_list.append(filename)

    duplicates_list_copy = duplicates_list

    for file1 in files_list:
        for file2 in files_list:
            if (file1[0] == file2[0]) and (file1[1] == file2[1]) and (file1[2] != file2[2]):
                pass
    return duplicates_list
    
def print_duplicate_files(duplicates):
    for filename in duplicates:
        print(filename)


if __name__ == '__main__':

    foldername = sys.argv[1]
    if os.path.isdir(foldername):
        #print_duplicate_files((find_duplicate(foldername)))
        print(find_duplicate(foldername))
    else:
        print("Неправильный каталог")
