import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "d42.settings")
django.setup()

#opening_crawl
from ex07.models import Movies

def parse_data():
    
    file_path = './opening_crawl.json'

    # print(episodes_nb)
    if os.path.isfile(file_path):
        if os.path.getsize(file_path):
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                for k,v in data.items():
                    Movies.objects.filter(title=k).update(opening_crawl=v)

if __name__ == "__main__":
    parse_data()