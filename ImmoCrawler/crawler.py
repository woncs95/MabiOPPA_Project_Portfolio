from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('/Users/beomi/Downloads/chromedriver')
driver.implicitly_wait(3)
driver.get('https://k-immo.de/angebote/')