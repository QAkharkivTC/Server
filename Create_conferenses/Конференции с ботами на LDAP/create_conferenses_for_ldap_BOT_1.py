import json
import requests
import time

def list_invitations (N_users):
    '''
    Функция возвращает список пользователей для конференции
    от user0 до userN-1
    '''
    invitations = [
            {
            "id": "apukhtin1",
            "display_name": "apukhtin1"
            },
            {
            "id": "apukhtin2",
            "display_name": "apukhtin2"
            },
            {
            "id": "apukhtin3",
            "display_name": "apukhtin3"
            },
            {
            "id": "bot_1",
            "display_name": "bot_1"
            },
            {
            "id": "bot_2",
            "display_name": "bot_2"
            },
            {
            "id": "bot_3",
            "display_name": "bot_3"
            },
            {
            "id": "bot_4",
            "display_name": "bot_4"
            },
            {
            "id": "bot_5",
            "display_name": "bot_5"
            },
            {
            "id": "bot_6",
            "display_name": "bot_6"
            },
            {
            "id": "bot_7",
            "display_name": "bot_7"
            },
            {
            "id": "bot_8",
            "display_name": "bot_8"
            },
            {
            "id": "bot_9",
            "display_name": "bot_9"
            },
            {
            "id": "sub2.trust1.loc\\bot_sub2_1",
            "display_name": "sub2.trust1.loc\\bot_sub2_1"
            },
            {
            "id": "sub2.trust1.loc\\bot_sub2_2",
            "display_name": "sub2.trust1.loc\\bot_sub2_2"
            },
            {
            "id": "sub2.trust1.loc\\bot_sub2_3",
            "display_name": "sub2.trust1.loc\\bot_sub2_3"
            },
            {
            "id": "sub2.trust1.loc\\bot_sub2_4",
            "display_name": "sub2.trust1.loc\\bot_sub2_4"
            },
            {
            "id": "sub2.trust1.loc\\bot_sub2_5",
            "display_name": "sub2.trust1.loc\\bot_sub2_5"
            },
            {
            "id": "sub2.trust1.loc\\bot_sub2_6",
            "display_name": "sub2.trust1.loc\\bot_sub2_6"
            },
            {
            "id": "sub2.trust1.loc\\bot_sub2_7",
            "display_name": "sub2.trust1.loc\\bot_sub2_7"
            },
            {
            "id": "sub2.trust1.loc\\bot_sub2_8",
            "display_name": "sub2.trust1.loc\\bot_sub2_8"
            },
            {
            "id": "sub2.trust1.loc\\bot_sub2_9",
            "display_name": "sub2.trust1.loc\\bot_sub2_9"
            },
            {
            "id": "sub1.trust1.loc\\bot_sub1_1",
            "display_name": "sub1.trust1.loc\\bot_sub1_1"
            },
            {
            "id": "sub1.trust1.loc\\bot_sub1_2",
            "display_name": "sub1.trust1.loc\\bot_sub1_2"
            },
            {
            "id": "sub1.trust1.loc\\bot_sub1_3",
            "display_name": "sub1.trust1.loc\\bot_sub1_3"
            },
            {
            "id": "sub1.trust1.loc\\bot_sub1_4",
            "display_name": "sub1.trust1.loc\\bot_sub1_4"
            },
            {
            "id": "sub1.trust1.loc\\bot_sub1_5",
            "display_name": "sub1.trust1.loc\\bot_sub1_5"
            },
            {
            "id": "sub1.trust1.loc\\bot_sub1_6",
            "display_name": "sub1.trust1.loc\\bot_sub1_6"
            },
            {
            "id": "sub1.trust1.loc\\bot_sub1_7",
            "display_name": "sub1.trust1.loc\\bot_sub1_7"
            },
            {
            "id": "sub1.trust1.loc\\bot_sub1_8",
            "display_name": "sub1.trust1.loc\\bot_sub1_8"
            },
            {
            "id": "sub1.trust1.loc\\bot_sub1_9",
            "display_name": "sub1.trust1.loc\\bot_sub1_9"
            },
            {
            "id": "sub1.trust1.loc\\testuser2",
            "display_name": "sub1.trust1.loc\\testuser2"
            },
            {
            "id": "sub1.trust1.loc\\testuser6",
            "display_name": "sub1.trust1.loc\\testuser6"
            },
            {
            "id": "sub2.trust1.loc\\testuser7",
            "display_name": "sub2.trust1.loc\\testuser7"
            },
            {
            "id": "sub2.trust1.loc\\testuser8",
            "display_name": "sub2.trust1.loc\\testuser8"
            }
            
        ]
    for u in range(N_users - 3):
        invitations.append({
            "id": "user"+str(u)+"",
            "display_name": "user"+str(u)+""
            })
    return invitations

