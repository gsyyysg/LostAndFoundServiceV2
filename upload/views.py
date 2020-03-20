import os
import time

import requests
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from LostAndFoundServiceV2 import settings

@csrf_exempt
def avatar(request):
    res = {'code': 0, 'msg': 'success', 'data': []}
    required = {'avatar','user_id'}
    if not required.issubset(set(request.POST.keys())):
        return JsonResponse({'code': -1, 'msg': 'unexpected params!', 'data': {'required': list(required), 'yours': request.POST.dict()}})

    dir = '{0}/avatar'.format(settings.MEDIA_ROOT)
    if not os.path.exists(dir):
        os.makedirs(dir)
    fname = '{0}_{1}.jpg'.format(request.POST['user_id'], time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())))
    path = '{0}/{1}'.format(dir, fname)
    try:
        r = requests.get(request.POST['avatar'])
        with open(path, "wb") as code:
            code.write(r.content)
        res={
            'code': 0,
            'msg': 'success',
            'data': {
                'avatar':'{0}/media/avatar/{1}'.format(settings.URL_PREFIX, fname)
            }
        }
    except Exception as e:
        res={'code': -2, 'msg': e.__str__(), 'data': []}
    return JsonResponse(res)