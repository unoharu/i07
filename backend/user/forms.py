from django import forms
from .models import Customer, Table


class CustomerGroupForm(forms.Form):
    people = forms.IntegerField(
        label="顧客数",
        min_value=1,
        widget=forms.NumberInput(attrs={
            'class': 'spinner',
            'min': '1',
            'max': '40',
            'value': '1'
        })
    )