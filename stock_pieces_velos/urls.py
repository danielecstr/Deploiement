
from django.urls import path, include
from . import views

app_name='stock_pieces_velos'

urlpatterns = [
    path('', views.stock_pieces_velos, name='indexStockPiecesVelos'),
]