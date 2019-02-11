from django import forms
from .models import Station

class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = ['name']
    def get_queryset(self):
        return Station.objects.all()