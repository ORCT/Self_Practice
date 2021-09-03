from selenium import webdriver
import time

browser = webdriver.Chrome('./chromedriver')
browser.get('https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F')
id = browser.find_element_by_css_selector('input#id')
id.send_keys('talingpython')
pw = browser.find_element_by_css_selector('input#inputPwd')
pw.send_keys('qw1w2e3!@#')
browser.find_element_by_css_selector('button#loginBtn').click()
time.sleep(3)

browser.get('https://mail.daum.net/')
time.sleep(2)
#<beautifulsoup>
#1. html get
#2. bs
#3. select
#<selenium>
#1. find_elements_by_css_selector
title = browser.find_elements_by_css_selector('strong.title_subject')
for i in title:
    print(i.text)
browser.close()