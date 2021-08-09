import json
import requests                                                 # pip install requests
import time
import logging

t = str(time.time())
logging.basicConfig(filename="log create conferenses "+t+".log", format='%(asctime)s %(levelname)s:%(message)s', level=logging.INFO)

def list_invitations (N_users):
    '''
    Функция возвращает список пользователей для конференции
    от user0 до userN-1
    '''
    invitations = []
    for u in range(N_users):
        invitations.append({
            "id": "user"+str(u)+"",
            "display_name": "user"+str(u)+""
            })
    return invitations

def creat_payload (id_conf, y, k, max_participants, max_podiums):
    '''
    Функция создает тело запроса для создания конференции
    '''
    payload = {
        "id": "200000"+str(id_conf)+"",
        "type": str(y),
        "topic": "Test conf "+str(id_conf)+"",
        "owner": "user11@aa111.trueconf.name",                      #указать домен сервера (при использовании с другими серверами)
        "invitations": list_invitations(max_participants),
        "description": "Test conf "+str(k)+"",
        "max_podiums": str(max_podiums),
        "max_participants": str(max_participants),
        "pin_enabled": True,
        "pin": "0"+str(id_conf)+"",
        "schedule": {"type": -1}
            }
    return payload

def schedule(type_s):
    '''
    функция генерирует расписание для конференции
    '''
    schedule = {}
    if type_s == 0:                                                 #-1 без расписания
        schedule.update({"type": -1})
        
    elif type_s == 1:                                               #0 - weekly
        timestamp = int(time.time())+120
        schedule.update({"type": 0,
        "start_time": timestamp,
        "duration": 3600,
        "time": "11:30",
        "time_offset": 180,
        "days": ["monday","tuesday","wednesday"]})
        
    else:                                                           #1 одноразовая
        timestamp = int(time.time())+120
        schedule.update({"type": 1,
        "start_time": timestamp,
        "duration": 600})
    return schedule
    

def send_response (payload, id_conf):
    '''
    Функция выполняет отправку запроса на сервер с уже подготовленным телом
    а после печатает результат отправки запроса
    '''
    url = 'http://localhost/api/v3.4/conferences'
    headers = {'content-type': 'application/json'}
    start = time.monotonic()
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    response.status_code
    result = time.monotonic() - start
    print("Конференция #",id_conf, "создана с результатом ",response.status_code)
    print(response.text)
    logging.info(" Conferenses"+ str(id_conf) +" Status code "+ str(response.status_code) + " Lead time: " + str(result) + " seconds.")
    if response.status_code != 200:
        logging.info(payload)
        logging.info(response.text)

    create_templates(payload, id_conf)                              #здесь включается/отключается создание шаблонов конференций

    
