import sys, re, os
from collections import Counter

def create_files_index(folder):
    files_index=[]
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            files_index.append(str(file)+':'+str(file_size))
    return files_index

def find_duplicate(files_index):

    counted_files = Counter(files_index)
    duplicated_files = [filename for filename in counted_files if counted_files[filename]>1]
    return duplicated_files


def print_duplicate_files(files_duplicate,folder):
    
    files_name = [] 
    for i in files_duplicate:
        file_name = i.partition(':')
        files_name.append(file_name[0])
  
    duplicates=[]
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file in files_name:
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                duplicates.append(str(file)+' in '+str(os.path.join(root))+'\\')
    duplicates.sort()

    return duplicates
  
if __name__ == '__main__':
    
    folder = sys.argv[1]
    if os.path.isdir(folder):
        print(print_duplicate_files(find_duplicate(create_files_index(folder)),folder))
    else:
        print("Неправильный каталог")
        