from django.urls import path, re_path

from dynamic import views

urlpatterns = [
    re_path(r'^categories$', views.categories),
    re_path(r'^create$', views.create),
    re_path(r'^list', views.list),
    re_path(r'^delete$', views.delete),
    re_path(r'^update', views.update),
    re_path(r'^apply$', views.apply),
    re_path(r'^confirm$', views.confirm),
    re_path(r'^reject$', views.reject),
]