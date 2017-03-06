from django import forms
from django.contrib.auth.models import User
from user.models import UserProfile
from django.core.validators import validate_email
from django.core.validators import URLValidator

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
