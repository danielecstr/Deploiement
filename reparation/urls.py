from django.urls import path, include
from . import views

app_name = 'reparation'

urlpatterns = [
    path('réparations/', views.reparation, name='indexReparations'),
    path('réparationsDétails/', views.reparation, name='indexReparations'),

]
