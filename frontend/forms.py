from django import forms
from django.contrib.auth.models import User
from django.forms import widgets

class UserReqisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username', 'email', 'password'
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}), 
            'last_name': forms.TextInput(attrs={'class': 'form-control'}), 
            'username': forms.TextInput(attrs={'class': 'form-control'}), 
            'email': forms.EmailInput(attrs={'class': 'form-control'}), 
            'password': forms.PasswordInput(attrs={'class': 'form-control'})
        }