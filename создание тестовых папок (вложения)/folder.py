import os

#global path 
#global name
path = "C://test_folder//"
name = "test"

def make_folder(n):
    #path = "C://test_folder//"
    #name = "test"
    #path += name + str(n)+"//"
    #os.mkdir(path)
    
    if n == 0:
        pass
    else:
        path += name + str(n)+"//"
        os.mkdir(path)
        make_folder(n-1)



make_folder(10)

