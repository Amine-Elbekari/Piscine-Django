from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies

# Create your views here.

def populate(request):
    
    try:
        movies_list = [
            Movies(episode_nb=1, title='The Phantom Menace', director='George Lucas', producer='Rick McCallum', release_date='1999-05-19'),
            Movies(episode_nb=2, title='Attack of the Clones', director='George Lucas', producer='Rick McCallum', release_date='2002-05-16'),
            Movies(episode_nb=3, title='Revenge of the Sith', director='George Lucas', producer='Rick McCallum', release_date='2005-05-19'),
            Movies(episode_nb=4, title='A New Hope' , director='George Lucas, Gary Kurtz', producer='Rick McCallum', release_date='1977-05-25'),
            Movies(episode_nb=5, title='The Empire Strikes Back', director='Irvin Kershner', producer='Gary Kurtz, Rick McCallum', release_date='1980-05-17'),
            Movies(episode_nb=6, title='Return of the Jedi', director='Richard Marquand', producer='Howard G. Kazanjian, George Lucas, Rick McCallum', release_date='1983-05-25'),
            Movies(episode_nb=7, title='The Force Awakens', director='J. J. Abrams, Kathleen Kennedy', producer='J. J. Abrams, Bryan Burk', release_date='2015-12-11')
        ]
        Movies.objects.bulk_create(movies_list)
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {e}")

def display(request):
    
    results = Movies.objects.all()
    if not results.exists():
        return HttpResponse("No data available")
    return render(request, 'ex03/display.html', {'results': results})        