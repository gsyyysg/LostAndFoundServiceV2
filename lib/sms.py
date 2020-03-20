#!/usr/bin/env python
#coding=utf-8
import json

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

def send(phoneNO, name, good_name):
    client = AcsClient('LTAI4FeLEc4Dip1GjscRKbZp', 'VU0g2It8wEaYDGWvXpJV0nUd9FkmzN', 'cn-hangzhou')

    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https') # https | http
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')

    request.add_query_param('RegionId', "cn-hangzhou")
    request.add_query_param('PhoneNumbers', phoneNO)
    request.add_query_param('SignName', "ELostFound")
    request.add_query_param('TemplateCode', "SMS_183242773")
    request.add_query_param('TemplateParam', json.dumps({'name':name,'goods_name':good_name}))
    print(json.dumps({'name':name,'good_name':good_name}))
    response = client.do_action_with_exception(request)
    # python2:  print(response)
    print(str(response, encoding = 'utf-8'))
