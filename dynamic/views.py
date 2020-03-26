
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from dynamic.models import Category, Dynamic
from lib import client, sms, utils
from lib.view import formatQuerySet, check


@csrf_exempt
def categories(request):
    res={'code':0, 'msg':'success', 'data':[]}
    try:
        categpries=Category.objects.all()
        categpries=formatQuerySet(categpries)
        res['data']=categpries
    except Exception as e:
        res={'code':-2, 'msg':e.__str__(), 'data':[]}
        utils.log('ERROR','dynamic categories',res['msg'],data='')
    return JsonResponse(res)

@csrf_exempt
def create(request):
    res = {'code': 0, 'msg': 'success', 'data': []}
    params=request.POST.dict()
    required={
        'user_id':{'required':True},
        'type' : {'required':True},
        'category' : {'required':True},
        'title': {'required': True},
        'desc' : {'required':True},
        'images' : {'required':False},
        'location' : {'required':False},
        'meta' : {'required':False},
    }
    check_res=check(required,params)
    if check_res is None or check_res['code']!=0:
        return JsonResponse(check_res)

    try:
        Dynamic.objects.create(**params)
        #校园卡专区
        if params.get('type')==2 and params.get('category')==1: #
            if params.get('meta',False) and len(params['meta'])>2: #提取学号
                #提取手机号
                rpc_res=client.rpc('user/get',{'stu_id':params['meta']})
                if rpc_res is None or rpc_res['code']!=0:
                    utils.log('ERROR','dynamic create', 'get use phone NO failed.', data=rpc_res)
                if len(rpc_res['data']['phone'])>2:
                    sms.send_for_loser(
                        phoneNO=rpc_res['data']['phone'],
                        name=rpc_res['data']['name'],
                        good_name=params['title']
                    )

    except Exception as e:
        res={'code':-2, 'msg':e.__str__(), 'data':[]}
        utils.log('ERROR', 'dynamic create', res['msg'], data=params)
    return JsonResponse(res)


@csrf_exempt
def list(request):
    res = {'code': 0, 'msg': 'success', 'data': {}}
    params = request.POST.dict()
    required = {
        'id': {'required': False},
        'user_id': {'required': False},
        'type': {'required': False},
        'category': {'required': False},
        'title': {'required': False},
        'desc': {'required': False},
        'state': {'required': False},
        'belongsTo': {'required': False},
        'page': {'required': False},
        'size': {'required': False},
    }
    check_res = check(required, params)
    page=int(params.get('page',0))
    size=int(params.get('size',10))
    if 'size' in params:
        params.pop('size')
    if 'page' in params:
        params.pop('page')
    params['status']=1

    if check_res is None or check_res['code'] != 0:
        return JsonResponse(check_res)

    try:
        cnt=Dynamic.objects.filter(**params).count()
        data=Dynamic.objects.filter(**params)[page*size:(page+1)*size]
        res['data']['cnt'] = cnt
        res['data']['dynamics']=[]
        for obj in data:
            obj=obj.format()
            res['data']['dynamics'].append(obj)
    except Exception as e:
        res = {'code': -2, 'msg': e.__str__(), 'data': []}
        utils.log('ERROR', 'dynamic list', res['msg'], data=params)
    return JsonResponse(res)

@csrf_exempt
def update(request):
    res = {'code': 0, 'msg': 'success', 'data': {}}
    params = request.POST.dict()
    required = {
        'id':{'requried':True},
        'user_id': {'required': False},
        'type': {'required': False},
        'category': {'required': False},
        'title': {'required': False},
        'desc': {'required': False},
        'images': {'required': False},
        'location': {'required': False},
        'meta': {'required': False},
    }
    check_res = check(required, params)
    if check_res is None or check_res['code'] != 0:
        return JsonResponse(check_res)

    id=params['id']
    params.pop('id')

    try:
        Dynamic.objects.filter(id=id).update(**params)

    except Exception as e:
        res = {'code': -2, 'msg': e.__str__(), 'data': []}
        utils.log('ERROR', 'dynamic update', res['msg'], data=params)
    return JsonResponse(res)

