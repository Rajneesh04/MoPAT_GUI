from django import forms
from .models import coordinates

class coordinateForm(forms.ModelForm):
    class Meta:
        model = coordinates
        fields = [
            'x_coordinate',
            'y_coordinate'
        ]