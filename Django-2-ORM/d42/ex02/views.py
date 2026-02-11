from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
from psycopg2 import sql, connect
from django.conf import settings
# Create your views here.

def init(request):

    # try:
    #     db_conf = settings.DATABASES['default']
        
    #     conn = connect(
    #         dbname=db_conf['NAME'],
    #         user=db_conf['USER'],
    #         password=db_conf['PASSWORD'],
    #         host=db_conf['HOST'],
    #         port=db_conf['PORT']
    #     )
    #     # create the cursor
    #     cursor = conn.cursor()
        
    #     query = """
    #         CREATE TABLE IF NOT EXISTS ex00_movies (
    #             title VARCHAR(64) UNIQUE NOT NULL,
    #             episode_nb INTEGER PRIMARY KEY CHECK (episode_nb > 0),
    #             opening_crawl TEXT,
    #             director VARCHAR(32) NOT NULL,
    #             producer VARCHAR(128) NOT NULL,
    #             release_date DATE NOT NULL
    #         );
    #     """
        
    #     # COMMIT and CLOSE are Critical here if you forget them everything will crash
    #     cursor.execute(query)
    #     conn.commit()
    #     cursor.close()
    #     conn.close()
    #     return HttpResponse('OK')
        
    # except Exception as e:
    #     return HttpResponse(f'Error: {e}')
    
    try:
        
        query = sql.SQL("""
            CREATE TABLE IF NOT EXISTS ex02_movies (
                title VARCHAR(64) UNIQUE NOT NULL,
                episode_nb INTEGER PRIMARY KEY,
                opening_crawl TEXT,
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
        (4, 'A New Hope', 'George Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25'),
        (5, 'The Empire Strikes Back', 'Irvin Kershner', 'Gary Kurtz, Rick McCallum', '1980-05-17'),
        (6, 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25'),
        (7, 'The Force Awakens', 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', '2015-12-11'),
    ]
    results = []
    for movie in movies:
        try:
            query = sql.SQL("""
                INSERT INTO ex02_movies (episode_nb, title, director, producer, release_date)
                VALUES (%s, %s, %s, %s, %s);
            """)
            with connection.cursor() as cursor:
                cursor.execute(query, movie)
            results.append("OK")
        except Exception as e:
            results.append(f"Error: {e}")
    return HttpResponse("<br>".join(results))

def display(request):
    
    try:
        query = sql.SQL("""
            SELECT episode_nb, title, opening_crawl, director, producer, release_date
            FROM ex02_movies;
        """)
        with connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
        return render(request, 'ex02/display.html', {'results': results})
        
    except Exception as e:
        return HttpResponse(f'No data available')