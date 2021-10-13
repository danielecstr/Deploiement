from django.urls import path, include
from . import views

app_name='stock_velos'

urlpatterns = [
    path('', views.stock_velos, name='indexStockVelos'),
    path('<int:id>/', views.details_velo, name='indexDetailsVelo'),
    path('nouveau_velo/', views.nouveau_velo, name='indexNouveauVelo'),
    path('modifier_velo/<str:pk>', views.modifier_velo, name='indexModifierVelo'),
    path('supprimer_velo/<str:pk>', views.supprimer_velo, name='indexSupprimerVelo'),
]
