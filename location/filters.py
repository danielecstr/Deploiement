"""
Auteur : Daniele Castro
"""

import django_filters
from .models import Location_Velo

class LocationFilter(django_filters.FilterSet):

    class Meta:
        model=Location_Velo
        fields = ['loc_statut']

    def __init__(self, *args, **kwargs):
        super(LocationFilter, self).__init__(*args, **kwargs)
        self.filters['loc_statut'].label = "Statut de location  "

