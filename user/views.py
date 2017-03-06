from user.forms import UserForm
from .models import UserProfile
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.core import mail
import random
from django import forms


def activate(request, user_id, n):
    # When user clicks activation link change status to active and log in
    user = User.objects.get(pk=user_id)
    user.is_active = True
    user.save()
    login(request, user)
    return render(request, 'user/activate.html')


def index(request):
    render(request, 'user/index.html')

def register(request):

    # A boolean value for telling the template whether the registration was successful.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        try:
            validate_email(request.POST.get("email", ""))
        except forms.ValidationError:
            print (user_form.errors)

        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            user.set_password(user.password)
            # Set status to inactive before validation
            user.is_active = False
            user.save()

            # Update our variable to tell the template registration was successful.
            registered = True

            # Generate activationlink it and send it to the dummy backend

            n = random.randint(0, 10000)
            activationlink = request.build_absolute_uri(reverse('user:activate', args=[user.id, n]))
            connection = mail.get_connection()
            activationmail = mail.EmailMessage(
                'Your activation link',
                activationlink,
                'no-reply@wsd2016.com',
                [user.email],
                connection=connection,
            )
            activationmail.send()

            connection.close()
            return render(request, 'user/register.html', {'user_form': user_form, 'registered': registered, 'activationlink': activationlink})
        else:
            print (user_form.errors)
            return render(request, 'user/register.html', {'user_form': user_form, 'registered': registered})

    # This form will be blank, ready for user input.
    else:
        user_form = UserForm()
        return render(request, 'user/register.html', {'user_form': user_form, 'registered': registered})

def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':

        # Gather the username and password provided by the user.
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)
        context = {'user':user}



        # If we have a User object, the details are correct.

        if user:

            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                if not request.POST.get('remember_me', None):
                    request.session.set_expiry(0)

                return HttpResponseRedirect('/games/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print ("Invalid login details")
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    else:

        return render(request, 'user/login.html', {})

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    return HttpResponseRedirect('/user/login/')

def detail(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'user/detail.html', {'user': user})
