import requests
import json
import logging
import time


def create_broadcast(N):
    for i in range(N):
        
        #   тут можно изменить тело запроса, тем самыс создавая шаблоны трансяций с другими настройками
        
        r = requests.post('http://localhost/api/v3.3/broadcast/presets/', data = json.dumps({
            "name": "broadcast_"+str(i),
            "type": "manualPull",
            "payload": {"audio_codec": "MP3",
                        "video_codec": "H264"}
        }))
        r.status_code
        print(r.status_code)
        print(r.text)

    make_list()



def make_list():
    r = requests.get('http://localhost/api/v3.3/broadcast/presets/')
    print(r.status_code)
    print(r.text)

    media = json.loads(r.text)
    for i in range(len(media['presets'])):
        id_preset = media['presets'][i]['id']
        with open('list_id_broadcasts.txt', 'at') as f:
            f.write(id_preset + "\n")



create_broadcast(100)
#make_list()


#   создаем N шаблонов трансялции (само тело запроса зожно в дальнейщем вынести в отдельную переменную)
#
#   после создания всех шаблонов вызывается функция которая создаст список id-ков трансялций и запишет в файл
#   если файл существует , то результаты будут записывася в конец файла, так что лучше удалить txt файл перед запуском
#
#   файл с id-ками понадобится при запуске других скриптов
#
