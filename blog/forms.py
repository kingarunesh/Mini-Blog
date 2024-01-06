from django import forms

from blog.models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "description"]
        
        widgets = {
            "title": forms.TextInput(attrs={"class": "add-blog--title"}) ,
            "description": forms.Textarea(attrs={"class": "add-blog--description"})
        }