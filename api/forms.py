from django import forms
from django.contrib.auth import models
from django.contrib.auth.models import User
from django.forms import fields


class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']