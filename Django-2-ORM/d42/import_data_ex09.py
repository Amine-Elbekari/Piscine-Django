import json
import os
import django

    
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "d42.settings")
django.setup()
    
from ex09.models import People, Planets

def parse_data():
    
    file_path = './ex09_initial_data.json'
    if os.path.isfile(file_path):
        if os.path.getsize(file_path):
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                for item in data:
                   
                    model_name = item.get('model')
                    fields = item.get('fields')
                    item_pk = item.get('pk')
                    if model_name == 'ex09.planets':
                        # Rather creating an instance then save it after using .save() method
                        # i can use .create method it will instantiates the object the saves it!
                        Planets.objects.create(
                            pk = item_pk,
                            name = fields['name'],
                            climate = fields['climate'],
                            diameter = fields['diameter'],
                            orbital_period = fields['orbital_period'],
                            population = fields['population'],
                            rotation_period = fields['rotation_period'],
                            surface_water = fields['surface_water'],
                            terrain = fields['terrain'],
                            created = fields['created'],
                            updated = fields['updated']
                        )
                        print(f'DEBUG: the Planet {fields['name']} is created')
                    elif model_name == 'ex09.people':
                        
                        homeworld_id = fields['homeworld']
                        planet = None
                        if fields['homeworld'] is not None:
                            try:
                                planet = Planets.objects.get(pk=homeworld_id)
                            except Planets.DoesNotExist:
                                print(f'Planet {homeworld_id} not found for {fields['name']}')
                                planet = None
                            
                        People.objects.create(
                            pk=item_pk,
                            name = fields['name'],
                            birth_year = fields['birth_year'],
                            gender = fields['gender'],
                            eye_color = fields['eye_color'],
                            hair_color = fields['hair_color'],
                            height = fields['height'],
                            mass = fields['mass'],
                            homeworld= planet,
                            created = fields['created'],
                            updated = fields['updated']
                        )
                        print(f'DEBUG: People {fields['name']} is created')
                        
if __name__ == "__main__":
    parse_data()