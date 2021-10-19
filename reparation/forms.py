from .models import ReparationVelos #Event (dans des anciens test pour le calendrier)

# from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput --- A modifier / supprimer
from django import forms



class Test(forms.ModelForm):
    class Meta:
        model = ReparationVelos
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


"""
class EventForm(forms.ModelForm): 
    class Meta:
        model = Event
        fields = ['name', 'start_date', 'end_date', 'start_time', 'end_time']
        widgets = {
            'start_date':DatePickerInput().start_of('event days'),
            'end_date':DatePickerInput().end_of('event days'),
            'start_time':TimePickerInput().start_of('party time'),
            'end_time':TimePickerInput().end_of('party time'),
        }
""" # A modifier / supprimer