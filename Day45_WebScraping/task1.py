import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/')
yc_website = response.text
soup = BeautifulSoup(yc_website,'html.parser')


titles_list = []
titles_link_list = []
title2 = soup.find_all(name='span',class_ = 'titleline')


for title in title2:
    text = title.get_text().split('(')[0]
    titles_list.append(text)
    link = title.a.get('href')
    titles_link_list.append(link)

titles_scores = [int(score.get_text().split(' ')[0]) for score in soup.find_all(name='span',class_ = 'score')]

print(titles_list)
print(titles_link_list)
print(titles_scores)
max_score = max(titles_scores)
max_score_index = titles_scores.index(max_score)
title_of_max_score = titles_list[max_score_index]
title_link_of_max_score = titles_link_list[max_score_index]

print(max_score)
print(max_score_index)
print(title_of_max_score)
print(title_link_of_max_score)
    






