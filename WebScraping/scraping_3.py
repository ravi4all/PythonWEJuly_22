import bs4
import urllib.request as url

path = "https://www.flipkart.com/search?q=iphone+13"
response = url.urlopen(path)

html = bs4.BeautifulSoup(response)

titles = html.find_all('a', {'class' : 's1Q9rs'})

if len(titles) == 0:
    titles = html.find_all('div', {'class' : '_2B099V'})
    if len(titles) == 0:
        titles = html.find_all('div', {'class' : '_4rR01T'})

for item in titles:
    print("Title :",item.text)
    print("*" * 20)

a_tag = html.find('a', {'class' : '_1fQZEK'})
href = a_tag['href']
link = 'https://www.flipkart.com' + href
print(href)
