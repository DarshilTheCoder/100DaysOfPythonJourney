import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')
empire_website = response.text
soup = BeautifulSoup(empire_website,'html.parser')
# print(soup.prettify())
# print(soup.title)
movie_name_list = [movieName.get_text() for movieName in soup.find_all(name='h3',class_ = "listicleItem_listicle-item__title__BfenH")]
movie_name_list.reverse()
with open('movies.txt',mode='w') as file:
    for name in movie_name_list:
        file.write(f"{name}\n")

