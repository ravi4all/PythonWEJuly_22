import bs4
import urllib.request as url

path = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
response = url.urlopen(path)

html = bs4.BeautifulSoup(response)
titles = html.find_all('td', {'class' : 'titleColumn'})
ratings = html.find_all('td', {'class' : 'ratingColumn imdbRating'})

for i in range(len(titles)):
    print("Title :",titles[i].text.replace("\n", "").replace("  ", ""))
    print("Rating :",ratings[i].text.replace("\n", "").replace("  ", ""))
    print("*" * 30)
