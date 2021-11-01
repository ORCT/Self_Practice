from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('./chromedriver')
browser.get('')#copy and paste the address that you want to crawl.
time.sleep(4)

browser.find_element_by_css_selector('html').send_keys(Keys.PAGE_DOWN)
time.sleep(3)

comments = browser.find_elements_by_css_selector('#content-text')
cnt = 0
while 1:
    try :
        print(comments[cnt].text)
    except:
        print('Finished!')
        break
    cnt += 1
    if cnt % 15 == 0:
        browser.find_element_by_css_selector('html').send_keys(Keys.END)
        time.sleep(3)
        comments = browser.find_elements_by_css_selector('#content-text')