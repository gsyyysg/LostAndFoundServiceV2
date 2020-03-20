import json
import traceback

from django.core import serializers
from django.db import models
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from pyexpat import model

from lib import client
from lib.client import studentLogin, rpc
from lib.utils import log
from user.models import UserOpenid, User


@csrf_exempt
def getOpenid(request):
    if not {'js_code'}.issubset(set(request.POST.keys())):
        return HttpResponse(json.dumps({'code': -1, 'msg': 'unexpected params!', 'data': request.POST.dict()}))
    res=client.getOpenid(request.POST['js_code'])
    return HttpResponse(json.dumps(res))

@csrf_exempt
def loginByOpenid(request):
    res={'code':0, 'msg':'success', 'data':[]}
    required={'openid'}
    if not required.issubset(set(request.POST.keys())):
        return HttpResponse(json.dumps({'code': -1, 'msg': 'unexpected params!', 'data': {'required':required,'yours':request.POST.dict()}}))
    try:
        openid=request.POST['openid']
        user_openid=UserOpenid.objects.get(openid=openid, status=1)
        user_info=User.objects.get(id=user_openid.user_id)
        res['data']=user_info.toJSON()
    except models.Model.DoesNotExist:
        res={'code':-2, 'msg':'need login,please', 'data':[]}
    except models.Model.MultipleObjectsReturned:
        res={'code':-2, 'msg':'MultipleObjectsReturned', 'data':[]}
    except Exception as e:
        res={'code':-2, 'msg':e, 'data':[]}
    return HttpResponse(json.dumps(res))

@csrf_exempt
def login(request):
    res={'code':0, 'msg':'success', 'data':[]}
    required={'openid','stu_id','password','phone','avatar','gender'}
    if not required.issubset(set(request.POST.keys())):
        return JsonResponse({'code': -1, 'msg': 'unexpected params!', 'data': {'required':list(required),'yours':request.POST.dict()}})
    try:
        #鉴权：
        login_res=studentLogin(request.POST['stu_id'],request.POST['password'])
        if login_res['code']!=0:
            return JsonResponse(login_res)
        else:
            #鉴权通过
            #注册或更新用户信息
            stu_id=request.POST['stu_id']
            dict=request.POST.dict().copy()
            update={
                'nick_name':dict['nick_name'],
                'name':login_res['data']['name'],
                'gender':dict['gender'],
                'phone':dict['phone'],
                'avatar':dict['avatar']
            }
            user,created=User.objects.update_or_create(stu_id=stu_id,defaults=update)
            # 更新openid
            obj, created = UserOpenid.objects.update_or_create(
                openid=request.POST['openid'], user_id=user.id,
                defaults={'status': 1}
            )
            #将头像存在本地
            rpc_res=rpc(fc='upload/avatar',data={'avatar':user.avatar,'user_id':user.id})
            if rpc_res['code']!=None:
                if rpc_res['code']==0:
                    user.avatar = rpc_res['data']['avatar']
                    user.save()
                else:
                    log('ERROR','user login','faild to save avatar',data=user.avatar)

            res['data']=user.format()

    except Exception as e:
        res={'code':-2, 'msg':e.__str__(), 'data':[]}
        log('ERROR','user login last exception',e.__str__())
    return JsonResponse(res)

@csrf_exempt
def logout(request):
    res={'code':0, 'msg':'success', 'data':[]}
    required={'user_id'}
    if not required.issubset(set(request.POST.keys())):
        return JsonResponse({'code': -1, 'msg': 'unexpected params!', 'data': {'required':required,'yours':request.POST.dict()}})
    try:
        user_id=request.POST['user_id']
        UserOpenid.objects.filter(user_id=user_id).update(status=1)
    except models.Model.DoesNotExist:
        res={'code':-2, 'msg':'DoesNotExist', 'data':[]}
    except models.Model.MultipleObjectsReturned:
        res={'code':-2, 'msg':'MultipleObjectsReturned', 'data':[]}
    except Exception as e:
        res={'code':-2, 'msg':e, 'data':[]}
    return HttpResponse(json.dumps(res))

@csrf_exempt
def update(request):
    res = {'code': 0, 'msg': 'success', 'data': []}
    required = {'user_id','update'}
    if not required.issubset(set(request.POST.keys())):
        return JsonResponse(
            {'code': -1, 'msg': 'unexpected params!', 'data': {'required': required, 'yours': request.POST.dict()}})
    try:
        user_id = request.POST['user_id']
        update = request.POST['update'].dict()
        user=User.objects.filter(id=user_id).update(update)
        res['data']=user.toJSON()
    except Exception as e:
        res = {'code': -2, 'msg': e, 'data': []}
    return HttpResponse(json.dumps(res))

def get(request):
    res = {'code': 0, 'msg': 'success', 'data': []}
    required = {'user_id'}
    if not required.issubset(set(request.POST.keys())):
        return JsonResponse(
            {'code': -1, 'msg': 'unexpected params!', 'data': {'required': required, 'yours': request.POST.dict()}}
        )
    try:
        user_id = request.POST['user_id']
        user=User.objects.get(id=user_id)
        res['data']=user.toJSON()
    except models.Model.DoesNotExist:
        res = {'code': -2, 'msg': 'DoesNotExist', 'data': []}
    except models.Model.MultipleObjectsReturned:
        res = {'code': -2, 'msg': 'MultipleObjectsReturned', 'data': []}
    except Exception as e:
        res = {'code': -2, 'msg': e, 'data': []}
    return HttpResponse(json.dumps(res))