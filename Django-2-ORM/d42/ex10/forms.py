from django import forms

class MoviesMinReleaseDate(forms.Form):
    min_date = forms.DateField(
        input_formats=["%Y-%m-%d"],
        widget=forms.DateInput(format="%Y-%m-%d", attrs={'type': 'date'})
    )

class MoviesMaxReleaseDate(forms.Form):
    max_date = forms.DateField(
        input_formats=["%Y-%m-%d"],
        widget=forms.DateInput(format="%Y-%m-%d", attrs={'type': 'date'})
    )

class PlanetDiameterGreaterThen(forms.Form):
    planet_diameter = forms.IntegerField()

class CharacterGender(forms.Form):
    gender = forms.ChoiceField(choices=(), required=True)