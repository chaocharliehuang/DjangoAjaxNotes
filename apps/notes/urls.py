from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add, name='add'),
    url(r'^delete/(?P<id>[0-9]+)$', views.delete, name='delete'),
    url(r'^save/(?P<id>[0-9]+)$', views.save, name='save'),
]