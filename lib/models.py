from django.db import models

# Create your models here.
from django.utils import timezone



class BaseModel(models.Model):
    status = models.IntegerField(default=1, blank=True)
    ctime = models.DateTimeField(default=timezone.now, blank=True)
    mtime = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        abstract = True

    def format(self, if_time_format=True,time_format=''):
        import json
        dict={}
        for f in self._meta.fields:
            dict[f.name]=getattr(self,f.name)
        for key in dict:
            if 'time' in key:
                dict[key]=dict[key].strftime("%Y-%m-%d %H:%M:%S")
        return dict

    def querysetToJson(self,qset,if_time_format=True,time_format=''):
        return list(qset)

