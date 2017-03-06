from django.conf.urls import url
from . import views

app_name = 'games'

urlpatterns = [

    #/games/payment/id/userid
    url(r'^payment/(?P<game_id>[0-9]+)/(?P<user_id>[0-9]+)/$', views.payment, name='payment'),
    url(r'^payment/error', views.error, name='error'),
    url(r'^add_game/', views.add_game, name='add_game'),
    url(r'^search/', views.search, name='search'),
    url(r'^delete/(?P<game_id>[0-9]+)/$', views.delete_game, name='delete'),
    url(r'^add_highscore/(?P<game_id>[0-9]+)/(?P<user_id>[0-9]+)/', views.add_highscore, name='add_highscore'),
    url(r'^get_highscores/(?P<game_id>[0-9]+)/', views.get_highscores, name='get_highscores'),
    url(r'^$', views.index, name='index'),

    #/games/id/
    url(r'^(?P<game_id>[0-9]+)/$', views.detail, name="detail"),

]
