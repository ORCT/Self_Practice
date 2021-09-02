import urllib.request as req
from bs4 import BeautifulSoup
import urllib.parse as par

keyword =input('input keyword >> ')
encoded = par.quote(keyword)
url = 'https://www.joongang.co.kr/search/news?keyword={}'.format(encoded)
code = req.urlopen(url)
soup = BeautifulSoup(code, 'html.parser')
title = soup.select('h2.headline>a')
for i in title:
    print('제목 : ',i.text)
    print('링크 : ',i.attrs['href'])
    code_news = req.urlopen(i.attrs['href'])
    soup_news = BeautifulSoup(code_news, 'html.parser')
    content = soup_news.select_one('div#article_body')
    print(content.text.strip().replace('  ',''))