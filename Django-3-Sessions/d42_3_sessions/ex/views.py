from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import CreateView
from django.urls import reverse_lazy
import time
import random
# Create your views here.

def anonym_users(request):

    saved_time = time.time()
    users = settings.ANYONYM_USERS
    if not request.session.get('random_user'):
        random_user = random.choice(users)
        request.session['random_user'] = random_user
        request.session['timestamp'] = saved_time
    else:
        current_time = time.time()
        time_saved = request.session.get('timestamp')
        if current_time - time_saved >= 42:
            random_user = random.choice(users)
            request.session['random_user'] = random_user
            request.session['timestamp'] = current_time
        if current_time - time_saved <= 42:
            pass
    setted_name = request.session.get('random_user')

    return render(request, 'ex/display.html', {'setted_name': setted_name})

class Registration(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("anonym_users")
    template_name = "registration/signup.html"
