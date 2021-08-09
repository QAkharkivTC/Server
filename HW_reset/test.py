import os

path = os.getcwd()
#print(os.listdir(path))
files = os.listdir(path)
files_txt = [i for i in files if i.endswith('.p12')]
print(str(files_txt[0]))
