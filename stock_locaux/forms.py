from django import forms
from .models import Local


class Localform(forms.ModelForm):
    class Meta:
        model = Local
        fields = '__all__'


#class Localform_modifier(forms.ModelForm):
 #   class Meta:
  #      model = Local
   #     fields = ['vel_num_cadre', 'vel_nom', 'vel_marque', 'vel_couleur', 'vel_type', 'vel_photo', 'vel_statut',
    #              'vel_etat', 'vel_remarque', 'local_id', 'don_id',
      #            ]
