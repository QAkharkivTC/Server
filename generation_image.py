from PIL import Image
import requests
import json
import logging
import time
import urllib3
import certifi
import ssl

#тестовые данные для проверки:
#localhost = "qa3.trueconf.net"
#token = "1Top3R0Hb81vGUZMkbDBGbdtUmPZVPX6"

users_id = []

def generation_image():         #создаем изображения 
    count = 0
    for r in range(16):
        for g in range(16):
            for b in range(16):
                count+=1
                img = Image.new('RGB', (400, 400), (r*16, g*16, b*16))
                #img.show()
                img.save("img_"+str(count)+".jpg")
                print('make img_'+str(count)+'.jpg')


def get_user_info(localhost, token):
    
    """
получаем пользователей проходимся по каждому пользователю смотри поле avatar если пусто то записываем id  пользователя
    """

    ssl._create_default_https_context = ssl._create_unverified_context
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    page_id = 0
    
    while True:
        
        r = requests.get('https://'+localhost+'/api/v3.3/users?&page_size=200&page_id='+str(page_id)+'&access_token='+token+'',verify=False)
        r.status_code
        #print(r.status_code)
        #print(r.text)
        media = json.loads(r.text)
        cheak_num_page = media['next_page_id']
        #print(len(media['users']))

        for i in range(len(media['users'])):
            #print(media['users'][i]['avatar'])
            if media['users'][i]['avatar'] == None:
                users_id.append(media['users'][i]['id'])
            else:
                pass
            
        if cheak_num_page == -1:
            break
        else:
            page_id+=1
            

def get_all_users(localhost, token):
    ssl._create_default_https_context = ssl._create_unverified_context
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    page_id = 0
    
    while True:
        r = requests.get('https://'+localhost+'/api/v3.3/users?&page_size=200&page_id='+str(page_id)+'&access_token='+token+'',verify=False)
        r.status_code
        media = json.loads(r.text)
        cheak_num_page = media['next_page_id'] #print(len(media['users']))

        for i in range(len(media['users'])):
            users_id.append(media['users'][i]['id'])
            
        if cheak_num_page == -1:
            break
        else:
            page_id+=1


def load_image_for_users(localhost, token):
    """
    берем список пользователей без аватара и добавляем аватар из диретории
    """
    ssl._create_default_https_context = ssl._create_unverified_context
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    for i in range(len(users_id)):
        user = users_id[i]
        #print(user)
        file_name = 'img_'+str(i+1)+'.jpg'
        url = 'https://'+localhost+'/api/v3.3/users/'+user+'/avatar?access_token='+token+''
        files=[('image',(file_name, open(file_name,'rb'),'image/jpeg'))]
        #headers = {'Cookie': 'PHPSESSID=dbc583b6532145cf95a6d4afeefb4a4a'}
        payload = {'Cache-Control':'max-age=0',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
            'Content-Type':'multipart/form-data',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer':'https://www.groupon.com/signup',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'es-ES,es;q=0.8'
            }

        r = requests.post( url, data=payload, files=files, verify=False)
        #print(r.status_code)
        #print(r.text)
        print("Пользователю "+user+" был добавлен аватар "+file_name+" Результат: "+str(r.status_code)+"")


localhost = input("Введие ip адрес: ")
token = input("Введите токен: ")

#generation_image()                         #генерируем файлы для аватаров (этот файл разместить в какой нибудь папке иначе засрете рабочий стол файлами)
get_user_info(localhost, token)             #находим пользователей без аватаров и добавляем их в список
load_image_for_users(localhost, token)      #добавляем аватарки пользователям из созданного списка
#get_all_users(localhost, token)            #если хотим переписать все аватары пользователей то раскоментировать эту строку и закоментировать вызов функции get_user_info()
