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


cid = 'chat'
sip_1 = '#sip:@10.130.2.89'
sip_2 = '#sip:@10.110.1.210'
sip_3 = '#sip:100@10.130.3.42'
sip_4 = '#h323:\e\40000@217.151.130.93'
sip_5 = '#sip:@10.110.1.208'
sip_6 = '#sip:@10.110.1.202'

user = 'bot_5@aa111.trueconf.name'
user_1 = 'sub1.trust1.loc\\testuser6@aa111.trueconf.name'
#user_2 = 'sub2.trust1.loc\\testuser7@aa111.trueconf.name'

h323_1 = '#h323:@10.110.1.210'
h323_2 = '#h323:@10.110.1.208'
h323_3 = '#h323:@10.110.1.202'
rtsp = 'rtsp://qa3.trueconf.net/c/sym/'


def invite_partisipant(cid, sip):
    url = 'http://localhost/api/v3.3/conferences/'+cid+'/invite?'
    headers = {'content-type': 'application/json'}
    payload = {"participants":[sip]}
    
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    response.status_code
    print(response.status_code)
    print(response.text)

def get_stream_id(cid):
    url = 'http://localhost/api/v4/conferences/?&state=running&page_size=1000'
    headers = {'content-type': 'application/json'}
    response = requests.get(url, headers=headers)
    response.status_code
    #print(response.text)
    
    media = json.loads(response.text)

    for i in range(len(media['conferences'])):
        if media['conferences'][i]['id'] == cid:
            stream_id = media['conferences'][i]['session_id']
        else:
            pass
        
    #print(stream_id)
    stream_id = re.sub('[@]','%40',stream_id)
    stream_id = re.sub('[#]','%23',stream_id)
    #print(stream_id)
    return stream_id

def get_instans_partisipant(sip, cid):
    stream_id = get_stream_id(cid)
    url = 'http://localhost/draft/v1/streams/'+stream_id+'/participants/'
    headers = {'content-type': 'application/json'}
    response = requests.get(url, headers=headers)
    response.status_code
    print(response.text)
    media = json.loads(response.text)
    print(len(media['data']['participants']))

    for i in range(len(media['data']['participants'])):
        if media['data']['participants'][i]['call_id'] == sip:
            instans = media['data']['participants'][i]['participant_id']
        else:
            pass
    print(instans)
    return instans

def remove_partisipant(cid, sip):
    stream_id = get_stream_id(cid)
    print(stream_id)
    instans = get_instans_partisipant(sip, cid)
    instans = re.sub('[@]','%40',instans)
    instans = re.sub('[/]','%2F',instans)
    instans = re.sub('[#]','%23',instans)
    url = 'http://localhost/draft/v1/streams/'+stream_id+'/participants/'+instans+'/'
    headers = {'content-type': 'application/json'}
    
    response = requests.delete(url, headers=headers)
    response.status_code
    print(response.status_code)
    print(response.text)
    
    

def repeat_invite(N):
    for i in range(N):
        print('invite ' + sip_1)
        invite_partisipant(cid, sip_1)
        time.sleep(5)
        
        print('invite ' + sip_2)
        invite_partisipant(cid, sip_2)
        time.sleep(5)
        
        print('invite ' + sip_3)
        invite_partisipant(cid, sip_3)
        time.sleep(5)
        
        print('invite ' + user_1)
        invite_partisipant(cid, user_1)
        time.sleep(5)
        
        #print('invite ' + user_2)
        #invite_partisipant(cid, user_2)
        #time.sleep(5)
        #invite_partisipant(cid, sip_4)
        #time.sleep(5)
        #invite_partisipant(cid, user)
        #time.sleep(5)
        print('invite ' + sip_5)
        invite_partisipant(cid, sip_5)
        time.sleep(5)
        #invite_partisipant(cid, sip_6)
        #time.sleep(5)
        #invite_partisipant(cid, h323_1)
        #time.sleep(5)
        #invite_partisipant(cid, h323_2)
        #time.sleep(5)
        #invite_partisipant(cid, h323_3)
        #time.sleep(5)
        #invite_partisipant(cid, rtsp)
        #time.sleep(5)
        time.sleep(10)


        print('remove ' + sip_1)
        remove_partisipant(cid, sip_1)
        time.sleep(5)

        print('remove ' + sip_2)
        remove_partisipant(cid, sip_2)
        time.sleep(5)

        print('remove ' + sip_3)
        remove_partisipant(cid, sip_3)
        time.sleep(5)
        #remove_partisipant(cid, sip_4)
        #time.sleep(5)

        print('remove ' + sip_5)
        remove_partisipant(cid, sip_5)
        time.sleep(5)
        #remove_partisipant(cid, sip_6)
        #time.sleep(5)
        #remove_partisipant(cid, h323_1)
        #time.sleep(5)
        #remove_partisipant(cid, h323_2)
        #time.sleep(5)
        #remove_partisipant(cid, h323_3)
        #time.sleep(5)

        print('remove ' + user_1)
        remove_partisipant(cid, user_1)
        time.sleep(5)

        #print('remove ' + user_2)
        #remove_partisipant(cid, user_2)
        #time.sleep(5)
        #remove_partisipant(cid, rtsp)
        #time.sleep(5)

repeat_invite(100)
#get_stream_id('chat')
      
#get_instans_partisipant('artem_7@aa111.trueconf.name')

