from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField, JSONField
from decimal import Decimal
import json

class Game(models.Model):
    name = models.CharField(max_length=250)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=250, default='')
    date = models.DateTimeField(auto_now_add=True)
    image = models.URLField(max_length=200, default='')
    game = models.URLField(max_length=200, default='')
    price = models.DecimalField(max_digits=4, decimal_places=2, default=Decimal('0.10'))
    timesplayed = models.IntegerField(default=0)
    timesbought = models.IntegerField(default=0)
    highscores = JSONField(default=dict)
    bought = JSONField(default=list)

    #Genres defined here
    ACTION ='Action'
    ADVENTURE = 'Adveture'
    DRINKING = 'Drinking'
    EDUCATIONAL = 'Educational'
    FIGHTING = 'Fighting'
    RACING = 'Racing'
    LOGIC = 'Logic'
    PLATFORMER = 'Platformer'
    SHOOTER = 'Shooter'
    SPORTS = 'Sports'

    GENRES = (
    	(ACTION, 'action'),
	    (ADVENTURE, 'adventure'),
	    (DRINKING, 'drinking'),
	    (EDUCATIONAL, 'educational'),
	    (FIGHTING,'fighting'),
	    (RACING, 'racing'),
	    (LOGIC, 'logic'),
	    (PLATFORMER , 'platformer'),
	    (SHOOTER, 'shooter'),
	    (SPORTS, 'sports'),
    )

    genre = ArrayField(
    	models.CharField(
    		max_length = 25,
    	),
    	max_length = len(GENRES)
   	)

    def __unicode__(self):
        return self.name
