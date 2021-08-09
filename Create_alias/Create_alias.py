import requests
import json
import logging
import time
'''
t = str(time.time())
logging.basicConfig(filename="log create users "+t+".log", format='%(asctime)s %(levelname)s:%(message)s', level=logging.INFO)
'''
def crete_alias(N):
    logging.info("Create users")
    for k in range(N):
        r = requests.post('http://localhost/api/v3.2/aliases/', data= {
             "id": "alias_"+str(k+1)+"",
             "call_id": "user"+str(k+1)+""
        })
        r.status_code
        print("Alias ", k+1, " from ", N, "result: ", r.status_code)
        #print(r.text.encode("utf-8"))
        print(r.status_code)
        print(r.text)
        #result = time.monotonic() - start
        #print("Program time: " + str(result) + " seconds.")
        #str(time.strftime("%c",time.localtime()))+
        #logging.info("Alias "+ str(k+1) +" Status code "+ str(r.status_code) + " Lead time: " + str(result) + " seconds.")
        #if r.status_code != 200:
        #    logging.info(r)
         #   logging.info(r.text)

            
crete_alias(50)
