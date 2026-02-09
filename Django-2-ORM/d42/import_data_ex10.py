import json
import os
import django
import sys

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "d42.settings")
django.setup()

from ex10.models import People, Planets, Movies

def parse_data():
    file_path = './ex10_initial_data.json'
    
    if not os.path.exists(file_path):
        print("File not found.")
        return

    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

    for item in data:
        model_name = item.get('model')
        fields = item.get('fields')
        item_pk = item.get('pk')

        # --- PLANETS ---
        if model_name == 'ex10.planets':
            # Check if THIS specific planet exists
            if Planets.objects.filter(pk=item_pk).exists():
                print(f"Planet {fields['name']} already exists. Skipping.")
            else:
                Planets.objects.create(
                    pk=item_pk,
                    name=fields['name'],
                    climate=fields['climate'],
                    diameter=fields['diameter'],
                    orbital_period=fields['orbital_period'],
                    population=fields['population'],
                    rotation_period=fields['rotation_period'],
                    surface_water=fields['surface_water'],
                    terrain=fields['terrain'],
                    # created/updated handled by auto_now_add
                )
                print(f"CREATED Planet: {fields['name']}")

        # --- PEOPLE ---
        elif model_name == 'ex10.people':
            if People.objects.filter(pk=item_pk).exists():
                print(f"Person {fields['name']} already exists. Skipping.")
            else:
                # Handle Foreign Key for Homeworld
                homeworld_id = fields.get('homeworld')
                planet_obj = None
                
                if homeworld_id:
                    try:
                        planet_obj = Planets.objects.get(pk=homeworld_id)
                    except Planets.DoesNotExist:
                        print(f"  Warning: Planet ID {homeworld_id} not found for {fields['name']}")

                People.objects.create(
                    pk=item_pk,
                    name=fields['name'],
                    birth_year=fields['birth_year'],
                    gender=fields['gender'],
                    eye_color=fields['eye_color'],
                    hair_color=fields['hair_color'],
                    height=fields['height'],
                    mass=fields['mass'],
                    homeworld=planet_obj
                )
                print(f"CREATED Person: {fields['name']}")

        # --- MOVIES ---
        elif model_name == 'ex10.movies':
            if Movies.objects.filter(pk=item_pk).exists():
                print(f"Movie {fields['title']} already exists. Skipping.")
            else:
                movie = Movies.objects.create(
                    pk=item_pk,
                    title=fields['title'],
                    opening_crawl=fields['opening_crawl'],
                    director=fields['director'],
                    producer=fields['producer'],
                    release_date=fields['release_date']
                )

                # Many to Many Relationships
                char_ids = fields.get('characters', [])
                for char_id in char_ids:
                    try:
                        person = People.objects.get(pk=char_id)
                        movie.characters.add(person)
                    except People.DoesNotExist:
                        print(f"  Warning: Person ID {char_id} not found for movie {fields['title']}")
                
                print(f"CREATED Movie: {fields['title']}")

if __name__ == "__main__":
    parse_data()