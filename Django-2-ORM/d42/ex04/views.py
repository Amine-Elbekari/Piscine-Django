from django.shortcuts import render, redirect
from django.db import connection
from django.http import HttpResponse, HttpResponseRedirect
from psycopg2 import sql, connect
from django.conf import settings
from .forms import DropDown
import psycopg2

# Create your views here.

def init(request):

    try:
        
        query = sql.SQL("""
            CREATE TABLE IF NOT EXISTS ex04_movies (
                title VARCHAR(64) UNIQUE NOT NULL,
                episode_nb INTEGER PRIMARY KEY CHECK (episode_nb > 0),
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL
            );
        """)
        with connection.cursor() as cursor:
            cursor.execute(query)
        return HttpResponse("OK")
    except Exception as e:
            return HttpResponse(f"Error: {e}")
        

def populate(request):
    
    movies = [
        (1, 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19'),
        (2, 'Attack of the Clones', 'George Lucas', 'Rick McCallum', '2002-05-16'),
        (3, 'Revenge of the Sith', 'George Lucas', 'Rick McCallum', '2005-05-19'),
        (4, 'A New Hope' , 'George Lucas, Gary Kurtz', 'Rick McCallum', '1977-05-25'),
        (5, 'The Empire Strikes Back', 'Irvin Kershner', 'Gary Kurtz, Rick McCallum', '1980-05-17'),
        (6, 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25'),
        (7, 'The Force Awakens', 'J. J. Abrams, Kathleen Kennedy', 'J. J. Abrams, Bryan Burk', '2015-12-11'),
    ]
    result_msg = []
    
    try:
        query = """
            INSERT INTO ex04_movies (episode_nb, title, director, producer, release_date)
            VALUES (%s, %s, %s, %s, %s);
        """
        with connection.cursor() as cursor:
            
            for movie in movies:
                episode_nb = movie[0]
                
                cursor.execute("SELECT episode_nb FROM ex04_movies WHERE episode_nb = %s;", [episode_nb])
                already_exist = cursor.fetchone()
                
                if not already_exist:
                    cursor.execute(query, movie)
                    result_msg.append("OK")
    except Exception as e:
        return HttpResponse(f"Error: {e}")
    if result_msg:
        return HttpResponse("<br>".join(result_msg))
    else:
        return HttpResponse("No data available")

def display(request):
    
    try:
        query = sql.SQL("""
            SELECT episode_nb, title, director, producer, release_date
            FROM ex04_movies;
        """)
        with connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
        return render(request, 'ex04/display.html', {'results': results})
        
    except Exception as e:
        return HttpResponse(f'No data available')

def remove(request):
    choices = []
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT title from ex04_movies ORDER BY title;")
            choices = [row[0] for row in cursor.fetchall()]
    except psycopg2.Error as e:
        print(f"Database Error: {e}")
    
    if request.method == 'POST':
        form = DropDown(request.POST)
        if form.is_valid():
            title_to_remove = form.cleaned_data['films_titles']
            try:
                with connection.cursor() as cursor:
                    cursor.execute("DELETE FROM ex04_movies WHERE title = %s;", [title_to_remove])
            except psycopg2.Error as e:
                return HttpResponse("No data available")
        return HttpResponseRedirect('/ex04/remove')
    else:
        form = DropDown()
    return render(request, 'ex04/remove.html', {
        'form': form,
        'choices': choices,
    })