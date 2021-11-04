"""
Auteur : Fatma Aydin
"""

from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import InscriptionForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Client
from .models import AuthUser
import datetime
from datetime import date


"""
Le bug se trouve dans ce code 

def get_logged_user_from_request(request):
    if 'loggeg_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        if len(Client.objects.filter(id=logged_user_id)) ==1:
            return Client.objects.get(id=logged_user_id)
        else:
            return None
    else:
        return None


def modify_profile(request):
        logged_user = get_logged_user_from_request(request)
        if logged_user:
            if len(request.GET) >0:
                form = InscriptionForm(request.GET,instance=logged_user)
            if form.is_valid():
                form.save()
                return redirect('/monCompte')
            else:
                return  render(request, 'monCompte.html', {'form':form})
        else:
            return redirect('inscription')
"""

def inscriptionPage(request):
    form = InscriptionForm()
    if request.method=='POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            nbmax = Client.objects.latest('cli_num').cli_num + 1
            client = Client(cli_nom=form.cleaned_data.get('last_name'), cli_prenom=form.cleaned_data.get('first_name'),cli_mail=form.cleaned_data.get('email'), cli_num=nbmax)
            client.save()
            password = make_password(form.cleaned_data.get('password1'), salt=None, hasher='default')
            nbmax = Client.objects.latest('cli_id')
            user = AuthUser(id=nbmax.cli_id,is_superuser=0,is_staff=0,is_active=1,date_joined=datetime.date.today(),password=password,username=form.cleaned_data.get("username"),first_name=form.cleaned_data.get('last_name'), last_name=form.cleaned_data.get('first_name'), email=form.cleaned_data.get("email"),CLI_ID=nbmax)
            user.save()
            userNom=form.cleaned_data.get('username')
            messages.success(request, 'Compte crée avec succès pour ' + userNom)
            return redirect('/compte/login')
    context={
        'form' : form
    }
    return render(request, 'compte/inscription.html', context)


def loginPage(request):
    context={
    }
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Nom d'utilisateur et/ou mot de passe erroné")
    return render(request, 'compte/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/compte/login')


def monCompte(request):
    context={
    }
    return render(request, 'compte/monCompte.html', context)
