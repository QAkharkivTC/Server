import requests
import json
import urllib3
import certifi
import ssl
import random
import csv

import io
import chardet
import codecs

# https://10.130.0.32/api/v3.2/users?&&page_size=200&login_name=bot&display_name=bot&first_name=bot&last_name=bot&email=bot

list_user_id = []

def make_list_users(ip, token, user_DN):                                #составляю список id тех у кого буду менять dn
    ssl._create_default_https_context = ssl._create_unverified_context
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    page_id = 0
    
    while True:
        r = requests.get('https://'+ip+'/api/v3.2/users?&&page_size=200&page_id='+str(page_id)+'&display_name='+'&login_name='+user_DN+'&first_name='+user_DN+'&last_name='+user_DN+'&access_token='+token+'',verify=False)
        r.status_code
        #print(r.status_code)
        #print(r.text)
        media = json.loads(r.text)
        cheak_num_page = media['next_page_id']
        #print(len(media['users']))

        for i in range(len(media['users'])):
            list_user_id.append(media['users'][i]['id'])
            
        if cheak_num_page == -1:
            break
        else:
            page_id+=1
    
    return list_user_id


def get_random_name_surname(random_number, path):                       #получаю рандомное имя/фамилия
    if path == 'name':
        row_num = 0
    elif path == 'surname':
        row_num = 1
    else:
        row_num = 0
        
    with open(source, encoding='cp1251') as r_file:
    #with open(source, encoding='utf-16') as r_file:
        file_reader = csv.reader(r_file, delimiter = ";")   # Создаем объект reader, указываем символ-разделитель ","
        count = 0                                           # Счетчик для подсчета количества строк и вывода заголовков столбцов

        for row in file_reader:
            if count == 0:
                pass
            elif count == random_number:
                #print(row[row_num])
                temp = row[row_num]
            else:
                pass
            count += 1
    return temp            
            

def rename_users(ip, token):                                #сама функция переименовывания
    ssl._create_default_https_context = ssl._create_unverified_context
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    make_list_users(ip, token, user_DN)
    print(list_user_id)
    
    for i in range(len(list_user_id)):
        name = get_random_name_surname(random.randint(1, 400), 'name')
        surname = get_random_name_surname(random.randint(1, 400), 'surname')
        
        r = requests.put('https://'+ip+'/api/v3.3/users/'+list_user_id[i]+'?access_token='+token+'', data= {
             
            "display_name": name +" "+ surname,
            "first_name": name,
            "last_name": surname
             
        }, verify=False)
        r.status_code
        #print("User ", k+1, " from ", N, "result: ", r.status_code)
        #print(r.text.encode("utf-8"))
        print(r.status_code)
        print(r.text)
    #pass


#source = "test_name_1.csv"
#source= "list_of_russian_male_names.csv"
source= "test_name.csv"
#source= "forin_names.csv"
#source= "list_of_european_names.csv"





ip = '10.130.0.32'
#ip = 'qa3.trueconf.net'

token = '1Top3R0Hb81vGUZMkbDBGbdtUmPZVPX6'

user_DN = 'test_100'


rename_users(ip, token)    
