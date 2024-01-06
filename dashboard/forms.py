from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
        
        widgets = {
            "username": forms.TextInput(attrs={"class": "signup__username"}),
            "first_name": forms.TextInput(attrs={"class": "signup__first_name"}),
            "last_name": forms.TextInput(attrs={"class": "signup__last_name"}),
            "email": forms.EmailInput(attrs={"class": "signup__email"}),
        }