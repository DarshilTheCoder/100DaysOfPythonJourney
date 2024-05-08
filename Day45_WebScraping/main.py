from bs4 import BeautifulSoup

with open('website.html',encoding='utf-8') as file:
        content = file.read()
    
soup = BeautifulSoup(content,'html.parser')
# print(soup.prettify())
# print(soup.title) # this will give the first title 
# print(soup.title.name) #this will the the first title as a tag
# print(soup.title.string) #this will the the first content of the title 

# print(soup.a)#this will gives the first anchor tag in html file
# print(soup.find_all('a'))#this will gives all the  anchor tag in html file in list form so that we can loop over it 
print(soup.findAll('p'))

# for link in soup.find_all('a'):
#     print(link.get('href')) 
    
# print(soup.get_text()) # it will give everything in text format

compnay_url = soup.select_one(selector='p a') #it will be work as a CSS selector
print(compnay_url)
name = soup.select_one(selector='#name')
print(name)
headings = soup.select(selector='.heading',limit=1) # will return a list
print(headings)