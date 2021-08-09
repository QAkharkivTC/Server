import json
import requests                                                 # pip install requests
import time
import logging
import urllib3
import certifi
import ssl

def stop_conferences(N):
    ssl._create_default_https_context = ssl._create_unverified_context
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    logging.info("Start test")
    for k in range(N):
        print("step "+ str(k))
        
        r = requests.post('http://localhost/api/v3.3/conferences/888000'+str(k)+'/stop')
        r = requests.post('http://localhost/api/v3.3/conferences/777000'+str(k)+'/stop')
        r = requests.post('http://localhost/api/v3.3/conferences/666000'+str(k)+'/stop')
        r = requests.post('http://localhost/api/v3.3/conferences/555000'+str(k)+'/stop')
        #r = requests.post('http://localhost/api/v3.3/conferences/999000'+str(k)+'/stop')
        
        r.status_code
        #print(r.text.encode("utf-8"))
        print(r.status_code)
        print(r.text)
        if r.status_code != 200:
            logging.info(r)
            logging.info(r.text)

def start_conferences(N):
    ssl._create_default_https_context = ssl._create_unverified_context
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    logging.info("Start test")
    for k in range(N):
        print("step "+ str(k))
        
        r = requests.post('http://localhost/api/v3.3/conferences/888000'+str(k)+'/run')
        r = requests.post('http://localhost/api/v3.3/conferences/777000'+str(k)+'/run')
        r = requests.post('http://localhost/api/v3.3/conferences/666000'+str(k)+'/run')
        r = requests.post('http://localhost/api/v3.3/conferences/555000'+str(k)+'/run')
        #r = requests.post('http://localhost/api/v3.3/conferences/999000'+str(k)+'/run')
        
        r.status_code
        #print(r.text.encode("utf-8"))
        print(r.status_code)
        print(r.text)
        if r.status_code != 200:
            logging.info(r)
            logging.info(r.text)


            
def delete_conferences(N):
    ssl._create_default_https_context = ssl._create_unverified_context
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    logging.info("Start test")
    for k in range(N):
        print("step "+ str(k))
        
        r = requests.delete('https://10.130.2.163/api/v3.3/conferences/777000'+str(k)+'?access_token=VNkBg6xyOt6X9RP2NJb5B09kxMlfo3SJ', verify=False)
        #r = requests.delete('https://10.130.1.156/api/v3.3/conferences/777000'+str(k)+'?access_token=hjqRJTq5Q13NJIXdxHmTNT84USnROiQz', verify=False)
        #r = requests.delete('https://10.130.1.156/api/v3.3/conferences/999000'+str(k)+'?access_token=hjqRJTq5Q13NJIXdxHmTNT84USnROiQz', verify=False)
        #r = requests.delete('http://localhost/api/v3.3/conferences/555000'+str(k)+'')
        #r = requests.delete('http://localhost/api/v3.3/conferences/999000'+str(k)+'')
        
        r.status_code
        #print(r.text.encode("utf-8"))
        print(r.status_code)
        print(r.text)
        if r.status_code != 200:
            logging.info(r)
            logging.info(r.text)


delete_conferences(144)
#stop_conferences(144)
#start_conferences(144)
