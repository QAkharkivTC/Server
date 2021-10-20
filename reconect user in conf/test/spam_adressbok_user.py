import requests
import json
import logging
import time
import urllib3
import certifi
import ssl


def spam_add_contacts(N):
    ssl._create_default_https_context = ssl._create_unverified_context
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    localhost = 'qa3.trueconf.net'
    user = 'artem'
    token = '00e07cc6fc3ddb69c07facb05e242653df9592a1'
    for i in range(N):
        data = {"contact_id":"SPAM_"+str(i)+"","display_name":"SPAM_"+str(i)+""}
        r = requests.post('https://'+localhost+'/api/v3.1/users/'+user+'/addressbook?access_token='+token+'', data=data , verify=False)
        print("Contact SPAM_"+str(i)+" was added with resalt: " , r.status_code)
        #print(r.text)

spam_add_contacts(100000)        
