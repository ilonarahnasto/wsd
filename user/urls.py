from . import views
from django.http import HttpResponse
from django.conf.urls import url
from user.views import *

app_name = 'user'

urlpatterns = [
    # /user/login
    url(r'^login/$', views.user_login, name='login'),
    # /user/logout
    url(r'^logout/$', views.user_logout, name='logout'),
    # /user/activate/id/XX
    url(r'^activate/(?P<user_id>[0-9]+)/(?P<n>[0-9]+)$', views.activate, name='activate'),
    # /user/register
    url(r'^register/$', views.register, name='register'),
]
