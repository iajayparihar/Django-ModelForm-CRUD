from django import forms
from .models import userModel
class userForms(forms.ModelForm):
    class Meta:
        model= userModel
        fields = '__all__'
        widgets = {
            "first_name": forms.TextInput(attrs={'class':'form-control'}),
            "last_name": forms.TextInput(attrs={'class':'form-control'}),
            "roll_no": forms.TextInput(attrs={'class':'form-control'}),
            "password": forms.TextInput(attrs={'class':'form-control','type':'password'}),
        }
        labels = {}
        help_texts = {}
        error_messages = {}
