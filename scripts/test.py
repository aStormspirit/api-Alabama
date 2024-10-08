import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class California:
    def __init__(self):
        self.url = 'https://bizfileonline.sos.ca.gov/forms/business'
        self.driver = uc.Chrome()

    def open_page(self):
        self.driver.get(self.url)
        time.sleep(20)

    def click(str):
        pass

    def login(self):

        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/main/div[2]/div[1]/div[2]/div[1]/div/h3/span').click()
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/main/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/button').click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div/div/div[2]/form/div[1]/div[3]/div[1]/div[2]/span/input').send_keys('ddgkevinedwards435@gmail.com')
        self.driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div/div/div[2]/form/div[1]/div[3]/div[2]/div[2]/span/input').send_keys('Graftio234!')
        self.driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div/div/div[2]/form/div[2]/input').click()

    def close_browser(self):
        time.sleep(50)
        self.driver.quit()

scraper = California()

try:
    scraper.open_page()
    scraper.login()
finally:
    scraper.close_browser()

