from django.contrib.auth.forms import AuthenticationForm


class StyledAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control form-control-sm',
            'placeholder': 'username',
            'autofocus': True,
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control form-control-sm',
            'placeholder': 'password',
        })

def login_form(request):
    return {'login_form': StyledAuthenticationForm()}

