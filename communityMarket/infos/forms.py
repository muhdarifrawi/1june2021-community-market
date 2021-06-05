from django import forms

from .models import price_form


class PriceForm(forms.ModelForm):
    
    class Meta:
        model = price_form
        fields = ('name',)