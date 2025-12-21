from bs4 import BeautifulSoup
import requests
import sys
# Custom Search API: AIzaSyBZTd2YgNQHAkk_FPXnOELdKtdvnhjIYPM

#for speed we can use lxml parser rather then html.parser
# lxml parser library use C functionalities

# soup = BeautifulSoup('<b class="boldest"><p>Extremely bold</p></b>Insert P here', 'html.parser')
# tag = soup.b
# # print(tag)
# del tag['class']
# # print(tag)
# tag.string.replace_with('No longer bold')
# # print(soup.string)

# p_tag = BeautifulSoup('<p>Just head text here</p>', 'html.parser')
# soup.find(string="Insert P here").replace_with(p_tag)

# print(soup.find_all('p'))
# print(tag.contents[0].name)

if len(sys.argv) == 2:
    HEADERS = {
        'User-Agent': 'ROADSTOPHILO/1.0 (contact: amine.elbekari13@gmail.com)'
    }
    content_to_search = sys.argv[1]
    URL = f"https://en.wikipedia.org/wiki/{content_to_search}"
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")
    p = soup.find_all('p')
    start = 0

    # print(a)