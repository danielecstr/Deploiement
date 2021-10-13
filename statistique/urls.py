"""
Auteur : Daniele Castro
"""

from django.urls import path, include
from . import views

app_name = 'statistique'

urlpatterns = [
    path('',views.statistique, name='index'),
]
