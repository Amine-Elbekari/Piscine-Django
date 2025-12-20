import requests
import json
from dewiki import from_string
import sys

def wiki_search():

    if len(sys.argv) == 2:
            content_to_search = sys.argv[1]
            s = requests.Session()
            HEADERS = {
                 'User-Agent': 'MyWikiRequestScript/1.0 (contact: amine.elbekari13@gmail.com)'
            }
            URL = 'https://en.wikipedia.org/w/api.php'
            PARAMS = {
                 "action": "query",
                 "format": "json",
                 "prop": "revisions",
                 "rvprop": "content",
                 "rvslots": "main",
                 "titles": content_to_search,
                 "redirects": 1
            }
            response = s.get(url=URL, params=PARAMS, headers=HEADERS)
            data = response.json()
            page = next(iter(data['query']['pages'].values()))
            # for k, v in data.items():
            content = page['revisions'][0]['slots']['main']['*']
            clean_content = from_string(content)
            filename = f'{content_to_search}.wiki'
            with open(filename, 'w', encoding='utf-8') as f:
                 f.write(clean_content)
            with open('file.json', 'w') as f:
                 json.dump(data, f, indent=4)
            print(clean_content[:1000])


    else:
        raise Exception('Usage: <file_name.py> "content_to_search"')

if __name__ == "__main__":
    try:
        wiki_search()
    except Exception as e:
        print(e)