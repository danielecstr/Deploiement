
from django.urls import path, include
from . import views

app_name = 'stock_pieces_velos'

urlpatterns = [
    path('', views.stock_pieces_velos, name='indexStockPiecesVelos'),
    path('nouvelle_piece/', views.nouvelle_piece, name='indexNouvellePiece'),
    path('supprimer_piece/<str:num>', views.supprimer_piece, name='indexSupprimerPiece'),
    path('modifier_piece/<str:num>', views.modifier_piece, name='indexModifierPiece'),
    path('details_piece/<str:num>', views.details_piece, name='indexDetailsPiece'),
    #path('commander_pieces/<str:num>', views.commander_piece, name='indexCommanderPieces'),
]