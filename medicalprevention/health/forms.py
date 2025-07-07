# symptom_checker/forms.py

from django import forms

class SymptomForm(forms.Form):
    description = forms.CharField(
        label='Describe your symptoms',
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40})
    )