@csrf_exempt
def delete(request):
    res = {'code': 0, 'msg': 'success', 'data': {}}
    params = request.POST.dict()
    required = {
        'id': {'requried': True},
        'user_id': {'requried': True}
    }
    check_res = check(required, params)
    if check_res is None or check_res['code'] != 0:
        return JsonResponse(check_res)
    try:
        Dynamic.objects.filter(id=params['id'],user_id=params['user_id']).update(status=0)
    except Exception as e:
        res = {'code': -2, 'msg': e.__str__(), 'data': []}
        utils.log('ERROR', 'dynamic delete', res['msg'], data=params)
    return JsonResponse(res)

@csrf_exempt
def apply(request):
    res = {'code': 0, 'msg': 'success', 'data': {}}
    params = request.POST.dict()
    required = {
        'id': {'requried': True},
        'user_id': {'requried': True}
    }
    check_res = check(required, params)
    if check_res is None or check_res['code'] != 0:
        return JsonResponse(check_res)

    try:
        dynamic=Dynamic.objects.get(id=params['id'])
        if dynamic.state==1:#
            dynamic.state=2
            dynamic.belongsTo=params['user_id']
            res['data']['user_info']=dynamic.format()['user_info']
            dynamic.save()
        else:
            res = {'code': -3, 'msg': '他人正在申领', 'data': dynamic.format()}
            return JsonResponse(res)
        #发消息确认

    except Exception as e:
        res = {'code': -2, 'msg': e.__str__(), 'data': []}
        utils.log('ERROR', 'dynamic apply', res['msg'], data=params)
    return JsonResponse(res)


@csrf_exempt
def confirm(request):
    res = {'code': 0, 'msg': 'success', 'data': {}}
    params = request.POST.dict()
    required = {
        'id': {'requried': True},
        'user_id': {'requried': True}
    }
    check_res = check(required, params)
    if check_res is None or check_res['code'] != 0:
        return JsonResponse(check_res)

    try:
        dynamic = Dynamic.objects.get(id=params['id'])
        if int(params['user_id'])!=dynamic.user_id:
            res = {'code': -3, 'msg': '当前用户无确认权限', 'data': dynamic.format()}
            return JsonResponse(res)
        if dynamic.state == 2:  #
            dynamic.state = 3
            dynamic.save()
        else:
            res = {'code': -3, 'msg': '状态不可确认', 'data': dynamic.format()}
            return JsonResponse(res)
    except Exception as e:
        res = {'code': -2, 'msg': e.__str__(), 'data': []}
        utils.log('ERROR', 'dynamic confirm', res['msg'], data=params)
    return JsonResponse(res)

@csrf_exempt
def reject(request):
    res = {'code': 0, 'msg': 'success', 'data': {}}
    params = request.POST.dict()
    required = {
        'id': {'requried': True},
        'user_id': {'requried': True}
    }
    check_res = check(required, params)
    if check_res is None or check_res['code'] != 0:
        return JsonResponse(check_res)

    try:
        dynamic = Dynamic.objects.get(id=params['id'])
        if int(params['user_id'])!=dynamic.user_id:
            res = {'code': -3, 'msg': '当前用户无权限', 'data': dynamic.format()}
            return JsonResponse(res)
        if dynamic.state == 2:  #
            dynamic.state = 1
            dynamic.save()
        else:
            res = {'code': -3, 'msg': '状态不可拒绝', 'data': dynamic.format()}
            return JsonResponse(res)
    except Exception as e:
        res = {'code': -2, 'msg': e.__str__(), 'data': []}
        utils.log('ERROR', 'dynamic reject', res['msg'], data=params)
    return JsonResponse(res)