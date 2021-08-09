import requests
import json
import logging
import time

# add filemode="w" to overwrite
#logging.debug("This is a debug message")
#logging.info("Informational message")
#logging.error("An error has happened!")

t = str(time.time())
logging.basicConfig(filename="log create users "+t+".log", format='%(asctime)s %(levelname)s:%(message)s', level=logging.INFO)


def create_users(N, id_u, email_u):
    logging.info("Create users")
    for k in range(N):
        start = time.monotonic()
        r = requests.post('http://localhost/api/v3.3/users', data= {
             "id": ""+id_u+str(k+1)+"",
             "login_name":""+id_u+str(k+1)+"",
             "password": "11",
             "email": ""+email_u+"+0"+str(k+1)+"@trueconf.ru",
             "first_name": "Фамилия "+str(k+1)+"",
             "last_name": "Имя "+str(k+1)+"",
             "company": "Тестовый отдел в городе Харьков",
             "mobile_phone": "+345967111"+str(k+1)+"",
             "work_phone": "+3258454111"+str(k+1)+"",
             "home_phone": "+3245569111"+str(k+1)+"",
             "groups":[{
                "id": "0001",
                "display_name": "Group 0"}]
        })
        r.status_code
        print("User ", k+1, " from ", N, "result: ", r.status_code)
        #print(r.text.encode("utf-8"))
        print(r.status_code)
        print(r.text)
        result = time.monotonic() - start
        #print("Program time: " + str(result) + " seconds.")
        #str(time.strftime("%c",time.localtime()))+
        logging.info(" "+id_u+ str(k+1) +" Status code "+ str(r.status_code) + " Lead time: " + str(result) + " seconds.")
        if r.status_code != 200:
            logging.info(r)
            logging.info(r.text)

#create_users(300)

def create_groups(G):
    logging.info("Create groups")
    for k in range(G):
        start = time.monotonic()
        r = requests.post('http://localhost/api/v3.3/groups', data=  {"display_name": "Group"+str(k+1)+""})
        r.status_code
        print("Group", k+1, r.status_code)
        result = time.monotonic() - start
        #print("Program time: " + str(result) + " seconds.")
        #str(time.strftime("%c",time.localtime()))+
        logging.info(" Group"+ str(k+1) +" Status code "+ str(r.status_code) + " Lead time: " + str(result) + " seconds.")
        if r.status_code != 200:
            logging.info(r)
            logging.info(r.text)

#create_groups(10)

        '''
не рабочие rtsp ссылки переодически проверять

      -  "VirginiaTech": {"video": "rtsp://198.82.159.136:554/axis-media/media.amp", "position":"37.223357,-80.417004"},
      -  "Honk-Kong": {"video": "rtsp://weathercam.gsis.edu.hk/axis-media/media.amp", "position":"22.352734,114.1277", "options":"rtptransport=tcp&timeout=60"},
      -  "Vavrisovo": {"video": "rtsp://stream5.kukaj.sk:1935/live/VAVRISOVO.stream",
     --   "audio": "rtsp://stream5.kukaj.sk:1935/live/VAVRISOVO.stream", "position":"49.0758931,19.7501234"},
    --  "Scheveningen-1": {"video": "rtsp://b1.dnsdojo.com:1935/live/sys1.stream", "position":"52.1042263,4.2494571"},
     ++   "Curacao": {"video": "rtsp://srv13.arkasis.nl:80/498/default.stream", "position":"12.2376122,-69.1801954"},
     
     
     
        {"contact_id": "#rtsp://webcamserverdh.dyndns-remote.com:1935/live/mp4:ehtx.stream",
        "display_name": "Texel"},
        {"contact_id": "#rtsp://srv13.arkasis.nl:80/498/default.stream",
        "display_name": "Curacao"},
        {"contact_id": "#h323:\e\40000@217.151.130.93"
        "display_name": "Curacao"},
        
        {"contact_id": "#rtsp://85.25.218.202:1935/live/mp4:havenmond.stream",
        "display_name": "Havenmond"},
        {"contact_id": "#rtsp://narr-cam.liladelman.com/axis-media/media.amp",
        "display_name": "LilaDelman"},
        {"contact_id": "#rtsp://stream5.kukaj.sk:1935/live/SOKOLYLM.stream",
        "display_name": "Sokolylm"},
        {"contact_id": "#rtsp://stream5.kukaj.sk:1935/live/MARINA.stream",
        "display_name": "Marina"},
        {"contact_id": "#rtsp://stream5.kukaj.sk:1935/live/BOCIANY_PRIB.stream",
        "display_name": "Prib"},
        {"contact_id": "#rtsp://194.32.173.211/axis-media/media.amp",
        "display_name": "Trento"}, #?
        {"contact_id": "#rtsp://b1.dnsdojo.com:1935/live/sys3.stream",
        "display_name": "Scheveningen-3"},
        {"contact_id": "#rtsp://stream5.kukaj.sk:1935/live/VF1212.stream",
        "display_name": "Velkafatra"},
        {"contact_id": "#rtsp://132.239.12.145:554/axis-media/media.amp",
        "display_name": "PriceCenterPlaza"},
        {"contact_id": "#rtsp://stream.zivekamery.sk:1935/live/LOMNICAK.stream",
        "display_name": "Lomnicak"},
        {"contact_id": "#rtsp://stream.tmr.sk:1935/tmr/STREAM17.stream",
        "display_name": "KonskyGrun"},
        {"contact_id": "#rtsp://stream5.kukaj.sk:1935/live/VYSOKAPRIMORAVE.stream",
        "display_name": "Vysokaprimorave"},
        {"contact_id": "#rtsp://stream5.kukaj.sk:1935/live/DEMANOVA.stream",
        "display_name": "Demanova"},

'''

