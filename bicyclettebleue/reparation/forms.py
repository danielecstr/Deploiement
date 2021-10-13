from django import forms
from .models import Reparation_velos

from django.db import models
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import widgets



class Test(forms.ModelForm):
    class Meta:
        model = Reparation_velos
        fields = ['rep_date_heure']
        widgets = {
            'rep_date_heure': forms.DateInput(attrs={'type': 'date', 'class': 'datepicker'})
    }


rep_date_heure = forms.DateField()
"""
    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)
        self.fields['rep_date_heure'].widget = AdminDateWidget()
"""
