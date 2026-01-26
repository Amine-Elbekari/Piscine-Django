from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import UserForm
import datetime
import os
import logging
# Create your views here.

def get_user_name(request):
    
    LOG_FILE = os.path.join(settings.BASE_DIR, 'ex02', 'logs.txt')
    
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            text_field = form.cleaned_data['text_field']
   
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            try:
                with open(LOG_FILE, 'a') as f:
                    f.write(f'{timestamp} - {text_field}\n')
            except Exception as e:
                print(f'Error writing log file: {e}')
            return HttpResponseRedirect(request.path)
    else:
        form = UserForm()
    history = []
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, 'r') as f:
                history = [line.strip() for line in f.readlines()]
        except Exception as e:
            print (f'Error reading log file: {e}')
    context = {
        'form': form,
        'history': history
    }
    return render(request, 'ex02/ex02-form.html', context)
