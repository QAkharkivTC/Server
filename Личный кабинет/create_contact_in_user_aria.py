import requests
import json
import logging
import time
import urllib3
import certifi
import ssl

def create_temp_UA(N):

    ssl._create_default_https_context = ssl._create_unverified_context
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    for k in range(N):

        payload = {"contact_id":"test_user_v"+str(k)+"",
                   "display_name":"test_user_v"+str(k)+""}
        
        URL = 'https://10.130.2.63/api/v3.1/users/artem4/addressbook?access_token=e139525ea73f9776ed75485c8c94b7e8140ecb4c' # редактировать перед запуском
        r = requests.post(URL, data= payload, verify=False)
        r.status_code
        print(r.status_code)
        print(r.text)
        
        
create_temp_UA(200)


