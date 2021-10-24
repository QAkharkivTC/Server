import psycopg2
from psycopg2 import Error
import random
import time
import datetime
from datetime import datetime

def send_data_to_DB(N):
    for i in range(N):
        try:
            # Подключиться к существующей базе данных
            connection = psycopg2.connect(user="postgres",
                                          # пароль, который указали при установке PostgreSQL
                                          password="",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="tcs")

            cursor = connection.cursor()
            # Выполнение SQL-запроса для вставки данных в таблицу
            
            value = str(make_data(i))
            #value = '(21, 89, 152, 524, 930, 534, 125, 333, 228, 117, 380, 493, 195, 172, \'2021-10-19 20:55:01\')'
            insert_query = """ INSERT INTO log.stats (id, cpu_load, endpoints, transport_bitrate_in, transport_bitrate_out, streams, streams_bitrate_in, streams_bitrate_out, online_users, conferences, participants, guests, gateways, terminals, created_at) VALUES """+value+""""""
            cursor.execute(insert_query)
            
            connection.commit()

        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Соединение с PostgreSQL закрыто")


def make_data(i):
    time_now = round(time.time())
    
    year = 31536000
    #time_start = time_now - year
    time_start = 1608633600
    id_ = i+8770                                        # добавляем некое значение (последнее значение +1 в колонке id в таблице log.stats)
    #ts = time_start + 3600*i                           # unixtime (от какого момента генерировать данные) + 3600 (количество секунд в часе)- с каким интервалом создавать данные
    #ts = time_start + 60*i                             # шаг минута
    #ts = time_start + 120*i                            # шаг 2 минуты
    ts = time_start + 600*i                             # шаг 10 минут
    #ts = time_start + 900*i                            # шаг 15 минута
    #ts = time_start + 1800*i                           # шаг 30 минута
    #ts = time_start + 3600*i                           # шаг 1 час
    #ts = time_start + 7200*i                           # шаг 2 часа
    #ts = time_start + 1234*i                           # шаг кастомный (сам указывай)
                                                        # 31536000 - количество секунд в году
    
    cpu_load = random.randint(0,100)                    # можно указать граничное значение для рандома
    endpoints = random.randint(0,300)
    transport_bitrate_in = random.randint(10,1024)
    transport_bitrate_out = random.randint(20,1024)
    streams = random.randint(100,1024)
    streams_bitrate_in = random.randint(1,1024)
    streams_bitrate_out = random.randint(1,1024)
    online_users = random.randint(1,500)
    conferences = random.randint(1,200)
    participants = random.randint(1,500)
    guests = random.randint(1,500)
    gateways = random.randint(1,51)
    terminals = random.randint(1,210)
    created_at = str(datetime.fromtimestamp(ts))

    value = '('+ str(id_) +', '+ str(cpu_load) +', '+ str(endpoints) +', '+ str(transport_bitrate_in) +', '+ str(transport_bitrate_out) +', '+ str(streams) +', '+ str(streams_bitrate_in) +', '+ str(streams_bitrate_out)+', '+ str(online_users) +', '+ str(conferences) +', '+ str(participants) +', '+ str(guests) +', '+ str(gateways) +', '+ str(terminals) +', \''+ created_at +'\')'

    print(value)
    return value


#make_data(10)

send_data_to_DB(43800)
