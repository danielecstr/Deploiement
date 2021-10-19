from django import forms
from .models import PieceDeVelo


class Piecesform(forms.ModelForm):
    class Meta:
        model = PieceDeVelo
        fields = '__all__'


class Piecesform_modifier(forms.ModelForm):
    class Meta:
        model = PieceDeVelo
        fields = ['piece_photo', 'piece_num_cadre', 'piece_nom', 'piece_type', 'piece_marque',
                  'piece_type_velo', 'piece_nb', 'piece_remarque', 'fourni_id', 'local_id',
                  'commande_fourni_id',
                  ]
