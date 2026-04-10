from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import MyCustomUser, ModelTip

class MyUserForm(UserCreationForm):
    
    class Meta:
        model = MyCustomUser
        fields = ('username',)
        
        # Lolo@123
class TipForm(ModelForm):
    
    class Meta:
        model = ModelTip
        # exclude = ["author", "date"]
        fields = ["content"]
        
    