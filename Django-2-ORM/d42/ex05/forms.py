from django import forms

class MoviesTitles(forms.Form):
    titles_lists = forms.ChoiceField(choices=(), required=True)
    