def add_cotact_to_users(N, id_u):
    logging.info(" Add contacts to users ")
    contact_list=[
        {"contact_id": "rtsp://76.75.8.116/axis-media/media.amp",
        "display_name": "Great Falls"},
        {"contact_id": "rtsp://196.21.92.82/axis-media/media.amp",
        "display_name": "Western Cape"},
        {"contact_id": "rtsp://srv13.arkasis.nl:80/498/default.stream",
        "display_name": "Curacao"},
        {"contact_id": "rtsp://187.1.147.77:2000/axis-media/media.amp",
        "display_name": "Bahia"},
        {"contact_id": "rtsp://77.110.228.219/axis-media/media.amp",
        "display_name": "Nordland"},
        {"contact_id": "rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov",
        "display_name": "Bunny"},
        {"contact_id": "rtsp://73.114.177.111/axis-media/media.amp",
        "display_name": "Bedford Hills"},
        {"contact_id": "rtsp://176.65.94.105/axis-media/media.amp", #?
        "display_name": "Pocapaglia"},
        {"contact_id": "rtsp://37.157.51.30/axis-media/media.amp",
        "display_name": "Norwich"},
        {"contact_id": "rtsp://64.187.201.16/axis-media/media.amp",
        "display_name": "Montana"},
        {"contact_id": "rtsp://stream.strba.sk:1935/strba/VYHLAD_JAZERO.stream",
        "display_name": "VyhladJazero"},
        {"contact_id": "rtsp://77.52.149.60/axis-media/media.amp",
        "display_name": "Kiev"},
        {"contact_id": "rtsp://78.10.34.92/axis-media/media.amp",
        "display_name": "Wroclaw"},
        {"contact_id": "#sip:@10.110.1.202",
        "display_name": "Cisco E20"},
        {"contact_id": "#h323:@10.110.1.202",
        "display_name": "Cisco E20"},
        {"contact_id": "#sip:@10.110.1.208",
        "display_name": "Grandstream GVC3200"},
        {"contact_id": "#h323:@10.110.1.208",
        "display_name": "Grandstream GVC3200"},
        {"contact_id": "#sip:@10.110.1.213",
        "display_name": "Cisco C20"},
        {"contact_id": "#h323:@10.110.1.213",
        "display_name": "Cisco C20"},
        {"contact_id": "#sip:gary@selfie.vc",
        "display_name": "CisC20"},
        {"contact_id": "#sip:loopback@rtp.ciscotac.net",
        "display_name": "CiC210"},
        {"contact_id": "#sip:astronaut@selfie.vc",
        "display_name": "Ci0"},
        {"contact_id": "#sip:thetestcall@getonsip.com",
        "display_name": "C7C20"},
        {"contact_id": "#sip:president@selfie.vc",
        "display_name": "Ci0"},
        {"contact_id": "#h323:367535@lifesizecloud.com",
        "display_name": "CC23"},
        {"contact_id": "#h323:111@199.48.152.152",
        "display_name": "CC22"},
        {"contact_id": "#h323:311647@lifesizecloud.com",
        "display_name": "C21"},
        {"contact_id": "#h323:3559379@lifesizecloud.com",
        "display_name": "C20"},
        {"contact_id": "#sip:@10.110.1.206",
         "display_name": "C120"},
        {"contact_id": "#h323:@10.110.1.206",
         "display_name": "C120"},
        {"contact_id": "#sip:@10.110.1.210",
         "display_name": "C2120"},
        {"contact_id": "#h323:@10.110.1.210",
         "display_name": "C1220"},
        {"contact_id": "rtsp://170.93.143.139/rtplive/470011e600ef003a004ee33696235daa",
         "display_name": "Road"},
        {"contact_id": "#h323:\e\40000@217.151.130.93",
         "display_name": "Terminal"},
        {"contact_id": "rtsp://qa3.trueconf.net/c/sym",
         "display_name": "QA SYM conf"},
        {"contact_id": "rtsp://qa3.trueconf.net/c/role",
         "display_name": "QA ROLE conf"},
        {"contact_id": "#sip:fireplace@ivr.vc,123#",
         "display_name": "Fireplace"},
        {"contact_id": "#sip:hdx6000@10.110.1.203",
         "display_name": "hdx6000"},
        {"contact_id": "#h323:cisco213@10.110.1.213",
         "display_name": "cisco213"}
        
        
        
        #h323:cisco213@10.110.1.213
        #sip:hdx6000@10.110.1.203

        ]
    for i in range(len(contact_list)):
        for user in range(N):
            start = time.monotonic()
            r = requests.post('http://localhost/api/v3.3/users/'+id_u+str(user+1)+'/addressbook', data= contact_list[i])
            r.status_code
            print(" Add contact "+str(i+1)+" to user "+ str(user+1) +"'s AB "+" Status code "+ str(r.status_code))
            result = time.monotonic() - start
            logging.info(" Add contact "+str(i+1)+" to user "+ str(user+1) +"'s AB "+" Status code "+ str(r.status_code) + " Lead time: " + str(result) + " seconds.")
            if r.status_code != 200:
                logging.info(r)
                logging.info(r.text)

