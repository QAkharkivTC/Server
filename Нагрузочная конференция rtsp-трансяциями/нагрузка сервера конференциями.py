import json
import requests                                                 # pip install requests
import time
import logging


l = []
list_id_preset = []

def read_list_broadcaste():
    f = open('list_id_broadcasts.txt', 'r')                     # читаем id шаблонов трансялций из файла (созданого скриптом make_list_broudcaste.py)
    for line in f:
        l.append(line) 
    global list_keys
    list_id_preset = [line.rstrip() for line in l]

    return list_id_preset

def create_conf(N_conf):

    list_preset = read_list_broadcaste()

    for i in range(N_conf):
        time_to_run = round(time.time())
        payload = {
            "id": "cid_"+str(i)+"",
            "type": 0,
            "topic": "Нагрузочная # "+str(i)+"",
            "owner": "11@aa111.trueconf.name",                      # указать домен сервера (при использовании с другими серверами) или указать id существующего пользователя в сервере
            "invitations": [
                {"id": "bot_"+str(i)+"",
                 "display_name": "bot_"+str(i)+""}],                # на сервере должны быть запущены (и созданы) боты с id bot_(N) в количестве равном количеству создваемых конференций
            "description": "Test conf "+str(i)+"",
            "max_podiums": 36,
            "max_participants": 36,
            "broadcast_enabled": True,
            "broadcast_id": ""+list_preset[i]+"",                   # используем id шаблонов трансялций (1 шаблон для 1 конференции)
            "schedule": {
                "type": 1,
                "start_time": time_to_run + 10 + i*5,               # время запуска конференций (текущий момент + 10сек + порядковый номер конференции*5) что бы конференции не запускались в один момент
                "duration": 1200                                    #  длительность конференций 20 минут
                    }
                }

        url = 'http://localhost/api/v3.1/conferences'
        headers = {'content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        response.status_code
        print("Конференция #",i, "создана с результатом ",response.status_code)
        print(response.text)

    
count =100                                  # указываем количество конференций (не больше чем создано шаблонов трансяций или созданых и запущеных ботов)

create_conf(count)
