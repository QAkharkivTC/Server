import json
import requests
import time

#http://localhost/api/v3.1/conferences/chat/invite?
#{"participants":["#tel:100"]}

#/api/v3.3/conferences/{{$conference_id}}/participants
#{"participants":["#rtsp://10.130.2.209/c/6518990187/"]}

def invite_partisipant(cid):
    url = 'http://localhost/api/v3.3/conferences/chat/invite?'              # в конференцию с cid "chat" вызываются rtsp трансялции конференций
    headers = {'content-type': 'application/json'}
    payload = {"participants":["#rtsp://10.130.2.209/c/cid_"+str(cid)+"/"]} # индекс созданых конференций 
    
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    response.status_code
    print(response.status_code)
    print(response.text)
    
    

def repeat_invite(N):
    for i in range(N):
        invite_partisipant(i)
        time.sleep(3)               # таймаут между каздым инфайтом трансялции в конференцию (можно подобрать для нагрузки)


repeat_invite(100)                  # указываем количество вызываемых трансялций


