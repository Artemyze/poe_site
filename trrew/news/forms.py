from django import forms
from .models import News


class AddNewForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            'title',
            'text',
            'is_published',
            'image',
            'category'
        ]
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'text': forms.Textarea(attrs={"class": "form-control"}),
            'category': forms.Select(attrs={"class": "form-control"})
        }


