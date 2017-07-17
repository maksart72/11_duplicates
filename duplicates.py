import sys
import os


def find_duplicate(folder):

    files_list = []
    duplicates_list = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            files_list.append([file, os.path.getsize(file_path), file_path])

    for file1 in files_list:
        for file2 in files_list:
            if (file1[0] == file2[0]) and (file1[1] == file2[1]) and (file1[2] != file2[2]):
                duplicates_list.append(file1[2])

    duplicates_list = set(duplicates_list)
    return duplicates_list


def print_duplicate_files(duplicates):
    for filename in duplicates:
        print(filename)


if __name__ == '__main__':

    foldername = sys.argv[1]
    if os.path.isdir(foldername):
        print_duplicate_files((find_duplicate(foldername)))
    else:
        print("Неправильный каталог")
