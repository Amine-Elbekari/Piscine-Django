from django import forms

class MoviesTitles(forms.Form):
    titles_lists = forms.ChoiceField(choices=(), required=True)

class OpeningCrawl(forms.Form):
    opening_crawl = forms.CharField(label='Opening Crawl')
    def clean_opening_crawl(self):
        data = self.cleaned_data.get('opening_crawl')
        if not data:
            raise forms.ValidationError('No data provided')
        return data