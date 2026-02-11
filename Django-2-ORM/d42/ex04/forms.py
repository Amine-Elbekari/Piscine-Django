from django import forms

class DropDown(forms.Form):
    films_titles = forms.ChoiceField(label='Films Titles')

    def __init__(self, choices, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['films_titles'].choices = [(title, title) for title in choices]