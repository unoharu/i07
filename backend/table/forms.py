from django import forms

class TableIDForm(forms.Form):
    table_id = forms.IntegerField(label='Table ID')