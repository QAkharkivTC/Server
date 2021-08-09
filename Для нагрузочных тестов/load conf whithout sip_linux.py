import json
import requests                                                 # pip install requests
import time
import logging
import urllib3
import certifi
import ssl

def list_invitations (N_users):
    '''
    Функция возвращает список пользователей для конференции
    от user0 до userN-1
    
    '''
    invitations = [
        {"id": "33",
         "display_name": "33"}]
    '''    
    for u in range(N_users):
        invitations.append({
            "id": "bot_4__"+str(15 + u)+"",
            "display_name": "bot_4__"+str(15 + u)+""
            })
            '''
    for u in range(N_users):
        invitations.append({
            "id": "user"+str(u)+"",
            "display_name": "user"+str(u)+""
            })
          
    return invitations

def create_conf(N_conf):
    ssl._create_default_https_context = ssl._create_unverified_context
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    for i in range(N_conf):
        
        #timestamp = int(time.time())+120
        #нужно указать время 00:00 следующего дня, для запуска в формате unix-time https://www.unixtimestamp.com/index.php

        #   temp = i*2 count = 720
        #   temp = i*1 count = 1440
        #   temp = i*10 count = 144
        #   temp = i*5 count = 288
        #   temp = i*0.5 count = 2880
        #
        
        timestamp =1611360000
        temp = i*1                 #тут надо указать какой длительности конференцию мы хотим (изначально 10 минут)
        hour = temp //60
        minute = temp % 60
        
        payload = {
            "id": "first000"+str(i)+"",
            "type": 0,
            "topic": "Нагрузочная конференция  2 "+str(i)+" ("+str(hour)+":"+str(minute)+")",
            "owner": "artem1@aa11h.trueconf.name",                      #указать домен сервера (при использовании с другими серверами)
            "invitations": list_invitations(10),
            "description": "Test conf "+str(i)+"",
            "max_podiums": 36,
            "max_participants": 36,
            "schedule": {
                "type": 0,
                "start_time": timestamp + 600*i,
                "duration": 600,
                "time": "0"+str(hour)+":0"+str(minute)+"",
                "time_offset": 120,
                "days": [
                    "monday",
                    "tuesday",
                    "wednesday",
                    "thursday",
                    "friday",
                    "saturday",
                    "sunday"
                        ]
                    }
                }

        url = 'https://10.130.2.163/api/v3.3/conferences?access_token=bp4nqlUGWTb7khzsNTTCVzCT8dD3LwMV'
        headers = {'content-type': 'application/json'}
        start = time.monotonic()
        response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)
        response.status_code
        print("Конференция #",i, "создана с результатом ",response.status_code)
        print(response.text)

    
count = 1440

create_conf(count)
