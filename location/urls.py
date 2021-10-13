"""
Auteur : Daniele Castro
"""

from django.urls import path, include
from . import views

app_name = 'location'

urlpatterns = [
    path('',views.location, name='index'),
    path('locationEnAttente/', views.locationEnAttente, name='locationEnAttente'),
    path('<int:id>/', views.detailsLocation, name='detailsLocation'),
    path('detailsLocationEnAttente/<int:id>', views.detailsLocationEnAttente, name='detailsLocationEnAttente'),
    path('confirmationLocation/<str:pk>', views.confirmationLocation, name='confirmationLocation'),
    path('nouvelleLocation/', views.nouvelleLocation, name='nouvelleLocation'),
    path('modifierLocation/<str:pk>', views.modifierlocation, name='modifierLocation'),
    path('supprimerLocation/<str:pk>',views.supprimerLocation, name='supprimerLocation'),
    path('refuseLocationEnAttente/<str:pk>',views.refuseLocationEnAttente, name='refuseLocationEnAttente'),



    path('locationClient/<str:pk>',views.locationClient, name='locationClient'),
    path('detailsLocation/<int:id>', views.detailsLocationClient, name='detailsLocationClient'),
    path('nouvelleLocationClient/', views.choixVeloClient, name='choixVeloClient'),
    path('modifierLocationClient/<str:pk>', views.modifierlocationClient, name='modifierLocationClient'),
    path('supprimerLocationClient/<str:pk>', views.supprimerLocationClient, name='supprimerLocationClient'),
    path('finaliserLocationClient/<str:pk>', views.finaliserLocationClient, name='finaliserLocationClient'),
    path('choixVelo/', views.choixVeloClient, name='choixVeloClient'),
    path('donneeLocationClient/<str:pk>', views.donneeLocationClient, name='donneeLocationClient'),
]
