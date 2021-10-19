from django.urls import path, include
from . import views

app_name='stock_locaux'

urlpatterns = [
    path('', views.stock_locaux, name='indexStockLocaux'),
    path('ajouter_local/', views.nouveau_local, name='indexNouveauLoc'),
]
