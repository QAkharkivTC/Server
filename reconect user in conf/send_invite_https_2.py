import json
import requests
import time
import urllib3
import certifi
import ssl
import re

#test data
user = 'artem_7'
server_name = 'aa111.trueconf.name'
ip = '10.130.2.209'
token = '2PReau6pERNRhbHZcd1Q6I2Y1Mlnd7C3'
cid = 'chat'
login_admim = 'tc'
password_admin = 'qweASD123'


def invite_partisipant(user, server_name, ip, cid, token):
    ssl._create_default_https_context = ssl._create_unverified_context
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    url = 'https://'+ip+'/api/v3.3/conferences/'+cid+'/invite?access_token='+token+''
    headers = {'content-type': 'application/json'}
    payload = {"participants":[""+user+"@"+server_name+""]}
    response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)
    
    #debug
    if response.status_code == 200:
        print('invite '+user)
    else:
        print('"invite_partisipant" dosen\'t work')
        print(response.status_code)
        print(response.text)
        

def get_stream_id(ip, cid, token):
    ssl._create_default_https_context = ssl._create_unverified_context
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    url = 'https://'+ip+'/api/v4/conferences/?access_token='+token+'&state=running&page_size=1000'
    headers = {'content-type': 'application/json'}
    response = requests.get(url, headers=headers, verify=False)
    
    media = json.loads(response.text)
    
    for i in range(len(media['conferences'])):
        if media['conferences'][i]['id'] == str(cid):
            stream_id = media['conferences'][i]['session_id']
        else:
            pass
        
    #print(stream_id)
    stream_id = re.sub('[@]','%40',stream_id)
    stream_id = re.sub('[#]','%23',stream_id)
    #print(stream_id)
    
    #debug
    if response.status_code != 200:
        print('something was wrong:  see in "get_stream_id"')
        print(response.text)
        print(response.status_code)
    else:
        pass
    
    return stream_id

def get_instans_partisipant(user, cid, ip, token, login_admim, password_admin, cookies_value, s):
    ssl._create_default_https_context = ssl._create_unverified_context
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    call_id = user+'@'+server_name
    stream_id = get_stream_id(ip, cid, token)
    
    #cookies_value = get_cookies(ip, login_admim, password_admin)
    
    cookies = {'PHPSESSID':''+cookies_value+''}
    headers = {'content-type': 'application/json'}
    url = 'https://'+ip+'/draft/v1/streams/'+stream_id+'/participants/'
    response = s.get(url, headers=headers, cookies=cookies, verify=False)
    
    print(response.status_code)
    print(response.text)
    media = json.loads(response.text)

    for i in range(len(media['data']['participants'])):
        if media['data']['participants'][i]['call_id'] == call_id:
            instans = media['data']['participants'][i]['participant_id']
        else:
            pass

    #debug
    if response.status_code != 200:
        print('something was wrong:  see in "get_instans_partisipant"')
        print(response.text)
        print(response.status_code)
        print(len(media['data']['participants']))
    else:
        #print(instans)
        pass
    
    return instans

def remove_partisipant(ip, cid, user, server_name, token, login_admim, password_admin, cookies_value, s):
    ssl._create_default_https_context = ssl._create_unverified_context
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    stream_id = get_stream_id(ip, cid, token)
    remove_user = user+'@'+server_name
    instans = get_instans_partisipant(user, cid, ip, token, login_admim, password_admin, cookies_value, s)
    instans = re.sub('[@]','%40',instans)
    instans = re.sub('[/]','%2F',instans)
    
    #cookies_value = get_cookies(ip, login_admim, password_admin)
    
    cookies = {'PHPSESSID':''+cookies_value+''} #  ea573dbe280b4235ac1f3c8fb16bb36d
    headers = {'content-type': 'application/json'}
    url = 'https://'+ip+'/draft/v1/streams/'+stream_id+'/participants/'+instans+'/'
    
    response = s.delete(url, headers=headers, cookies=cookies, verify=False)
    response.status_code

    #debug
    if response.status_code == 200:
        print('user ' + user + ' was removed')
    else:
        print(response.status_code)
        print(response.text)


def get_cookies(ip, login_admim, password_admin):
    ssl._create_default_https_context = ssl._create_unverified_context
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    s = requests.Session()
    
    headers = {'content-type': 'application/json'}
    data = {"username":login_admim,"password":password_admin}
    url = 'https://'+ip+'/guest/auth/login/'
    response = s.post(url, headers=headers, data=data, verify=False)
    response.status_code
    #print(response.cookies)
    test = response.cookies
    #print(test)
    
    for cookie in response.cookies:
        print(cookie.__dict__)
        coockies = cookie.__dict__['value']
        #coockies = test['value']

    #print(coockies)
    
    return coockies, s
        

def repeat_invite(N):
    #cookies_value = 'ea573dbe280b4235ac1f3c8fb16bb36d'
    '''
    ssl._create_default_https_context = ssl._create_unverified_context
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    s = requests.Session()
    
    headers = {'content-type': 'application/json'}
    data = {"username":login_admim,"password":password_admin}
    url = 'https://'+ip+'/guest/auth/login/'
    r = s.post(url, headers=headers, data=data, verify=False, stream=False)
    r.status_code
    #print(response.cookies)
    #test = r.cookies
    #print(test)
    
    
    for cookie in r.cookies:
        print(cookie.__dict__)
        cookies_value = cookie.__dict__['value']
        #coockies = test['value']

    #print(coockies)
    '''
    
    
    for i in range(N):
        invite_partisipant(user, server_name, ip, cid, token)
        time.sleep(3)
        remove_partisipant(ip, cid, user, server_name, token, login_admim, password_admin, cookies_value, s)
        time.sleep(3)

repeat_invite(100)


#debug
#get_cookies(ip, login_admim, password_admin)
#get_stream_id(ip, cid, token)      
#get_instans_partisipant(user, cid, ip, token)
#remove_partisipant(ip, cid, user, server_name, token, login_admim, password_admin)
#invite_partisipant(user, server_name, ip, cid, token)

