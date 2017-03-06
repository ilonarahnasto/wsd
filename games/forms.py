from django import forms
from games.models import Game
#Category, Page,
from django.contrib.postgres.forms import SimpleArrayField


class GameForm(forms.ModelForm):
    name = forms.CharField(max_length=250)
    description = forms.CharField(max_length=250)
    genre = forms.MultipleChoiceField( choices=Game.GENRES, widget=forms.CheckboxSelectMultiple)    
    image = forms.URLField(max_length=200)
    gameURL = forms.URLField(max_length=200)
    price = forms.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        model = Game
        fields = ('name', 'description', 'genre', 'image', 'gameURL', 'price')
