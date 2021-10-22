
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accueil.urls')),
    path('location/',include('location.urls')),
    path('client/',include('client.urls')),
    path('compte/',include('compte.urls')),
    path('stock_velos/',include('stock_velos.urls')),
    path('stock_pieces_velos/',include('stock_pieces_velos.urls')),
    path('stock_locaux/',include('stock_locaux.urls')),
    path('réparations/', include('reparation.urls')),
    path('statistique/', include('statistique.urls')),

    path('', include('cal.urls')),  # fatma (22.10)
]
