"""Auteur : Daniele Castro"""

from django.urls import path, include
from . import views

app_name = 'accueil'

urlpatterns = [
    path('',views.home, name="index"),
    path('a_propos/',views.a_propos, name="a_propos"),
    path('contact/',views.contact, name="contact"),
]
