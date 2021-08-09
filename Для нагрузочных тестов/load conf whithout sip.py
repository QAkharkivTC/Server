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
        {"id": "user30",
         "display_name": "user30"}]
        
    for u in range(N_users):
        invitations.append({
            "id": "bot_"+str(u)+"",
            "display_name": "bot_"+str(u)+""
            })
          
    return invitations

def create_conf(N_conf):

    for i in range(N_conf):
        
        #timestamp = int(time.time())+120
        #нужно указать время 00:00 следующего дня, для запуска в формате unix-time https://www.unixtimestamp.com/index.php
        timestamp =1611360000
        temp = i*10
        hour = temp //60
        minute = temp % 60
        
        payload = {
            "id": "xx000"+str(i)+"",
            "type": 0,
            "topic": "Нагрузочная конференция "+str(i)+" ("+str(hour)+":"+str(minute)+")",
            "owner": "user30@aa111.trueconf.net",                      #указать домен сервера (при использовании с другими серверами)
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

        url = 'http://localhost/api/v3.1/conferences'
        headers = {'content-type': 'application/json'}
        start = time.monotonic()
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        response.status_code
        print("Конференция #",i, "создана с результатом ",response.status_code)
        print(response.text)

    
count =144

create_conf(count)
