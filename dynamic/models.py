import json

from django.db import models

# Create your models here.
from lib import client
from lib.models import BaseModel

STATE_DICT={
    1:'待申领',
    2:'待确认',
    3:'申领成功'
}

class Category(BaseModel):
    name = models.CharField(max_length=255,blank=False,null=False,unique=True)

    def __str__(self):
        return self.name

class Dynamic(BaseModel):
    user_id = models.IntegerField()
    type = models.IntegerField(default=1)  #1:lost 2:found
    category = models.IntegerField(default=1)
    title = models.TextField(default='')
    desc = models.TextField(default='')
    images = models.TextField(default=json.dumps([]))
    location = models.TextField(default=json.dumps({}), blank=True, null=False)
    meta = models.CharField(max_length=255, default='',null=True,blank=True)

    belongsTo = models.IntegerField(default=1) #流转状态
    state = models.IntegerField(default=1) #流转状态

    def format(self, if_time_format=True, time_format=''):
        dict = super().format(if_time_format, time_format)
        dict['state']=STATE_DICT[dict['state']]
        dict['images'] = json.loads(dict['images'])
        dict['location'] = json.loads(dict['location'])
        user_res=client.rpc('user/get',{'id':dict['user_id']})
        dict['user_info']=user_res['data']
        return dict

# class Recode(BaseModel):
#     user_id = models.IntegerField()
#     dynamic_id = models.IntegerField()
#     state = models.IntegerField(default=2)  # 流转状态