def creat_payload (id_conf, y, k, max_participants, max_podiums):
    '''
    Функция создает тело запроса для создания конференции
    '''

    text_desctription = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt, explicabo. Nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos, qui ratione voluptatem sequi nesciunt, neque porro quisquam est, qui dolorem ipsum, quia dolor sit, amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt, ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit, qui in ea voluptate velit esse, quam nihil molestiae consequatur, vel illum, qui dolorem eum fugiat, quo voluptas nulla pariatur? At vero eos et accusamus et iusto odio dignissimos ducimus, qui blanditiis praesentium voluptatum deleniti atque corrupti, quos dolores et quas molestias excepturi sint, obcaecati cupiditate non provident, similique sunt in culpa, qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio, cumque nihil impedit, quo minus id, quod maxime placeat, facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet, ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt, explicabo. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet, ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt, explicabo. laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit, qui in ea voluptate velit esse, quam nihil molestiae consequatur, vel illum, qui dolorem eum fugiat, quo voluptas nulla pariatur? At vero eos et accusamus et iusto odio dignissimos ducimus, qui blanditiis praesentium voluptatum deleniti atque corrupti, quos dolores et quas molestias excepturi sint, obcaecati cupiditate non provident, similique sunt in culpa, qui officia deserunt mollitia animi, id est laborum sunt in culpa, qui officia deserunt mollitia animi, id est laborum et dolorum fugasunt in culpa, qui officia deserunt mollitia animi, id est laborum et dolorum fugasunt in culpa, qui officia deserunt mollitia animi, id est laborum et dolorum fugasunt in culpa, qui officia deserunt mollitia animi, id est laborum et dol"

    
    payload = {
        "id": "000"+str(id_conf)+"",
        "pin_enabled": True,
        "pin": "000"+str(id_conf)+"",
        "meeting_room":"г.Харьков ул. Отакара Яроша 9а, 5 этаж каб.6-7",
        "type": str(y),
        "topic": "Test conf "+str(id_conf)+"",
        "owner": "apukhtin@aa111.trueconf.name",                      #указать домен сервера (при использовании с другими серверами)
        "invitations": list_invitations(max_participants),
        "description": "Test conf "+str(id_conf)+" "+ text_desctription +"",
        "max_podiums": str(max_podiums),
        "max_participants": str(max_participants),
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
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    response.status_code
    print("Конференция #",id_conf, "создана с результатом ",response.status_code)
    print(response.text)

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
            elif type_conf == 1:
                y = 1
                max_podiums = 1
                max_participants = 36		
            else:
                y = 3
                max_podiums = 6
                max_participants = 300
                
            for ty2_conf in range (2):                              #выбираем вид конференции (внутренняя, публичная)
                if ty2_conf%2 == 0:                                 #публичная
                    payload = creat_payload(id_conf, y, k, max_participants, max_podiums)
                    payload.update({"allow_guests":True})

                    for t in range(3):                              #выбираем тип расписания для типа конференции
                        if t == 0:                                  #-1 - without schedule
                            type_s = str(t)
                            sch1={}
                            sch1.update(schedule(t))
                            payload.update({"schedule": sch1})
                            id_conf+=1
                            payload.update({"id": "000"+str(id_conf)+""})
                            payload.update({"topic": "Test conf "+str(id_conf)+""})
                        elif t == 1:                                #0 - weekly
                            type_s = str(t)
                            sch1={}
                            sch1.update(schedule(t))
                            payload.update({"schedule": sch1})
                            id_conf+=1
                            payload.update({"id": "000"+str(id_conf)+""})
                            payload.update({"topic": "Test conf "+str(id_conf)+""})
                        else:                                       #1 - one-time
                            type_s = str(t)
                            sch1={}
                            sch1.update(schedule(t))
                            payload.update({"schedule": sch1})
                            id_conf+=1
                            payload.update({"id": "000"+str(id_conf)+""})
                            payload.update({"topic": "Test conf "+str(id_conf)+""})
                        
                        send_response (payload, id_conf)

                else:                           
                    payload = creat_payload(id_conf, y, k, max_participants, max_podiums)
                    payload.update({"allow_guests":False})          #внутренняя
                    
                    for t in range(3):                              #выбираем тип расписания для типа конференции
                        if t == 0:                                  #-1 - without schedule
                            type_s = str(t)
                            sch1={}
                            sch1.update(schedule(t))
                            payload.update({"schedule": sch1})
                            id_conf+=1
                            payload.update({"id": "000"+str(id_conf)+""})
                            payload.update({"topic": "Test conf "+str(id_conf)+""})
                        elif t == 1:                                #0 - weekly
                            type_s = str(t)
                            sch1={}
                            sch1.update(schedule(t))
                            payload.update({"schedule": sch1})
                            id_conf+=1
                            payload.update({"id": "000"+str(id_conf)+""})
                            payload.update({"topic": "Test conf "+str(id_conf)+""})
                        else:                                       #1 - one-time
                            type_s = str(t)
                            sch1={}
                            sch1.update(schedule(t))
                            payload.update({"schedule": sch1})
                            id_conf+=1
                            payload.update({"id": "000"+str(id_conf)+""})
                            payload.update({"topic": "Test conf "+str(id_conf)+""})
                        
                        send_response(payload, id_conf)
                
create_conf(1)
