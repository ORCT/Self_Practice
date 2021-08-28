import urllib.request as req
from bs4 import BeautifulSoup as BS

print('=============== menu ===============')
print('1. America')
print('2. Japan')
print('3. Europe')
print('4. China')
print('====================================')
menu = int(input("select >> "))
unit = ["dollar", 'yen', 'euro', 'yiuan ']
money = int(input('input price ({}) >> '.format(unit[menu-1])))
if menu == 2:
    money = money / 100

code = req.urlopen("https://finance.naver.com/marketindex/")
soup = BS(code, "html.parser")
price = soup.select("span.value")
#price = soup.select("ul#exchangeList span.value")
print(float(price[menu-1].string.replace(',',''))*money)