import json
import requests
import time
import urllib3
import certifi
import ssl
import re

#http://localhost/api/v3.1/conferences/chat/invite?
#{"participants":["#tel:100"]}

#/api/v3.3/conferences/{{$conference_id}}/participants

def invite_partisipant():
    url = 'http://localhost/api/v3.3/conferences/chat/invite?'
    headers = {'content-type': 'application/json'}
    payload = {"participants":["artem_7@aa111.trueconf.name"]}
    
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    response.status_code
    #print(response.status_code)
    #print(response.text)

def get_stream_id(conf_id):
    url = 'http://localhost/api/v4/conferences/?&state=running&page_size=1000'
    headers = {'content-type': 'application/json'}
    response = requests.get(url, headers=headers)
    response.status_code
    #print(response.text)
    
    media = json.loads(response.text)

    for i in range(len(media['conferences'])):
        if media['conferences'][i]['id'] == conf_id:
            stream_id = media['conferences'][i]['session_id']
        else:
            pass
        
    #print(stream_id)
    stream_id = re.sub('[@]','%40',stream_id)
    stream_id = re.sub('[#]','%23',stream_id)
    #print(stream_id)
    return stream_id

def get_instans_partisipant(user_id):
    stream_id = get_stream_id('chat')
    url = 'http://localhost/draft/v1/streams/'+stream_id+'/participants/'
    headers = {'content-type': 'application/json'}
    response = requests.get(url, headers=headers)
    response.status_code
    print(response.text)
    media = json.loads(response.text)
    print(len(media['data']['participants']))

    for i in range(len(media['data']['participants'])):
        if media['data']['participants'][i]['call_id'] == user_id:
            instans = media['data']['participants'][i]['participant_id']
        else:
            pass
    print(instans)
    return instans

def remove_partisipant():
    stream_id = get_stream_id('chat')
    instans = get_instans_partisipant('artem_7@aa111.trueconf.name')
    instans = re.sub('[@]','%40',instans)
    instans = re.sub('[/]','%2F',instans)
    url = 'http://localhost/draft/v1/streams/'+stream_id+'/participants/'+instans+'/'
    headers = {'content-type': 'application/json'}
    
    response = requests.delete(url, headers=headers)
    response.status_code
    print(response.status_code)
    print(response.text)
    
    

def repeat_invite(N):
    for i in range(N):
        invite_partisipant()
        time.sleep(3)
        remove_partisipant()
        time.sleep(3)

repeat_invite(100)
#get_stream_id('chat')
      
#get_instans_partisipant('artem_7@aa111.trueconf.name')

