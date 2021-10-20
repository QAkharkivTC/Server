import json
import requests
import time

#http://localhost/api/v3.1/conferences/chat/invite?
#{"participants":["#tel:100"]}

#/api/v3.3/conferences/{{$conference_id}}/participants

def invite_partisipant():
    url = 'http://localhost/api/v3.3/conferences/chat/invite?'
    headers = {'content-type': 'application/json'}
    payload = {"participants":["#sip:100@10.130.3.42"]}
    
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    response.status_code
    print(response.status_code)
    print(response.text)
    
    

def repeat_invite(N):
    for i in range(N):
        invite_partisipant()
        time.sleep(1)


repeat_invite(100)       


