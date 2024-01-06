from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm



class SignUpForm(UserCreationForm):
    #ERROR :        change later - error message
    password2 = forms.CharField(label="Confirm Password")
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
        
        widgets = {
            "username": forms.TextInput(attrs={"class": "signup__username"}),
            "first_name": forms.TextInput(attrs={"class": "signup__first_name"}),
            "last_name": forms.TextInput(attrs={"class": "signup__last_name"}),
            "email": forms.EmailInput(attrs={"class": "signup__email"}),
        }



class EditProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]