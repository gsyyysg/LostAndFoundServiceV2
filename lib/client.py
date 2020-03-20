import json
import traceback

import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from LostAndFoundServiceV2.settings import URL_PREFIX
from lib.utils import log


def studentLogin(stu_id, stu_pwd):
    try:
        url = 'http://202.120.82.2:8081/ClientWeb/pro/ajax/login.aspx'
        params = {"id":stu_id,"pwd":stu_pwd,"act":'login'}
        r=requests.post(url, data=params,timeout=5).json()
        log('DEBUG','client studentLogin','request res',data=r)
        r['code']=1-r['ret']
    except Exception as e:
        traceback.print_exc()
        return {'code':-2,'msg':e.__str__(),'data':[]}
    return r

def getOpenid(code):
    data={
        'appid':'wxd8d5a2f6fa7f1878',
        'secret':'c1377133ab2c26acf453a0d7ed877710',
        'grant_type':'authorization_code',
        'js_code':code
    }
    url='https://api.weixin.qq.com/sns/jscode2session'
    try:
        print(data)
        r=requests.post(url,data=data)
    except:
        traceback.print_exc()
        return {'code':-1,'msg':'timeout | getopenid failed!','data':[]}
    return {'code':0, 'msg':'success','data':json.loads(r.text)}

def rpc(fc,data):
    url = URL_PREFIX+'/service/' + fc
    res={'code':-2,'msg':'error in rpc','data':[]}
    #尝试本地
    try:
        r=requests.post(url=url,data=data).json()
        log('DEBUG', '@client rpc', data=[url,r])
    except Exception as e:
        log('ERROR','@client rpc',e,data=url)
        res['msg']=e
        return res
    return r