from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
from psycopg2 import sql, connect
from django.conf import settings
# Create your views here.

def init(request):

    try:
        db_conf = settings.DATABASES['default']
        
        conn = connect(
            dbname=db_conf['NAME'],
            user=db_conf['USER'],
            password=db_conf['PASSWORD'],
            host=db_conf['HOST'],
            port=db_conf['PORT']
        )
        # create the cursor
        cursor = conn.cursor()
        
        query = """
            CREATE TABLE IF NOT EXISTS ex00_movies (
                title VARCHAR(64) UNIQUE NOT NULL,
                episode_nb INTEGER PRIMARY KEY CHECK (episode_nb > 0),
                opening_crawl TEXT,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL
            );
        """
        
        # COMMIT and CLOSE are Critical here if you forget them everything will crash
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
        return HttpResponse('OK')
        
    except Exception as e:
        return HttpResponse(f'Error: {e}')
    
    # try:
        
    #     query = sql.SQL("""
    #         CREATE TABLE IF NOT EXISTS ex00_movies (
    #             title VARCHAR(64) UNIQUE NOT NULL,
    #             episode_nb INTEGER PRIMARY KEY CHECK (episode_nb > 0),
    #             opening_crawl TEXT,
    #             director VARCHAR(32) NOT NULL,
    #             producer VARCHAR(128) NOT NULL,
    #             release_date DATE NOT NULL
    #         );
    #     """)
    #     with connection.cursor() as cursor:
    #         cursor.execute(query)
    #     return HttpResponse("OK")
    # except Exception as e:
    #         return HttpResponse(f"Error: {e}")
        
    