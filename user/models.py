from django.db import models

# Create your models here.
from django.utils import timezone

from lib.models import BaseModel


class User(BaseModel):
    stu_id = models.CharField(max_length=100,blank=False,null=False,unique=True)
    nick_name = models.CharField(max_length=100,blank=False,null=False)
    name = models.CharField(max_length=100, default='', blank=True)
    avatar = models.CharField(max_length=255,blank=False,null=False)
    gender = models.IntegerField(default=1)
    phone = models.CharField(max_length=100,blank=False,null=False)
    role = models.IntegerField(default=2,blank=True)


class UserOpenid(BaseModel):
    user_id = models.IntegerField()
    openid = models.CharField(max_length=255,blank=False,null=False)

    class Meta:
        unique_together = ('user_id', 'openid')
