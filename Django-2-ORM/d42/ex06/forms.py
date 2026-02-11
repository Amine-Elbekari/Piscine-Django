from django import forms

class DropDown(forms.Form):
    films_titles = forms.ChoiceField(label='Films Titles')

    def __init__(self, choices, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['films_titles'].choices = [(title, title) for title in choices]

class OpeningCrawl(forms.Form):
    opening_crawl = forms.CharField(label='Opening Crawl')
    def clean_opening_crawl(self):
        
        data = self.cleaned_data.get('opening_crawl')
        if not data:
            raise forms.ValidationError('No data provided')
        return data