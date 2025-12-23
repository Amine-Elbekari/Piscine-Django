from bs4 import BeautifulSoup

html_doc = """
<html>
<head>
    <title>The Dormouse's story</title>
</head>
<body>
    <p>Hello World</p>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Access the <title> tag
title_tag = soup.title
# print(f"The title tag: {title_tag}")

parent_of_title = title_tag.parent.name
print(parent_of_title)
