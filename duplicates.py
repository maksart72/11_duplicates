import sys, re, os
from collections import Counter

def create_files_index(folder): #Создаем список файлов в виде строки из имени файла и его размера. Например 'test.txt:0'
    files_index=[]
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            files_index.append(str(file)+':'+str(file_size))
    return files_index

def find_duplicate(files_index): #Находим одинаковые строки из списка файлов, используем Counter для подсчета и вывода только значений >1
    counts = Counter(files_index)
    files_duplicate=[]
    for i in counts:
        if counts[i]>1:
            files_duplicate.append(i)
    return(files_duplicate)

def print_duplicate_files(files_duplicate,folder): #Из списка одинаковых строк выделяем имя файла через partition и выводим все пути где лежат файлы с таким именем.
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

def main(folder):
    if os.path.isdir(folder):
        DuplicateList = print_duplicate_files(find_duplicate(create_files_index(folder)),folder)
        for filepath in DuplicateList:
            print(filepath)
    else:
        print("Неправильный каталог")
    return('Программа выполнена!')
if __name__ == '__main__':
    folder = sys.argv[1]
    print(main(folder))