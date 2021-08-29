import urllib.request as req
from bs4 import BeautifulSoup as BS
import urllib.parse as par
import os

if not os.path.exists('./crawl_image'):
    os.mkdir('./crawl_image')

keyword = input('input keyword >> ')
if not os.path.exists('./crawl_image/{}'.format(keyword)):
    os.mkdir('./crawl_image/{}'.format(keyword))

encoded = par.quote(keyword)#it will change the keyword to some encoded string
url = 'https://www.google.com/search?q={}&tbm=isch&ved=2ahUKEwivrJ_019byAhU5w4sBHRv4DHQQ2-cCegQIABAA&oq={}&gs_lcp=CgNpbWcQAzoFCAAQgAQ6BAgAEB46BAgAEBg6BAgAEBM6BggAEB4QE1DwHli4LWCNL2gBcAB4AIABe4gBjQaSAQMwLjeYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=gLorYa_sELmGr7wPm_CzoAc&bih=1288&biw=1279'.format(encoded, encoded)
reqcode = req.Request(url,headers={'User-Agent': 'Mozilla/5.0'})
code = req.urlopen(reqcode).read()
soup = BS(code, 'html.parser')
image = soup.select('img.rg_i Q4LuWd')
for i in image:
    img_url = i.attrs['data-source']
    try:
        req.urlretrieve(img_url, './crawl_image/{}/{}.png'.format(keyword, image.index[i]+1))
    except:
        print('image does not exist')
    print('{} image crawl complete'.format(image.index[i]+1))