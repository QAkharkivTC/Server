import requests
import json
import logging
import time

'''
#пример создания пресета
def create_broadcast(): 
    
    r = requests.post('http://localhost/api/v3.3/broadcast/presets/', data = json.dumps({
        "name": "broadcast_name",
        "type": "manualPull",
        "payload": {"audio_codec": "MP3",
                    "video_codec": "H264"}
    }))
    r.status_code
    print(r.status_code)
    print(r.text)

create_broadcast()
'''

def create_broadcast_for_conf():
    for vc in range(2):         #перебираем видео кодеки
        name = "Broadcast manualPull "
        if vc%2==0:
            video_codec = "H264"
            name +=video_codec
        else:
            video_codec = "VP8"
            name +=video_codec

        name+=" + "

        for ac in range(5):     #перебираем аудио кодеки
            if ac == 0:
                audio_codec = "MP3"
                br_name = name+audio_codec
            elif ac == 1:
                audio_codec = "G711U"
                br_name = name+audio_codec
            elif ac == 2:
                audio_codec = "G711A"
                br_name = name+audio_codec
            elif ac == 3:
                audio_codec = "PCM"
                br_name = name+audio_codec
            else:
                audio_codec = "AAC"
                br_name = name+audio_codec

            #отправляем запрос с комбинацией кодеков
            r = requests.post('http://localhost/api/v3.3/broadcast/presets/', data = json.dumps({
                "name": br_name,
                "type": "manualPull",
                "payload": {"audio_codec": audio_codec,
                            "video_codec": video_codec}
                }))
            r.status_code
            print(r.status_code)
            print(r.text)
            

def create_CDNvideo_broadcast():

    r = requests.post('http://localhost/api/v3.3/broadcast/presets/', data = json.dumps({
        "name": "CDNvideo (apukhtin+00000001@trueconf.ru)",
        "type": "cdnvideo",
        "payload":{
            "username": "apukhtin+00000001@trueconf.ru",
            "password": "fQUqpYmP7F"}}))
    r.status_code
    print(r.status_code)
    print(r.text)


def create_YouTube_broadcast_1():

    r = requests.post('http://localhost/api/v3.3/broadcast/presets/', data = json.dumps({
        "name": "YouTube broadcast 1",
        "type": "youtube",
        "payload":{
            "stream_url": "rtmp://a.rtmp.youtube.com/live2",
            "stream_key": "xkz1-d3ap-00dx-6zd3-3fhk",
            "audio_codec": "MP3",
            "video_codec": "H264"}}))
    r.status_code
    print(r.status_code)
    print(r.text)

def create_YouTube_broadcast_2():

    r = requests.post('http://localhost/api/v3.3/broadcast/presets/', data = json.dumps({
        "name": "YouTube broadcast 2",
        "type": "youtube",
        "payload":{
            "stream_url": "rtmp://b.rtmp.youtube.com/live2?backup=1",
            "stream_key": "xkz1-d3ap-00dx-6zd3-3fhk",
            "audio_codec": "MP3",
            "video_codec": "VP8"}}))
    r.status_code
    print(r.status_code)
    print(r.text)

    

def create_manual_broadcast():

    for k in range(2):                  #выбираем тип трансляции: manualPush/manualPull
        if k%2==0:                      #создаем набор пресетов manualPush
            br_type = "manualPush"

            for vc in range(2):         #перебираем видео кодеки
                name = "Broadcast manualPush "
                if vc%2==0:
                    video_codec = "H264"
                    name +=video_codec
                else:
                    video_codec = "VP8"
                    name +=video_codec
                    
                name+=" + "
                
                for ac in range(5):     #перебираем аудио кодеки
                    if ac == 0:
                        audio_codec = "MP3"
                        br_name = name+audio_codec
                    elif ac == 1:
                        audio_codec = "G711U"
                        br_name = name+audio_codec
                    elif ac == 2:
                        audio_codec = "G711A"
                        br_name = name+audio_codec
                    elif ac == 3:
                        audio_codec = "PCM"
                        br_name = name+audio_codec
                    else:
                        audio_codec = "AAC"
                        br_name = name+audio_codec

                    #отправляем запрос с комбинацией кодеков
                    r = requests.post('http://localhost/api/v3.3/broadcast/presets/', data = json.dumps({
                        "name": br_name,
                        "type": br_type,
                        "payload": {"url_publish": "rtsp://qa.trueconf.net/",
                                    "username": "",
                                    "password": "",
                                    "audio_codec": audio_codec,
                                    "video_codec": video_codec,
                                    #"rtp_over_tcp": false,                     #позже дописать как переключать данный флаг
                                    "inactive_receiver_timeout": 60,
                                    "retries": 0,
                                    "retry_delay": 10}
                        }))
                    r.status_code
                    print(r.status_code)
                    print(r.text)
                        
        else:                           #создаем набор пресетов manualPull
            br_type = "manualPull"

            for vc in range(2):         #перебираем видео кодеки
                name = "Broadcast manualPull "
                if vc%2==0:
                    video_codec = "H264"
                    name +=video_codec
                else:
                    video_codec = "VP8"
                    name +=video_codec

                name+=" + "

                for ac in range(5):     #перебираем аудио кодеки
                    if ac == 0:
                        audio_codec = "MP3"
                        br_name = name+audio_codec
                    elif ac == 1:
                        audio_codec = "G711U"
                        br_name = name+audio_codec
                    elif ac == 2:
                        audio_codec = "G711A"
                        br_name = name+audio_codec
                    elif ac == 3:
                        audio_codec = "PCM"
                        br_name = name+audio_codec
                    else:
                        audio_codec = "AAC"
                        br_name = name+audio_codec

                    #отправляем запрос с комбинацией кодеков
                    r = requests.post('http://localhost/api/v3.3/broadcast/presets/', data = json.dumps({
                        "name": br_name,
                        "type": br_type,
                        "payload": {"audio_codec": audio_codec,
                                    "video_codec": video_codec}
                        }))
                    r.status_code
                    print(r.status_code)
                    print(r.text)

def delete_all_broadcaste():                                        #Функция удаления всех шаблонов трансляции для удобства очистки
    
    list_id = []                                                    #создаем пустой список для хранения id шаблонов
    r = requests.get('http://localhost/api/v3.3/broadcast/presets/')#запрашиваем весь список шаблонов
    #r.status_code
    #print(r.status_code)
    #print(r.text)                                                  #распечатываем json всех шаблонов

    media = json.loads(r.text)                                      #json.dumps конвертирует словарь в строку. json.loads конвертирует строку в словарь
    for i in range(len(media['presets'])):                          #проходимся циклом по словарю (определяем количество пресетов)
        list_id.append(media['presets'][i]['id'])                   #в список записываем id каждого пресета
    #print(media['presets'][0]['id'])
        
    for k in range(len(list_id)):                                   #проходимся по заполненному списку и удаляем все шаблоны
        print("Удаляем шаблон трансляции с id "+str(list_id[k]))
        r = requests.delete('http://localhost/api/v3.3/broadcast/presets/'+ str(list_id[k]) +'/')
        r.status_code
        print(r.status_code)



create_manual_broadcast()
create_CDNvideo_broadcast()
create_YouTube_broadcast_1()
create_YouTube_broadcast_2()

#create_broadcast_for_conf()
#delete_all_broadcaste()

'''
def create_wowza_stream_engine_broadcast()
create_wowza_stream_engine_broadcast()

def create_wowza_stream_cloud_broadcast()
create_wowza_stream_cloud_broadcast()

def create_youtube_broadcast()
create_youtube_broadcast()
'''
