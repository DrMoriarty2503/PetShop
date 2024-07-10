from django import forms
from .models import Req

class ReqForm(forms.ModelForm):
    class Meta:
        model = Req
        fields = ['name', 'gen', 'sex', 'color', 'desc']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'gen': forms.TextInput(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
        }
