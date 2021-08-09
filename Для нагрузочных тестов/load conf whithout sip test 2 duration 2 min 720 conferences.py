import json
import requests                                                 # pip install requests
import time
import logging

def list_invitations (N_users):
    '''
    Функция возвращает список пользователей для конференции
    от user0 до userN-1
    
    '''
    invitations = [
        {"id": "artem1",
         "display_name": "artem1"}]
        
    for u in range(N_users):
        invitations.append({
            "id": "bot_1__"+str(u)+"",
            "display_name": "bot_1__"+str(u)+""
            })
          
    return invitations

def create_conf(N_conf):

    for i in range(N_conf):
        
        #timestamp = int(time.time())+120
        #нужно указать время 00:00 следующего дня, для запуска в формате unix-time https://www.unixtimestamp.com/index.php
        timestamp =1611360000
        temp = i*2             #тут надо указать какой длительности конференцию мы хотим (изначально 10 минут)
        hour = temp //60
        minute = temp % 60
        
        payload = {
            "id": "999000"+str(i)+"",
            "type": 0,
            "topic": "Нагрузочная конференция "+str(i)+" ("+str(hour)+":"+str(minute)+")",
            "owner": "artem1@aa111.trueconf.name",                      #указать домен сервера (при использовании с другими серверами)
            "invitations": list_invitations(36),
            "description": "Test conf "+str(i)+"",
            "max_podiums": 36,
            "max_participants": 36,
            "schedule": {
                "type": 0,
                "start_time": timestamp + 120*i,
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

        url = 'http://localhost/api/v3.1/conferences'
        headers = {'content-type': 'application/json'}
        start = time.monotonic()
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        response.status_code
        print("Конференция #",i, "создана с результатом ",response.status_code)
        print(response.text)

    
#count =144
count =720

create_conf(count)
