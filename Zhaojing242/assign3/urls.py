from django.conf.urls import url

from . import views


app_name = 'assign3'
urlpatterns = [
    #/assign3
    url(r'^$', views.index, name='index'),
    url(r'^secret/$', views.secret, name='secret'),
    url(r'^content/$', views.content, name='content'),
    url(r'^project/(?P<project_id>[0-9]+)$', views.project, name='project')
]
