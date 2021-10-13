from django.shortcuts import render
"""Auteur : Daniele Castro"""
def home(request):
    return render(request, 'accueil/accueil.html')

def a_propos(request):
    return render(request, 'accueil/a_propos.html')

def contact(request):
    return render(request, 'accueil/contact.html')
