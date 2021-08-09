import os
import json
import requests                                                 # pip install requests  |or| python -m pip install requests
import urllib3
import certifi
import ssl
import http.client
from OpenSSL import crypto                                      # pip install OpenSSL
from requests_pkcs12 import post
from requests import Session
from requests_pkcs12 import Pkcs12Adapter                       # pip install requests_pkcs12


# https://crm.trueconf.com/server/view/AA112&act=resethw&comment=111
# https://pypi.org/project/requests-pkcs12/
# https://gist.github.com/erikbern/756b1d8df2d1487497d29b90e81f8068


ssl._create_default_https_context = ssl._create_unverified_context
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
url = 'https://crm.trueconf.com'
headers = { 
           'Accept': '*/*', 
           'Accept-Encoding': 'gzip, deflate, br', 
           'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',  
           'Content-Length': '32', 
           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
           #'Cookie': '_ga=GA1.2.1332897830.1614871631; rl_anonymous_id=%2247e2eef8-5e9a-4bc2-bd66-fe04da37c691%22;'+
           #'rl_trait=%7B%7D; rl_user_id=%22dy6pbqybfjddbmf1oq37sqjsee%22; _hjid=302beb92-8140-40d6-83fa-53b35387b313; PHPSESSID=kqf8c2kk4ik25tck9bbm25q8n2',
           'Origin': 'https://crm.trueconf.com',
           #'Referer': 'https://crm.trueconf.com/server/view/AA111',
           'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
           'sec-ch-ua-mobile': '?0',
           'sec-fetch-dest': 'empty',
           'Sec-Fetch-Mode': 'cors', 
           'Sec-Fetch-Site': 'same-origin', 
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
           'X-Requested-With': 'XMLHttpRequest'
           }
data = {"act=resethw&comment=111"}

l = []
list_keys = []

def read_list_txt():
    f = open('list_keys.txt', 'r')
    for line in f:
        l.append(line) 
    global list_keys
    list_keys = [line.rstrip() for line in l]

def read_pass():
    f = open('password.txt', 'r')
    global password
    for line in f:
        password = line.strip()
    return password

def get_ssl_file_name():
    global filename
    path = os.getcwd()
    files = os.listdir(path)
    files_txt = [i for i in files if i.endswith('.p12')]
    filename = str(files_txt[0])
    return filename
    
        
#read_list_txt()
#print(list_keys)


def rest_HW():
    read_pass()
    read_list_txt()
    get_ssl_file_name()
    
    for i in range(len(list_keys)):
        with Session() as s:
            #s.mount('https://crm.trueconf.com', Pkcs12Adapter(pkcs12_filename='apukhtin.p12', pkcs12_password='5G2d6jFnH2ap'))
            s.mount('https://crm.trueconf.com', Pkcs12Adapter(pkcs12_filename=filename, pkcs12_password=password))
            r = s.get('https://crm.trueconf.com/server/view/'+str(list_keys[i])+'')
            #print(r.text)
            
            # отвязываю HW
            r = s.post('https://crm.trueconf.com/server/view/'+str(list_keys[i])+'', data=data, headers=headers)
            print(r.text)
            r = s.get('https://crm.trueconf.com/server/view/'+str(list_keys[i])+'')


rest_HW()
