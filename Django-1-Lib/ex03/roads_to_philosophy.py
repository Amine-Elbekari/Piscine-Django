from bs4 import BeautifulSoup, Tag
import requests
import sys

def check_valid_anchor(p_tag):
    open_parenth = 0
    open_brackets = 0
    anchor = None

    for node in p_tag.descendants:

        # if '(' in node:
        #     open_parenth += 1
        # if ')' in node:
        #     open_parenth -= 1
        if isinstance(node, str):
            open_parenth += node.count('(')
            open_parenth -= node.count(')')
            open_brackets += node.count('[')
            open_brackets -= node.count(']')
        if open_parenth > 0 or open_brackets > 0:
            continue

        if isinstance(node, Tag) and node.name == 'a':
            href = node.get('href')
            if not href or not href.startswith('/wiki/') or ':' in href:
                continue
            anchor = node
            break
    # print(f'\n{anchor}\n')
    return anchor

def road_to_philo():
    if len(sys.argv) == 2:
        HEADERS = {
            'User-Agent': 'ROADSTOPHILO/1.0 (contact: amine.elbekari13@gmail.com)'
        }
        content_to_search = f'/wiki/{sys.argv[1]}'

        is_already_visited = [content_to_search]
        is_error = False
        is_invalid_link = False
        counter = 0
        while True:

            URL = f"https://en.wikipedia.org{content_to_search}"
            try:
                response = requests.get(URL, headers=HEADERS)
                response.raise_for_status()
            except requests.exceptions.RequestException:
                is_invalid_link = True
                raise Exception(' It leads to a dead end !')
            if is_invalid_link:
                break
            
            soup = BeautifulSoup(response.text, "html.parser")
            title = soup.h1.get_text()
            # 
            print(title)
            counter += 1
            if title.lower() == 'philosophy':
                break

            p = soup.find_all('p')
            anchor_found = False
            for elem in p:
                
                if elem.find_parent('table'):
                    continue
                valid_anchor = check_valid_anchor(elem)
                if valid_anchor:
                    content_to_search = valid_anchor['href']
                    if content_to_search in is_already_visited:
                        is_error = True
                        raise Exception('It leads to an infinite loop!')
                    is_already_visited.append(content_to_search)
                    anchor_found = True
                if anchor_found:
                    break
            if is_error:
                break

        print(f'{counter} roads from {sys.argv[1]} to philosophy !')

if __name__ == "__main__":
    try:
        road_to_philo()
    except Exception as e:
        print(e)