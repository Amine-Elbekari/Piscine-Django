from django import forms
from .models import Article

class PublicationForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = ['title', 'synopsis', 'content']
