"""
Auteur : Fatma Aydin
"""
from django.urls import path, include
from . import views

app_name = 'client'

urlpatterns = [
    path('',views.client, name='index'),
    path('nouveauClient/', views.nouveauClient, name='nouveauClient'),
    path('modifierClient/<str:pk>', views.modifierClient, name='modifierClient'),
    path('supprimerClient/<str:pk>', views.supprimerClient, name='supprimerClient'),
]
