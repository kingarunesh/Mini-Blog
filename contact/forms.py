from django import forms

from contact.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["first_name", "last_name", "email", "phone", "subject", "message"]
        
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email Address",
        }
        
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "c_first_name"}),
            "flast_name": forms.TextInput(attrs={"class": "c_flast_name"}),
            "email": forms.EmailInput(attrs={"class": "c_email"}),
            "phone": forms.TextInput(attrs={"class": "c_phone"}),
            "subject": forms.TextInput(attrs={"class": "c_subject"}),
            "message": forms.Textarea(attrs={"class": "c_message"}),
        }