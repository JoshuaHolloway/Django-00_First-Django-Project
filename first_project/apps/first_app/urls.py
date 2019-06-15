from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^new$', views.new),
    url(r'^(?P<my_val>\d+)$', views.show),
    url(r'^(?P<my_val>\d+)/edit$', views.edit),
    url(r'^(?P<my_val>\d+)/destroy$', views.destroy)
]