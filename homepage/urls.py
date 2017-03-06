from django.conf.urls import url
from . import views
from django.http import HttpResponse

app_name = 'homepage'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
