from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django.conf import settings
import psycopg2
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "d42.settings")
# Create your views here.

def init(request):

    try:
        
        query_planets = psycopg2.sql.SQL("""
            CREATE TABLE IF NOT EXISTS ex08_planets (
                id SERIAL PRIMARY KEY,
                name VARCHAR(64) UNIQUE NOT NULL,
                climate TEXT,
                diameter INT,
                orbital_period INT,
                population BIGINT,
                rotation_period INT,
                surface_water FLOAT,
                terrain VARCHAR(128)
            );
        """)
        query_people = psycopg2.sql.SQL("""
            CREATE TABLE IF NOT EXISTS ex08_people (
                id SERIAL PRIMARY KEY,
                name VARCHAR(64) UNIQUE NOT NULL,
                birth_year VARCHAR(32),
                gender VARCHAR(32),
                eye_color VARCHAR(32),
                hair_color VARCHAR(32),
                height INT,
                mass FLOAT,
                homeworld VARCHAR(64), FOREIGN KEY(homeworld) REFERENCES ex08_planets(name)
            );
        
        
        """)
        with connection.cursor() as cursor:
            cursor.execute(query_planets)
            cursor.execute(query_people)
        return HttpResponse("OK")
    except Exception as e:
            return HttpResponse(f"{e} ->No data available")


def populate(request):
    
    success_message = []
    try:
        db = settings.DATABASES['default']
        conn = psycopg2.connect(
            dbname=db['NAME'],
            user=db['USER'],
            password=db['PASSWORD'],
            host=db['HOST'],
            port=db['PORT']
        )
        curs = conn.cursor()
        with open('./planets.csv') as data_f:
            curs.copy_from(data_f, 'ex08_planets', sep='\t', columns=('name', 'climate','diameter','orbital_period','population','rotation_period','surface_water','terrain'), null='NULL')
            success_message.append("OK")
        with open('./people.csv') as data_f:
            curs.copy_from(data_f, 'ex08_people', sep='\t', columns=('name','birth_year', 'gender','eye_color','hair_color','height','mass','homeworld'), null='NULL')
            success_message.append("OK")
        conn.commit()
        curs.close()
        conn.close()
       
        return HttpResponse(f"{"<br>".join(success_message)}")
    except psycopg2.Error as e:
        return HttpResponse(f'Error: {e}')

def display(request):
    
    try:
        query = psycopg2.sql.SQL("""
                SELECT ex08_people.name, ex08_people.homeworld, ex08_planets.climate
                FROM ex08_people
                INNER JOIN ex08_planets
                    ON ex08_people.homeworld = ex08_planets.name
                ORDER BY ex08_people.name;
        """)
        with connection.cursor() as cursor:
            cursor.execute(query)
            names = cursor.fetchall()
        return render(request, 'ex08/display.html', {'names': names})
        
    except Exception as e:
        return HttpResponse(f'No data available -> : {e}')
