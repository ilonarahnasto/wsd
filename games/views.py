from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .models import Game
from .forms import GameForm
from datetime import datetime
from django.utils.formats import get_format
from django.utils.dateformat import DateFormat
from django.template import Context
from django.template.loader import render_to_string
from user.models import UserProfile
from django.core.urlresolvers import reverse
from hashlib import md5
from django.db.models import Q
from django.db import models
from django.contrib.postgres.fields import ArrayField
import json
import operator
from django.contrib.auth.models import User
import itertools
from itertools import islice
import random

def delete_game(request, game_id):
    # build the absolute urls
    gamesurl = request.build_absolute_uri(reverse('games:index'))
    detailurl = request.build_absolute_uri(reverse('games:detail', args=[game_id]))
    game = Game.objects.get(pk=game_id)
    # if OK is pressed, delete game and redirect to /games/
    if request.method == 'POST':
        game.delete()
        return HttpResponseRedirect(gamesurl)
    return render(request, 'games/delete.html', {'gamesurl': gamesurl, 'detailurl': detailurl, 'game': game})

def add_game(request):
    gamesurl = request.build_absolute_uri(reverse('games:index'))
    if request.method == 'POST':
        game_form = GameForm(request.POST)
        # Save attributes for game and redirect to /games/
        if game_form.is_valid():
            game_name = game_form.cleaned_data['name']
            game_description = game_form.cleaned_data['description']
            game_uploader = request.user
            game_date = DateFormat(datetime.now()).format(get_format('DATE_FORMAT'))
            game_genre = game_form.cleaned_data['genre']
            game_image = game_form.cleaned_data['image']
            game_url = game_form.cleaned_data['gameURL']
            game_price = game_form.cleaned_data['price'] #uusi rivi???
            new_game = Game(name=game_name, uploader = game_uploader, description=game_description, date = game_date, genre = game_genre, image = game_image, game = game_url, price = game_price)
            new_game.save()
            return HttpResponseRedirect(gamesurl)
    else:
        game_form = GameForm()
    return render(request, 'games/add_game.html', {'gamesurl': gamesurl, 'game_form': game_form})

def index(request):
    # Get games ordered by date and name
    all_games = Game.objects.all().order_by('-date')
    all_games_alph = Game.objects.all().order_by('name')
    context = {'all_games': all_games, 'all_games_alph': all_games_alph}
    return render(request, 'games/index.html', context)

def detail(request, game_id):
    # Fetch the game
    try:
        game = Game.objects.get(pk=game_id)
    except Game.DoesNotExist:
        raise Http404("Question does not exist")
    # Modify stats
    game.timesplayed += 1
    game.save()
    scores = sorted(game.highscores.items(), key=operator.itemgetter(1), reverse=True)
    top = itertools.islice(scores, 10)
    return render(request, 'games/detail.html', {'game': game, 'topscores':top})

def payment(request, game_id, user_id):
    # Generate absolute urls
    detailurl = request.build_absolute_uri(reverse('games:detail', args=[game_id]))
    gamesurl = request.build_absolute_uri(reverse('games:index'))
    errorurl = request.build_absolute_uri(reverse('games:error'))
    # Generate randomn payment id
    pid = random.randint(0, 10000)
    game = Game.objects.get(pk=game_id)
    game.timesbought += 1
    game.save()
    price = game.price
    checksumstr = "pid={}&sid={}&amount={}&token={}".format(pid, "wsd2016", game.price, "0ff89cef7ccd657d845c71b4fe5a87c5")
    m = md5(checksumstr.encode("ascii"))
    checksum = m.hexdigest()
    # Add access to the user
    if game.bought:
        game.bought.append(int(user_id))
    else:
        game.bought = [int(user_id)]
    game.save()
    return render(request, 'games/payment.html', {'game': game, 'gamename': game.name, 'errorurl': errorurl, 'gamesurl': gamesurl, 'detailurl': detailurl, 'checksum': checksum, 'price': price, 'pid': pid, 'game_id': game.id})

def error(request):
    return HttpResponse('<h1>There was an error in the payment<h1>')

    # Search function
def search(request):
    query = request.GET.get('q')
    if query:
        results = Game.objects.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(genre__icontains=query))
    else:
        results = Game.objects.all()
    context = dict(results=results, q=query)
    return render(request, 'games/index.html', context)

def add_highscore(request, game_id, user_id):
    score = request.GET['score']
    game = Game.objects.get(pk=game_id)
    user = User.objects.get(pk=user_id).username
    valid = False
    if game.highscores:
        if user in game.highscores.keys():
            if game.highscores[user] < int(score):
                game.highscores[user] = int(score)
                valid = True
        else:
            game.highscores[user] = int(score)
            valid = True
    else:
        game.highscores = {user : int(score)}
        valid = True
    game.save()
    userscore = game.highscores[user]
    html = render_to_string('games/highscore.html', {'user_id': user_id, 'score':score, 'scorevalid':valid, 'userscore':userscore })
    return HttpResponse(html)

def get_highscores(request, game_id):
    game = Game.objects.get(pk=game_id)
    scores = sorted(game.highscores.items(), key=operator.itemgetter(1), reverse=True)
    top = itertools.islice(scores, 10)
    html = render_to_string('games/get_highscores.html', {'game': game, 'topscores':top})
    return HttpResponse(html)