def create_conf(N_conf):
    '''
    Функция создает набор конференциий N*6
    (внутрениие:(симметричные, ассиметричные,ролевые),
    публичные: (симметричные, ассиметричные,ролевые))
        
    '''

    id_conf = 0
    for k in range(N_conf):
        for type_conf in range(3):                                  #выбираем тип конференции (0 - симметричная, 1 - ассиметричная, 3 - ролевая)
            if type_conf  == 0:
                y = 0
                max_podiums = 36                                    # max_podiums - зависит от лицензии выданой для сервера
                max_participants = 36	                            # max_participants - зависит от лицензии выданой для сервера
                type_conf_name = "симметричная"
            elif type_conf == 1:
                y = 1
                max_podiums = 1
                max_participants = 36
                type_conf_name = "ассиметричная"
            else:
                y = 3
                max_podiums = 6
                max_participants = 300
                type_conf_name = "ролевая"
                
            for ty2_conf in range (2):                              #выбираем вид конференции (внутренняя, публичная)
                if ty2_conf%2 == 0:                                 #публичная
                    payload = creat_payload(id_conf, y, k, max_participants, max_podiums)
                    payload.update({"allow_guests":True})
                    mode_conf = "публичная"
                    for t in range(3):                              #выбираем тип расписания для типа конференции
                        if t == 0:                                  #-1 - without schedule
                            shed = "/без расписания/"
                            type_s = str(t)
                            sch1={}
                            sch1.update(schedule(t))
                            payload.update({"schedule": sch1})
                            id_conf+=1
                            payload.update({"id": "2000"+str(id_conf)+""})
                            payload.update({"topic": "Test conf "+str(id_conf)+" " +mode_conf + shed + type_conf_name+" "+str(max_podiums)+"*"+str(max_participants)+""})
                        elif t == 1:                                #0 - weekly
                            shed = "/с расписанием/"
                            type_s = str(t)
                            sch1={}
                            sch1.update(schedule(t))
                            payload.update({"schedule": sch1})
                            id_conf+=1
                            payload.update({"id": "2000"+str(id_conf)+""})
                            payload.update({"topic": "Test conf "+str(id_conf)+" " +mode_conf + shed + type_conf_name+" "+str(max_podiums)+"*"+str(max_participants)+""})
                        else:                                       #1 - one-time
                            shed = "/одноразовая/"
                            type_s = str(t)
                            sch1={}
                            sch1.update(schedule(t))
                            payload.update({"schedule": sch1})
                            id_conf+=1
                            payload.update({"id": "2000"+str(id_conf)+""})
                            payload.update({"topic": "Test conf "+str(id_conf)+" " +mode_conf + shed + type_conf_name+" "+str(max_podiums)+"*"+str(max_participants)+""})
                        
                        send_response (payload, id_conf)

                else:                           
                    payload = creat_payload(id_conf, y, k, max_participants, max_podiums)
                    payload.update({"allow_guests":False})          #внутренняя
                    mode_conf = "внутренняя"
                    
                    for t in range(3):                              #выбираем тип расписания для типа конференции
                        if t == 0:                                  #-1 - without schedule
                            shed = "/без расписания/"
                            type_s = str(t)
                            sch1={}
                            sch1.update(schedule(t))
                            payload.update({"schedule": sch1})
                            id_conf+=1
                            payload.update({"id": "2000"+str(id_conf)+""})
                            payload.update({"topic": "Test conf "+str(id_conf)+" " +mode_conf + shed + type_conf_name+" "+str(max_podiums)+"*"+str(max_participants)+""})
                        elif t == 1:                                #0 - weekly
                            shed = "/с расписанием/"
                            type_s = str(t)
                            sch1={}
                            sch1.update(schedule(t))
                            payload.update({"schedule": sch1})
                            id_conf+=1
                            payload.update({"id": "2000"+str(id_conf)+""})
                            payload.update({"topic": "Test conf "+str(id_conf)+" " +mode_conf + shed + type_conf_name+" "+str(max_podiums)+"*"+str(max_participants)+""})
                        else:                                       #1 - one-time
                            shed = "/одноразовая/"
                            type_s = str(t)
                            sch1={}
                            sch1.update(schedule(t))
                            payload.update({"schedule": sch1})
                            id_conf+=1
                            payload.update({"id": "2000"+str(id_conf)+""})
                            payload.update({"topic": "Test conf "+str(id_conf)+" " +mode_conf + shed + type_conf_name+" "+str(max_podiums)+"*"+str(max_participants)+""})
                        
                        send_response(payload, id_conf)


def delete_all_conf():
    list_id = []                                                    #создаем пустой список для хранения id конференций
    r = requests.get('http://localhost/api/v3.4/conferences/')      #запрашиваем весь список конференций
                                                                        #r.status_code
                                                                        #print(r.status_code)
                                                                        #print(r.text)  #распечатываем json всех конференций

    media = json.loads(r.text)                                      #json.dumps конвертирует словарь в строку. json.loads конвертирует строку в словарь
    for i in range(len(media['conferences'])):                      #проходимся циклом по словарю (определяем количество конференций)
        list_id.append(media['conferences'][i]['id'])               #в список записываем id каждой конференции
                                                                    #print(media['presets'][0]['id'])
        
    for k in range(len(list_id)):                                   #проходимся по заполненному списку и удаляем все конференции
        print("Удаляем конференцию с id "+str(list_id[k]))
        r = requests.delete('http://localhost/api/v3.4/conferences/'+ str(list_id[k]) +'/')
        r.status_code
        print(r.status_code)

def create_templates (payload, id_conf):
    temp_payload ={
        "id": str(id_conf),
        "name": "templat"+str(id_conf)+"",
        "created_at": 1523401234,
        "updated_at": 1523412345,
        "creator_id": "test",
        "object": payload}
    url = 'http://localhost/api/v3.4/templates/conferences'
    headers = {'content-type': 'application/json'}
    start = time.monotonic()
    response = requests.post(url, data=json.dumps(temp_payload), headers=headers)
    response.status_code
    result = time.monotonic() - start
    print("Шаблон конференции #",id_conf, "создан с результатом ",response.status_code)
    print(response.text)
    logging.info("Templates conferenses"+ str(id_conf) +" Status code "+ str(response.status_code) + " Lead time: " + str(result) + " seconds.")
    if response.status_code != 200:
        logging.info(payload)
        logging.info(response.text)


logging.info(" Create Conferenses")
count = int(input("Какое количество конференций создать ? (N*18) "))
start = time.monotonic()

create_conf(count)
#delete_all_conf()

result = time.monotonic() - start
print("All time: " + str(result) + " seconds.")
logging.info(" All time: " + str(result) + " seconds.")
