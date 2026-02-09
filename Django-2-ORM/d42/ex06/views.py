from django.shortcuts import render, redirect
from django.db import connection
from django.http import HttpResponse, HttpResponseRedirect
from psycopg2 import sql, connect
from django.conf import settings
from .forms import DropDown, OpeningCrawl
import psycopg2

# Create your views here.

def init(request):

    try:
        
        query = sql.SQL("""
            CREATE TABLE IF NOT EXISTS ex06_movies (
                title VARCHAR(64) UNIQUE NOT NULL,
                episode_nb INTEGER PRIMARY KEY CHECK (episode_nb > 0),
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                opening_crawl TEXT,
                release_date DATE NOT NULL,
                created TIMESTAMP DEFAULT NOW(),
                updated TIMESTAMP DEFAULT NOW()
            );
        """)
        query_function = sql.SQL("""
        CREATE OR REPLACE FUNCTION update_changetimestamp_column()
        RETURNS TRIGGER AS $$
        BEGIN
            NEW.updated = now();
            NEW.created = OLD.created;
            RETURN NEW;
        END;
        $$ language 'plpgsql';
    """)
        query_drop_trigger = sql.SQL("""
            DROP TRIGGER IF EXISTS update_films_changetimestamp ON ex06_movies;     
    """)
        query_create_trigger = sql.SQL("""
            CREATE TRIGGER update_films_changetimestamp
            BEFORE UPDATE ON ex06_movies
            FOR EACH ROW
            EXECUTE PROCEDURE update_changetimestamp_column();
        """)
        with connection.cursor() as cursor:
            cursor.execute(query)
            cursor.execute(query_function)
            cursor.execute(query_drop_trigger)
            cursor.execute(query_create_trigger)
        return HttpResponse("OK")
    except Exception:
            return HttpResponse("No data available")
        

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
            INSERT INTO ex06_movies (episode_nb, title, director, producer, release_date)
            VALUES (%s, %s, %s, %s, %s);
        """
        with connection.cursor() as cursor:
            
            for movie in movies:
                episode_nb = movie[0]
                
                cursor.execute("SELECT episode_nb FROM ex06_movies WHERE episode_nb = %s;", [episode_nb])
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
            SELECT episode_nb, title, director, producer, release_date, opening_crawl, created, updated
            FROM ex06_movies
            ORDER BY episode_nb;
        """)
        with connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
        return render(request, 'ex06/display.html', {'results': results})
        
    except Exception as e:
        return HttpResponse(f'No data available')

def update(request):
    choices = []
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT title from ex06_movies ORDER BY title;")
            choices = [row[0] for row in cursor.fetchall()]
    except psycopg2.Error as e:
        print(f"Database Error: {e}")
    
    if request.method == 'POST':
        form = DropDown(request.POST)
        form_opening_crawl = OpeningCrawl(request.POST)
        if form.is_valid() and form_opening_crawl.is_valid():
            title = form.cleaned_data['films_titles']
            opening_crawl = form_opening_crawl.cleaned_data['opening_crawl']
            
            try:
                with connection.cursor() as cursor:
                    cursor.execute("UPDATE ex06_movies SET opening_crawl = %s WHERE title = %s ;", [opening_crawl, title])
            except psycopg2.Error as e:
                return HttpResponse("No data available")
        return HttpResponseRedirect('/ex06/update')
    else:
        form = DropDown()
        form_opening_crawl = OpeningCrawl()
    return render(request, 'ex06/update.html', {
        'form': form,
        'choices': choices,
    })