from django import forms
from .models import Article, UserFavouriteArticle

class PublicationForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = ['title', 'synopsis', 'content']

class AddFavoriteForm(forms.ModelForm):

    class Meta:
        model = UserFavouriteArticle
        fields = []