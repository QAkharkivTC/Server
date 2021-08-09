import requests
import json
import logging
import time
import urllib3
import certifi
import ssl

client_id = ''
client_name = ''
client_secret = ''
access_token = ''

def create_client(localhost, token):

    ssl._create_default_https_context = ssl._create_unverified_context
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    r = requests.post('https://'+localhost+'/api/v3/api-clients?access_token='+token+'',
                      data= {"client_name":"localhost",
                             "redirect_uri":"https://localhost",
                             "scope":"conferences "+
                             "conferences:read "+
                                 "conferences:write "+
                                 "conferences.participants "+
                                 "conferences.participants:read "
                                 "conferences.participants:write "+
                                 "conferences.operators:read "+
                                 "conferences.operators:write "+
                                 "conferences.invitations "+
                                 "groups "+
                                 "groups:read "+
                                 "groups:write "+
                                 "groups.users "+
                                 "groups.users:read "+
                                 "groups.users:write "+
                                 "users users:read "+
                                 "users:write "+
                                 "users.avatar:read "+
                                 "users.avatar:write "+
                                 "users.addressbook "+
                                 "users.addressbook:read "+
                                 "users.addressbook:write "+
                                 "templates.conferences:read "+
                                 "templates.conferences:write "+
                                 "directory.servers:read "+
                                 "logs.calls:read "+
                                 "logs.calls.participants:read "+
                                 "logs.calls.invites:read "+
                                 "conferences.video_layouts:read "+
                                 "conferences.video_layouts:write "+
                                 "conferences.video_layouts.personal:read "+
                                 "conferences.video_layouts.personal:write "+
                                 "conferences.records "+
                                 "conferences.records:read "+
                                 "conferences.records:write "+
                                 "conferences.sessions:read "+
                                 "conferences.sessions.participants:read "+
                                 "conferences.sessions.podiums.participants:read "+
                                 "conferences.sessions.podiums.participants:write"}, verify=False)

    r.status_code
    print("API OAuth2 created with code: ", r.status_code)
    media = json.loads(r.text)

    global client_id
    global client_secret
    client_id = media['client']['id']
    client_name = media['client']['client_name']
    client_secret = media['client']['client_secret']
    

def make_token(localhost, client_id, client_secret, token):
    
    ssl._create_default_https_context = ssl._create_unverified_context
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    data = {'grant_type':'client_credentials', 'client_id': client_id , 'client_secret': client_secret}
    headers = {'Cache-Control':'max-age=0',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
        'Content-Type':'application/x-www-form-urlencoded',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer':'https://www.groupon.com/signup',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'es-ES,es;q=0.8'
        }
    
    r = requests.post('https://'+localhost+'/oauth2/v1/token?access_token='+token+'', headers=headers , data=data, verify=False)

    global access_token
    media = json.loads(r.text)
    access_token = media['access_token']
    print("API OAuth2 token was made: ", r.status_code, " access_token: ", access_token)
    
    

def delete_client(localhost, client_id, token):
    
    ssl._create_default_https_context = ssl._create_unverified_context
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    r = requests.delete('https://'+localhost+'/api/v3/api-clients/'+client_id+'?access_token='+token+'', verify=False)

    r.status_code
    print("API OAuth2 was delete: ", r.status_code)
    #print(r.status_code)
    print(r.text)



localhost = str(input("Укажите адрес "  ))
token = str(input("Укажите токен "  ))    
    
create_client(localhost, token)
make_token(localhost, client_id, client_secret, token)

#print("access_token: ", access_token)
#delete_client(client_id)
