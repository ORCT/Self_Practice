from selenium import webdriver
import time

your_champ = input('input chanmp : ')
browser = webdriver.Chrome('./chromdriver')
browser.get('https://www.op.gg/champion/statistics')
time.sleep(3)

champs = browser.find_elements_by_css_selector('div.champion-index__champion-item__name')
for i in champs:
    if i.text == your_champ:
        i.click()
        break
time.sleep(3)

browser.find_element_by_css_selector('li.champion-stats-menu__list__item.champion-stats-menu__list__item--red.tabHeader > a').click()
time.sleep(2)