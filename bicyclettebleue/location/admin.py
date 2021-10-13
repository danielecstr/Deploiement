"""
Auteur : Daniele Castro
"""

from django.contrib import admin
from .models import Velo
from .models import Location
from .models import Client
from .models import Location_Velo

admin.site.register(Location_Velo)
admin.site.register(Location)
admin.site.register(Velo)
admin.site.register(Client)
