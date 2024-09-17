from selenium import webdriver
import time
from extension import proxies
import undetected_chromedriver as uc


username = "user210318"
password = "u9bkcx"
endpoint = "181.215.152.137"
port = "8403"

chrome_options = webdriver.ChromeOptions()

proxies_extension = proxies(username, password, endpoint, port)

chrome_options.add_extension(proxies_extension)
chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
# chrome_options.add_argument("--headless=new")
chrome_options.add_argument("start-maximized")

class Indiana2:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(options=chrome_options)

    def open_page(self):
        self.driver.get(self.url)
        time.sleep(50)


indiana = Indiana2('https://access.in.gov/client/signin/')

indiana.open_page()