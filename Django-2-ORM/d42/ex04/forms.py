from django import forms

class DropDown(forms.Form):
    films_titles = forms.CharField(label='Films Titles', max_length=64)
    def clean_films_titles(self):
        data = self.cleaned_data.get('films_titles')
        if not data:
            raise forms.ValidationError('No data provided')
                
        return data