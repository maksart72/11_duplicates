import sys, re, os
folder = sys.argv[1]

def indexation(folder):
    for root, dirs, files in os.walk(folder):
        file_index={}
        i=1
        for file in files:
            #print(file)
            file_index[i]=file,os.path.join(root, file),os.path.getsize(os.path.join(root, file))
            print(file_index[i])
            i =i+1
    return(file_index)

if __name__ == '__main__':
    #print(indexation(folder))
    key = indexation(folder)
    word_frequence = {}
    for key[0] in indexation(folder):
        if key[0] in word_frequence:
            frequence = word_frequence[key[0]]
            word_frequence[key[0]]=frequence+1
        else:
            word_frequence[key[0]]=1

    print(word_frequence)

"""
              if file.endswith(".xml"):
                print(os.path.join(root, file))
                print(os.path.getsize(os.path.join(root, file))
        else
        print(folder)

word_frequence = {}
    for key in voc:
        key = key.lower()
        if key in word_frequence:
            frequence = word_frequence[key]
            word_frequence[key]=frequence+1
        else:
            word_frequence[key]=1


"""