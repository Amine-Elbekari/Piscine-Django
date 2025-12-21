import requests
import json
from dewiki import from_string
import sys

def clean_content(content):

     while '{{' in content:
          start = content.find('{{')
          end = content.find('}}', start)
          if start == -1:
               break
          if end != -1:
               content = content[:start] + content[end + 2:]
          else:
               break
     content = content.replace('}}', '')

     while '<ref' in content:
          start = content.find('<ref')
          end = content.find('</ref>', start)
          if end != -1:
               content = content[:start] + content[end + 6:]
          else:
               tag_end = content.find('>', start)
               if tag_end != -1:
                    content = content[:start] + content[tag_end + 1:]
               else:
                    break
     content = content.replace('</ref>', '').replace('</ref>', '')

     while '{|' in content:
          start = content.find('{|')
          end = content.find('|}', start)
          if end != -1:
               content = content[:start] + content[end + 2:]
          else:
               break
     while '<' in content:
          start = content.find('<')
          if start == -1:
               break
          end = content.find('>', start)
          if end != -1:
               content = content[:start] + content[end + 1:]
          else:
               break
     content = content.replace('(', '')
     content = content.replace(')', '')
     return content

def wiki_search():

    suggestion = False
    if len(sys.argv) == 2:
          content_to_search = sys.argv[1]
          s = requests.Session()
          HEADERS = {
               'User-Agent': 'MyWikiRequestScript/1.0 (contact: amine.elbekari13@gmail.com)'
          }
          URL = 'https://fr.wikipedia.org/w/api.php'
          PARAMS_TO_SEARCH = {
               "action": "query",
               "format": "json",
               "list": "search",
               "srsearch": content_to_search,
               "srlimit": 1
          }
          response = s.get(url=URL, params=PARAMS_TO_SEARCH, headers=HEADERS).json()
          
          with open('file_search.json', 'w') as f:
               json.dump(response, f, indent=4)

          if 'query' in response and 'search' in response['query'] and len(response['query']['search']) > 0: 
               current_title = response['query']['search'][0]['title']
          elif 'searchinfo' in response['query'] and 'suggestion' in response['query']['searchinfo']:
               current_title = response['query']['searchinfo']['suggestion']
          else:
               raise Exception('Error: no results found!')
          
          PARAMS = {
               "action": "parse",
               "format": "json",
               "page": current_title,
               "prop": "wikitext",
               "redirects": 1
          }
          response_content = requests.get(url=URL, params=PARAMS, headers=HEADERS).json()
          if 'error' in response_content:
              raise Exception(f'Error: {response_content['error']['info']}')
          raw_wiki_text = response_content['parse']['wikitext']['*']
          content = from_string(raw_wiki_text)
          content_cleaned = clean_content(content)
    
          with open('file_content.json', 'w') as f:
               json.dump(response_content, f, indent=4)
          to_search = sys.argv[1].replace(' ', '_')
          with open(f'{to_search}.wiki', 'w', encoding='utf-8') as outfile:
              outfile.write(content_cleaned)

    else:
        raise Exception('Usage: <file_name.py> "content_to_search"')

if __name__ == "__main__":
    try:
        wiki_search()
    except Exception as e:
        print(e)