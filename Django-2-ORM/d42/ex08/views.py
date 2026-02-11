from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django.conf import settings
import psycopg2

# Create your views here.

def init(request):

    try:
        
        query_planets = psycopg2.sql.SQL("""
            CREATE TABLE IF NOT EXISTS ex08_planets (
                name VARCHAR(64) PRIMARY KEY,
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
                name VARCHAR(64) PRIMARY KEY,
                birth_year VARCHAR(32),
                gender VARCHAR(32),
                eye_color VARCHAR(32),
                hair_color VARCHAR(32),
                height INT,
                mass FLOAT,
                homeworld VARCHAR(64),
                FOREIGN KEY(homeworld) REFERENCES ex08_planets(name)
            );
        """)
        with connection.cursor() as cursor:
            cursor.execute(query_planets)
            cursor.execute(query_people)
        return HttpResponse("OK")
    except Exception as e:
            return HttpResponse(f"Error: {e}")


def populate(request):
    results = []

    try:
        planets_path = settings.BASE_DIR / 'planets.csv'
        people_path = settings.BASE_DIR / 'people.csv'

        with connection.cursor() as cursor:
            raw_conn = cursor.connection

            # Load planets first (people has FK to planets)
            try:
                with open(planets_path, 'r') as f:
                    cursor.copy_from(
                        f,
                        'ex08_planets',
                        columns=('name', 'climate', 'diameter', 'orbital_period',
                                 'population', 'rotation_period', 'surface_water',
                                 'terrain'),
                        null='NULL',
                    )
                results.append("OK")
            except Exception as e:
                raw_conn.rollback()
                results.append(f"Error: {e}")

            # Load people
            try:
                with open(people_path, 'r') as f:
                    cursor.copy_from(
                        f,
                        'ex08_people',
                        columns=('name', 'birth_year', 'gender', 'eye_color',
                                 'hair_color', 'height', 'mass', 'homeworld'),
                        null='NULL',
                    )
                results.append("OK")
            except Exception as e:
                raw_conn.rollback()
                results.append(f"Error: {e}")

        return HttpResponse("<br>".join(results))
    except Exception as e:
        return HttpResponse(f"Error: {e}")

def display(request):
    
    try:
        query = psycopg2.sql.SQL("""
                SELECT ex08_people.name, ex08_people.homeworld, ex08_planets.climate
                FROM ex08_people
                INNER JOIN ex08_planets
                    ON ex08_people.homeworld = ex08_planets.name
                WHERE ex08_planets.climate ILIKE '%windy%'
                ORDER BY ex08_people.name;
        """)
        with connection.cursor() as cursor:
            cursor.execute(query)
            names = cursor.fetchall()
        if not names:
            return HttpResponse('No data available')
        return render(request, 'ex08/display.html', {'names': names})
        
    except Exception as e:
        return HttpResponse('No data available')
