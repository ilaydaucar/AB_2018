# -*- coding: utf-8 -*-

from django.http import *
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from election.profile.models import UserProfile
from django.contrib.auth import logout
from election.models import Survey


def home(request):
    querysets = Survey.objects.all()
    return render(request,"index.html" ,{'querysets': querysets})



def login_view(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login_view.html')
    else:
        return render(request, 'login_view.html')

def signup(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password_again = request.POST['password_again']
        user = UserProfile.objects.filter(email=email)
        print(user)

        if len(user)==0 :
           if password == password_again:
               user = UserProfile(name=name, email=email, password=password, is_active=True)
               user.set_password(password)
               user.save()
               return render(request, 'login_view.html')

        else:

                return render(request, 'login_view.html')

    else:
        return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    return redirect("/")





