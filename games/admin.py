from django.contrib import admin
from .models import Game
from user.models import UserProfile

admin.site.register(UserProfile)

admin.site.register(Game)
