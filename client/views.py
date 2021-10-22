"""
Auteur : Fatma Aydin
"""

from django.shortcuts import render, redirect
from .models import Client
from .forms import ClientForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='/compte/login')
def client(request):
    client = Client.objects.all()

    client_number = client.count()
    messageNbClient = f'{client_number} clients :'

    if client_number == 1:
        messageNbClient = f'{client_number} client :'


    context = {
        'client' : client,
        'messageNbClient' : messageNbClient,
    }
    return render(request, 'client/client.html', context)

@login_required(login_url='/compte/login')
def nouveauClient(request):
    formClient = ClientForm()
    if request.method=='POST':
        formClient = ClientForm(request.POST)
        if formClient.is_valid():
            formClient.save()
            return redirect('/client')
    context = {
        'formClient' : formClient,
    }
    return render(request, 'client/nouveauClient.html', context)

@login_required(login_url='/compte/login')
def modifierClient(request, pk):
    client = Client.objects.get(cli_id=pk)
    formClient=ClientForm(instance=client)
    if request.method=='POST':
        formClient=ClientForm(request.POST, instance=client)
        if formClient.is_valid():
            formClient.save()
            return redirect('/client')
    context = {
        'formClient' : formClient
    }
    return render(request, 'client/nouveauClient.html', context)

@login_required(login_url='/compte/login')
def supprimerClient(request, pk):
    client = Client.objects.get(cli_id=pk)
    if request.method=='POST':
        client.delete()
        return redirect('/client')
    context = {
        'item': client,
    }
    return render(request, 'client/supprimerClient.html', context)