def add_sub_contacts(N, id_u, K):
    for i in range(K):
        logging.info(" Add Sub_contacts to users ")
        contact_list=[
            {"contact_id": "sub_contact"+str(i)+"@qa3.trueconf.net",
            "display_name": "sub_contact"+str(i)+""}
            ]
        
        for user in range(N):
            start = time.monotonic()
            r = requests.post('http://localhost/api/v3.3/users/'+id_u+str(user+1)+'/addressbook', data= contact_list[0])
            r.status_code
            print(" Add псевдо contact "+str(i+1)+" to user "+ str(user+1) +"'s AB "+" Status code "+ str(r.status_code))
            result = time.monotonic() - start
            logging.info(" Add псевдо contact "+str(i+1)+" to user "+ str(user+1) +"'s AB "+" Status code "+ str(r.status_code) + " Lead time: " + str(result) + " seconds.")
            if r.status_code != 200:
                logging.info(r)
                logging.info(r.text)
    

#add_cotact_to_users(N, id_u)

def add_user_to_group(N, G, id_u):
                                                #N - users G - groups
    uig = N//G                                  #определяем количество пользователей в группах
    logging.info(" Add users to groups")
    list_id = []                                #список id групп
    for f in range(G):                          #прохожусь по каждой созданной группе
        
        r = requests.get('http://localhost/api/v3.3/groups/')   #запрашиваем весь список групп
        media = json.loads(r.text)                              #json.dumps конвертирует словарь в строку. json.loads конвертирует строку в словарь
        #print(media)

        for v in range(len(media['groups'])):                                       #прохожусь по каждой группе из json файла
            if ((media['groups'][v]['display_name']) == ('Group'+str(f+1)+'')):     #ищу группу по ее названию
                list_id.append(media['groups'][v]['id'])                            #в список записываем id найденной группы
            else:
                pass

    #print(list_id)


        for y in range(uig):                                    #для каждой группы f я добавляю y пользователя из uig (количество)
            u = int((f*uig)+y+1)
            start = time.monotonic()
            r = requests.post('http://localhost/api/v3.3/groups/'+str(list_id[f])+'/users', data= {"user_id":""+id_u+str(u)+""})
            r.status_code
            print(" Add user to group "+ str(f) +" Status code "+ str(r.status_code))
            result = time.monotonic() - start
            #print("Program time: " + str(result) + " seconds.")
            logging.info(" Add user to group "+ str(f) +" Status code "+ str(r.status_code) + " Lead time: " + str(result) + " seconds.")
            if r.status_code != 200:
                logging.info(r)
                logging.info(r.text)

N = int(input("Сколько создать пользователей? "))
id_u = str(input("Укажите id для пользователей "))
email_u = str(input("Укажите email для пользователей "))
G = int(input("Сколько создать групп? "))
K = int(input("Сколько создать псевдоконтактов ? "))

start = time.monotonic()

create_groups(G)                    # создает N групп
create_users(N, id_u, email_u)      # создает N пользователей
add_user_to_group(N, G, id_u)       # распределяет N пользователей по N групп 
add_cotact_to_users(N, id_u)        # добавляет контакты в АК пользователей (39 шт sip/h323/rtsp)
#add_sub_contacts(N, id_u, K)        # добавляет N псевдоконтактов в АК пользователя

result = time.monotonic() - start
print("All time: " + str(result) + " seconds.")
logging.info("All time: " + str(result) + " seconds.")
