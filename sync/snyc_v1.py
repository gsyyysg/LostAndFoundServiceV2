import os
import sys

import requests



def sync_user():
    url='https://lostandfound.yiwangchunyu.wang/service/user/getById'
    for i in range(10,700):
        r = requests.post(url,data={'id':i,'user_id':10152150127}).json()
        data=r['data']
        payload = {
            'phone':'',
            'gender':1,
            'stu_id' : data['user_id'],
            'nick_name': data['nick_name'],
            'avatar': data['avatar_url'],

        }
        if data['contact_type']=='手机号':
            payload['phone']=data['contact_value']
        payload['ctime']=data['ctime'].replace('T',' ').replace('Z','')

        r=requests.post('http://127.0.0.1:8000/service/user/insert',data=payload)
        print(r.json())
        if i%10==0:
            print(i,700)
if __name__=='__main__':
    sync_user()