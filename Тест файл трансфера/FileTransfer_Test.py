import os
import json
import requests                                             
import urllib3
import certifi
import ssl
import http.client
from OpenSSL import crypto                                      
from requests_pkcs12 import post
from requests import Session
from requests_pkcs12 import Pkcs12Adapter

l = []
list_keys = []

def read_list_txt():
    f = open('расширения.txt', 'r')
    for line in f:
        l.append(line) 
    global list_keys
    list_keys = [line.rstrip() for line in l]

    return list_keys
    #print (list_keys)

#read_list_txt()

def make_file():
    list_name = read_list_txt()

    for i in range(len(list_name)):
                   name = "New_File"+str(i)+"."+list_name[i]+""
                   my_file = open(name, "w+")
                   #my_file = open("New_File"+str(i)+list_name[i]+"", "w+")
                   my_file.write("и еще кое-что!00000000000000000000000000000000000000001231234123421342134123421342134324123421341234213")
                   my_file.close()
                   #f = open(name,"wb")
                   #f.truncate(451824)
                   ##f.write('\0')
                   #f.close()
                   

#print(read_list_txt())
make_file()
