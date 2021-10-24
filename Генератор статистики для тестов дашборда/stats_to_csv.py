import random
import time
import datetime
from datetime import datetime
import csv

index = str(round(time.time()))
filename = 'stats_'+index+'.csv'

def create_stats_file(N):
    make_file()
    for i in range(N):
        line = make_data(i)
        write_to_csv(line)
    
def write_to_csv(line):
    text = [line]
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(text)

def make_file():
    line = ['id,\"cpu_load\",\"endpoints\",\"transport_bitrate_in\",\"transport_bitrate_out\",\"streams\",\"streams_bitrate_in\",\"streams_bitrate_out\",\"online_users\",\"conferences\",\"participants\",\"guests\",\"gateways\",\"terminals\",\"created_at\"']
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file,  delimiter=';')
        writer.writerow(line)

def make_data(i):
    time_now = round(time.time())
    
    year = 31536000
    time_start = time_now - year                        # тут можно указать за сколько лет нужно создать статистику (например за 2 года: time_start = time_now - year * 2)
                                                        #time_start = 1608633600
    id_ = i                                             # добавляем некое значение (последнее значение +1 в колонке id в таблице log.stats)
    #ts = time_start + 3600*i                           # unixtime (от какого момента генерировать данные) + 3600 (количество секунд в часе)- с каким интервалом создавать данные
    ts = time_start + 60*i                              # шаг минута            за год 525600 записей
    #ts = time_start + 120*i                            # шаг 2 минуты          за год 262800 записей
    #ts = time_start + 600*i                            # шаг 10 минут          за год 52560 записей
    #ts = time_start + 900*i                            # шаг 15 минута         за год 35040 записей
    #ts = time_start + 1800*i                           # шаг 30 минута         за год 17520 записей
    #ts = time_start + 3600*i                           # шаг 1 час             за год 8760 записей
    #ts = time_start + 7200*i                           # шаг 2 часа            за год 4380 записей
    #ts = time_start + 1234*i                           # шаг кастомный (сам указывай)
                                                        # 31536000 - количество секунд в году
    
    cpu_load = random.randint(25,80)                    # можно указать граничное значение для рандома
    endpoints = random.randint(30,300)
    transport_bitrate_in = random.randint(500,2024)
    transport_bitrate_out = random.randint(200,1024)
    streams = random.randint(1000,2024)
    streams_bitrate_in = random.randint(1,1024)
    streams_bitrate_out = random.randint(800,4024)
    online_users = random.randint(20,500)
    conferences = random.randint(1,200)
    participants = random.randint(100,200)
    guests = random.randint(100,300)
    gateways = random.randint(10,51)
    terminals = random.randint(100,210)
    created_at = str(datetime.fromtimestamp(ts))

    value = ''+ str(id_) +', '+ str(cpu_load) +', '+ str(endpoints) +', '+ str(transport_bitrate_in) +', '+ str(transport_bitrate_out) +', '+ str(streams) +', '+ str(streams_bitrate_in) +', '+ str(streams_bitrate_out)+', '+ str(online_users) +', '+ str(conferences) +', '+ str(participants) +', '+ str(guests) +', '+ str(gateways) +', '+ str(terminals) +', '+ created_at +''

    print(value)
    return value        
    
#make_data(10)
create_stats_file(525600)
