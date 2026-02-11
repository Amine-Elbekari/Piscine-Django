from django.shortcuts import render
# from django.views import generic
from .models import  People

# Create your views here.

def display_data(request):

    people = People.objects.filter(
        homeworld__climate__icontains='windy'
    ).order_by('name')
    if not people.exists():
        return render(request, 'ex09/display.html', {
            "error_message": "No data available, please use the following command line before use:",
            "command": "python import_data_ex09.py"
        })

    return render(request, 'ex09/display.html', {'people': people})

