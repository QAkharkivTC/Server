import json
import requests
import time
import urllib3
import certifi
import ssl
import re
from requests import Request, Session

user = 'artem_7'
server_name = 'aa111.trueconf.name'
ip = '10.130.2.209'
token = '2PReau6pERNRhbHZcd1Q6I2Y1Mlnd7C3'
cid = 'chat'
login_admim = 'tc'
password_admin = 'qweASD123'                            
cookies_value = 'ea573dbe280b4235ac1f3c8fb16bb36d'


#  http://169.254.247.130/tools/real-time?
#  k=00AEEA115A2E398D957C73CBEE31B55AA0181D88&call_id=sub2.trust1.loc%5Ctestuser8%40aa111.trueconf.name%2Fa2a12b48&
#  stream_id=0000004e65d96a21%40aa111.trueconf.name%23vcs&lang=ru&version=8.0.0&mode=inapp&app=TrueConf_Windows


def test_1():
    ssl._create_default_https_context = ssl._create_unverified_context
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


    s = requests.Session()

    
    headers = {'content-type': 'application/json'}
    data = {"username":login_admim,"password":password_admin}
    url_1 = 'https://'+ip+'/guest/auth/login/'
    
    response = s.post(url_1, headers=headers, data=data, verify=False)

    response.status_code
    #print(response.cookies)
    test = response.cookies
    #print(test)
    
    for cookie in response.cookies:
        print(cookie.__dict__)
        coockies_2 = cookie.__dict__
        coockies_1 = cookie.__dict__['value']
        #coockies_1 = test['value']

    print(coockies_1)

    #response_2 = s.post(url_1, headers=headers, data=data, verify=False)


    cook = 'PHPSESSID=ea573dbe280b4235ac1f3c8fb16bb36d'
    cook2 = 'PHPSESSID='+coockies_1+''

    cookies_11 = {'PHPSESSID':'ea573dbe280b4235ac1f3c8fb16bb36d'} #  ea573dbe280b4235ac1f3c8fb16bb36d
    headers = {'content-type': 'application/json'}
    url = 'https://'+ip+'/draft/v1/streams/0000004e65d96a21%40aa111.trueconf.name%23vcs/participants/artem_7%40aa111.trueconf.name%2Fb3509b25/?a='+cook2+'&lang=ru'
    url_2 = 'https://10.130.2.209/tools/real-time/0000004e65d96a21%40aa111.trueconf.name%23vcs?a='+cook+'&lang=ru'
    response_2 = s.delete(url, headers=headers, verify=False)
    #response_3 = s.delete(url_2, headers=headers, cookies=cookies_11, verify=False)

    print(response_2.text)
    #print(response_3.text)

test_1()

