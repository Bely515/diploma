from django import forms
from .models import Priority

class PriorityForm(forms.ModelForm):
    class Meta:
        model = Priority
        fields = ['name']
