from django import forms
from django.contrib.auth.models import User
from .models import Reply

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['author', 'content']

        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }