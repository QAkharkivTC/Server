import os

path = "C://test_folder//"
name = "test"

def make(n):
    path = "C://test_folder//"
    for i in range(n):
        path = path + str(i) + "//"
        os.mkdir(path)
        make_file(path, i)

def make_file(path, i):
    with open(path + 'textfile_'+str(i)+'.txt', 'tw', encoding='utf-8') as f:
        f.write("test test test test test test test test test test test ")

        

make(10)
