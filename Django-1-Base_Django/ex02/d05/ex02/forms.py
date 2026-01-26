from django import forms

class UserForm(forms.Form):
    text_field = forms.CharField(label='Your name', max_length=50)
    
    def clean_text_field(self):
        data = self.cleaned_data.get('text_field')
        if data is None:
            return
        if not data.isalpha():
            raise ValidationError('Invalid Text Field, Your Name contain only lower or upercase Charaters')
        return data
    