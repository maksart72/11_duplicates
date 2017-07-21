import sys
import os
from collections import defaultdict


def get_file_list(folder):
    files_list = defaultdict(list)
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            file_info = os.path.getsize(file_path)
            files_list[file, file_info].append(file_path)
    return files_list


def find_duplicates(files_list):
    duplicates_list = defaultdict(list)
    for name, paths in files_list.items():
        if len(paths) > 1:
            duplicates_list[name].extend(paths)
    return duplicates_list


def output_duplicates(duplicates: defaultdict):
    for name, paths in duplicates.items():
        print('-'*30)
        print('Duplicated file: {} with size: {}'.format(name[0], name[1]))
        for path in paths:
            print('Location is: {}'.format(path))

if __name__ == '__main__':

    foldername = sys.argv[1]
    if os.path.isdir(foldername):
        output_duplicates((find_duplicates(get_file_list(foldername))))
    else:
        print("Error! Folder doesn't exist!")
