from attr import field
from django import forms

from .models import reservation

class ReservationForm(forms.ModelForm):
    class Meta: # Metadata ig
        model = reservation # The model name
        fields = '__all__' # Since we need all fields we give that dunner method