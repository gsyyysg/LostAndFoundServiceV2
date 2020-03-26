from django.conf.urls import url
from django.urls import include

from service import views

urlpatterns = [
    url(r'^$', views.hello),
    # url(r'^notify/', include('notify.urls')),
    url(r'^user/', include('user.urls')),
    url(r'^dynamic/', include('dynamic.urls')),
    url(r'^upload/', include('upload.urls'))
]