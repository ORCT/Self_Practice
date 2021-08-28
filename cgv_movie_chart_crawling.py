import urllib.request as req
from bs4 import BeautifulSoup as BS

# get html code from server
code = req.urlopen("http://www.cgv.co.kr/movies/")
#print(code.read())

#arrange html code
soup = BS(code,"html.parser")
#print(soup)

title = soup.select("div.sect-movie-chart strong.title")
#print(title)
for i in title:
    print(i.string)