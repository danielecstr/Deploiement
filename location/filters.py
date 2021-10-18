"""
Auteur : Daniele Castro
"""

import django_filters
from .models import Location_Velo

class LocationFilter(django_filters.FilterSet):
    class Meta:
        model=Location_Velo
        fields = ['loc_statut']
