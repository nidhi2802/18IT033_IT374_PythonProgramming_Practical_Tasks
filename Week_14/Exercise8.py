import requests
from bs4 import BeautifulSoup

base_url = 'https://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

for story_heading in soup.find_all(class_="css-8atqhb"):
    if story_heading.a:
        print(story_heading.a.text.replace("\n", " ").strip())
    else:
        print(story_heading.contents[0].strip())


