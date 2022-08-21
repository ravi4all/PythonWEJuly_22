import bs4
import urllib.request as url

path = "https://www.flipkart.com/search?q=jbl+headphones"
response = url.urlopen(path)

html = bs4.BeautifulSoup(response)
# title = html.find('a', {'class' : 's1Q9rs'})
# print("Title :", title.text)

titles = html.find_all('a', {'class' : 's1Q9rs'})
for item in titles:
    print("Title :",item.text)
    print("*" * 20)
