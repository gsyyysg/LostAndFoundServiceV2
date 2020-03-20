import json

from django.http import HttpResponse


class HttpJsonResponse(HttpResponse):
    def __init__(self, json_obj, *args, **kwargs):
        content=json.dumps(json_obj)
        super().__init__(content, *args, **kwargs)
