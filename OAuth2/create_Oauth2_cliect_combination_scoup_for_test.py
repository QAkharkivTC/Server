import requests
import json
import logging
import time
import urllib3
import certifi
import ssl

#                   тестовые данные для проверки:
#
#for test           qa3.trueconf.net
#sec_key            1Top3R0Hb81vGUZMkbDBGbdtUmPZVPX6


client_id = ''
client_name = ''
client_secret = ''
access_token = ''
list_client_id = []
scope_test_list = ''
client_name = ''

def create_test_combination_clients():
    """Создаем набор клиентов с различными комбинациями прав (от "без прав" до "все права") и получаем их токены (записав их в файл)"""
    
    for i in range(40):                                                         #это количество всех прав с которыми можно создать клиент ( в случае изменений на сервере дописать их в scope_list и изменить их количество
        client_name                                                             #тут не глобальная переменная, что бы передать имя клиента в функции
        scope_test_list                                                         #так же не глобальная переменная что бы передать комбинацию прав клиента
        create_data_list_for_test(i)                                            #для i-го клиента на основе переменных client_name и scope_test_list создаем набор прав и его имя
        create_client(localhost, token, scope_test_list, client_name)           #создаем клиент с переданым именем и правами
        make_token(localhost, client_id, client_secret, token, client_name)     #создаем токен для созданого клиента и записываем в файл list_clients_tokens.txt
        

def create_data_list_for_test(n):
    """Создаем набор прав и имя клиента в зависимости от переданого значение (количество вклченных прав из списка)"""
    
    scope_list = ["conferences ", "conferences:read ", "conferences:write ", "conferences.participants ", "conferences.participants:read ","conferences.participants:write ",
                  "conferences.operators:read ", "conferences.operators:write ", "conferences.invitations ", "groups ",  "groups:read ", "groups:write ", "groups.users ",
                  "groups.users:read ", "groups.users:write ", "users users:read ","users:write ", "users.avatar:read ", "users.avatar:write ", "users.addressbook ",
                  "users.addressbook:read ", "users.addressbook:write ", "templates.conferences:read ", "templates.conferences:write ", "directory.servers:read ", "logs.calls:read ",
                  "logs.calls.participants:read ", "logs.calls.invites:read ", "conferences.video_layouts:read ", "conferences.video_layouts:write ",
                  "conferences.video_layouts.personal:read ","conferences.video_layouts.personal:write ", "conferences.records ", "conferences.records:read ",
                  "conferences.records:write ", "conferences.sessions:read ", "conferences.sessions.participants:read ", "conferences.sessions.podiums.participants:read ",
                  "conferences.sessions.podiums.participants:write"]
    global scope_test_list
    global client_name

    for i in range(n):
        scope_test_list += scope_list[i]

    client_name = 'test_client_' + str(n)    
    
    return scope_test_list, client_name


def create_client(localhost, token, scope_test_list, client_name):
    """Создаем клиент по получиным параметрам(имя клиента и набор доступных функций для него) """

    ssl._create_default_https_context = ssl._create_unverified_context
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    r = requests.post('https://'+localhost+'/api/v3/api-clients?access_token='+token+'',
                      data= {"client_name":""+client_name+"",
                             "redirect_uri":"https://localhost",
                             "scope":""+scope_test_list+""}, verify=False)

    r.status_code
    print("API OAuth2 client "+client_name+" created with code: ", r.status_code)
    #print(r.text)
    media = json.loads(r.text)
    
    #После создания записываем в глобальные переменные для того что бы ф-ия make_token создала токен
    global client_id
    #global client_name
    global client_secret
    client_id = media['client']['id']
    client_name = media['client']['client_name']
    client_secret = media['client']['client_secret']
    

def make_token(localhost, client_id, client_secret, token, client_name):
    """Создаем access_token клиента. Результат записывается в файл list_clients_tokens.txt"""
    
    ssl._create_default_https_context = ssl._create_unverified_context
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    data = {'grant_type':'client_credentials', 'client_id': client_id , 'client_secret': client_secret}
    headers = {'Cache-Control':'max-age=0',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
        'Content-Type':'application/x-www-form-urlencoded',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer':'https://www.groupon.com/signup',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'es-ES,es;q=0.8'
        }
    
    r = requests.post('https://'+localhost+'/oauth2/v1/token?access_token='+token+'', headers=headers , data=data, verify=False)

    global access_token
    media = json.loads(r.text)
    access_token = media['access_token']
    #print("API OAuth2 token was made: ", r.status_code, " client_access_token: ", access_token)
      
    with open('list_clients_tokens.txt', 'at') as f:
        f.write(client_name + " access_token: " + access_token + "\n")
    

def delete_client(localhost, client_id, token):
    """Удаляем клиент с указаным id"""
    
    ssl._create_default_https_context = ssl._create_unverified_context
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    r = requests.delete('https://'+localhost+'/api/v3/api-clients/'+client_id+'?access_token='+token+'', verify=False)
    print("API OAuth2 client with id: " +client_id+ " was delete  with result: ", r.status_code)


def delete_all_client(localhost, list_client_id, token):
    """Удаляем все записи на странице /admin/api/clients/"""

    ssl._create_default_https_context = ssl._create_unverified_context
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    get_client_list(localhost, token)
    for i in range(len(list_client_id)):
        delete_client(localhost, list_client_id[i], token)
        
    
def get_client_list(localhost, token):
    """Получаем список клиентов их secret и id. Результат записывается в файл list_client.txt"""
    
    ssl._create_default_https_context = ssl._create_unverified_context
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    r = requests.get('https://'+localhost+'/api/v3/api-clients?access_token='+token+'', verify=False)

    r.status_code
    media = json.loads(r.text)

    for i in range(len(media['clients'])):
        client_id = media['clients'][i]['id']
        client_name = media['clients'][i]['client_name']
        client_secret = media['clients'][i]['client_secret']
        list_client_id.append(client_id)
        with open('list_clients.txt', 'at') as f:
            f.write(client_name + " " + client_id + " " + client_secret + "\n")
    print("List was creat")



localhost = str(input("Укажите адрес "  ))
token = str(input("Укажите токен "  ))    


create_test_combination_clients()


#print(list_client_id)
#print("access_token: ", access_token)

#create_client(localhost, token)
#make_token(localhost, client_id, client_secret, token)
#get_client_list(localhost, token)
#delete_client(client_id)
#delete_all_client(localhost, list_client_id, token)
