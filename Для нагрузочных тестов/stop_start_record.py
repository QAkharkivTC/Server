import requests
import json
import logging
import time
#/api/v3.2/conferences/{{$conference_id}}/stop-record
#/api/v3.2/conferences/{{$conference_id}}/start-record

logging.basicConfig(filename="Test stop-start record.log", format='%(asctime)s %(levelname)s:%(message)s', level=logging.INFO)

def restart_record (N):
    logging.info("Start test")
    for k in range(N):
        
        r = requests.post('http://localhost/api/v3.2/conferences/sym/stop-record')
        r.status_code
        #print(r.text.encode("utf-8"))
        print(r.status_code)
        print(r.text)
        if r.status_code != 200:
            logging.info(r)
            logging.info(r.text)

        time.sleep(0.5)

        r = requests.post('http://localhost/api/v3.2/conferences/sym/start-record')
        r.status_code
        #print(r.text.encode("utf-8"))
        print(r.status_code)
        print(r.text)
        if r.status_code != 200:
            logging.info(r)
            logging.info(r.text)

        time.sleep(5)

restart_record (1000)            
