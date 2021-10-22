"""
Auteur : Fatma Aydin
"""
from django.urls import path, include
from . import views

app_name = 'compte'

urlpatterns = [
    path('inscription',views.inscriptionPage, name='inscription'),
    path('login',views.loginPage, name='login'),
    path('quitter',views.logoutUser, name='quitter'),
    path('monCompte',views.monCompte, name='monCompte'),
]
