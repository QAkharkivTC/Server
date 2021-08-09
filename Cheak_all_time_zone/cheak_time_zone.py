import requests
import json
import logging
import time
import urllib3
import certifi
import ssl

# http://localhost/api/v4/product/stats?timezone=Etc/GMT-11
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# https://bug-tracking.trueconf.com/show_bug.cgi?id=65191
# https://golang.org/src/time/zoneinfo_abbrs_windows.go



list_time_zone = []

def read_file_time_zone():
    f = open('time_zone_v2.txt', 'r')
    l = []
    for line in f:
        l.append(line) 
    global list_time_zone
    list_time_zone = [line.rstrip() for line in l]
    
    
    pass

def send_request():
    read_file_time_zone()
    
    for i in range(len(list_time_zone)):
        r = requests.get('http://localhost/api/v4/product/stats?timezone='+list_time_zone[i]+'')
        print(list_time_zone[i] + '\t\t\t\t\t' + str(r.status_code))
        if r.status_code != 200:
            print (list_time_zone[i] + ' ' + str(r.status_code))
            print (list_time_zone[i])
            print (r.text)
        #print(r.status_code)
        #print(r.text.encode("utf-8"))
        #print(r.status_code)
        #print(r.text)
    pass


send_request()    
