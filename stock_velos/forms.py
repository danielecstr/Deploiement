from django import forms
from .models import Velo, Local, Donateur


class Velosform(forms.ModelForm):
    class Meta:
        model = Velo
        fields = '__all__'


class Velosform_modifier(forms.ModelForm):
    class Meta:
        model = Velo
        fields = ['vel_num_cadre', 'vel_nom', 'vel_marque', 'vel_couleur', 'vel_type', 'vel_photo', 'vel_statut',
                  'vel_etat', 'vel_remarque', 'local_id', 'don_id',
                  ]
