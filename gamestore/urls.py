from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^user/', include('user.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^games/', include('games.urls')),
    url(r'^', include('homepage.urls')),
]
