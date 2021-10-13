from django import forms
from .models import Velo, Local, Donateur

class Velosform(forms.ModelForm):
    class Meta:
        model = Velo
        fields = '__all__'