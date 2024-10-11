import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#2152 166th St, Torrance, CA 90504
# использовать прокси системный или найти аналог подключения в скрипте
# обработка ошибок и ожиданий загрузки эллементов перед взаимодействием

class California:
    def __init__(self):
        self.url = 'https://bizfileonline.sos.ca.gov/forms/business'
        self.driver = uc.Chrome()

    def open_page(self):
        self.driver.get(self.url)
        time.sleep(20)

    def login(self):
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/main/div[2]/div[1]/div[2]/div[1]/div/h3/span').click()
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/main/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/button').click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div/div/div[2]/form/div[1]/div[3]/div[1]/div[2]/span/input').send_keys('ddgkevinedwards435@gmail.com')
        self.driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div/div/div[2]/form/div[1]/div[3]/div[2]/div[2]/span/input').send_keys('Graftio234!')
        self.driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div/div/div[2]/form/div[2]/input').click()

    def page1(self):
        time.sleep(20)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/label[1]').click()
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/button').click()

    def page2(self):
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/form/div/div[2]/div/input').send_keys('Kevin')
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div/input').send_keys('ddgkevinedwards435@gmail.com')
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/form/div/div[4]/div/input').send_keys('8632792045')
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/button[2]').click()

    def page3(self):
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/button[2]').click()

    def page4(self):
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[1]/fieldset/div/div[2]/label').click()
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[1]/div/input').send_keys('The Instruction LLC')
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[2]/div/input').send_keys('The Instruction LLC')
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/button[2]').click()

    def page5(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[1]/div/div/div/div[1]/input').send_keys('2152 166th St')
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[3]/div[1]/div/div/input').send_keys('LOS ANGELES')
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[3]/div[3]/div/div/input').send_keys('90504')
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[3]/div[2]/div/select').click()
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[3]/div[2]/div/select/option[7]').click()
        #Mail Address
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/form/div[3]/div[2]/div/div[1]/div/div/div/div[1]/input').send_keys('2152 166th St')
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/form/div[3]/div[2]/div/div[4]/div[1]/div/div/input').send_keys('LOS ANGELES')
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/form/div[3]/div[2]/div/div[4]/div[3]/div/div/input').send_keys('90504')
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/form/div[3]/div[2]/div/div[4]/div[2]/div/select').click()
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/form/div[3]/div[2]/div/div[4]/div[2]/div/select/option[7]').click()
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/button[2]').click()
        time.sleep(5)

    def page6(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/fieldset/div/div[1]/label').click()
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[3]/div/div[1]/div/div/input').send_keys("Kevin")
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[3]/div/div[3]/div/div/input').send_keys("Edwards")
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[4]/div/div[1]/div/div/div/div[1]/input').send_keys('2152 166th St')
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[4]/div/div[3]/div[1]/div/div/input').send_keys('LOS ANGELES')
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[4]/div/div[3]/div[3]/div/div/input').send_keys('90504')
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/button[2]').click()
        time.sleep(5)

    def page7(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/form/div[3]/div[2]/fieldset/div/div[1]/label'))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/form/div[4]/div[2]/fieldset/div/div[1]/label'))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/button[2]'))
        ).click()

    def page8(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/button[2]').click()

    def page9(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/form/div[3]/div[2]/fieldset/div/div[1]/label').click()
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/form/div[3]/div[4]/div/div/div[2]/div/button').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div[2]/div[1]/div[1]/div/input').send_keys('Kevin Edwards')
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div[2]/div[1]/div[2]/div/div/div/button[1]').click()
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div[2]/div[2]/button').click()
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/form/div[3]/div[3]/div/label[2]').click()
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/button[2]').click()

    def page10(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[1]/div/label[2]').click()
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/form/div[3]/div[1]/fieldset/div/div[1]/label').click()
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/button[2]').click()

    def page11(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/button[2]').click()

    def close_browser(self):
        time.sleep(50)
        self.driver.quit()

scraper = California()

try:
    scraper.open_page()
    scraper.login()
    scraper.page1()
    scraper.page2()
    scraper.page3()
    scraper.page4()
    scraper.page5()
    scraper.page6()
    scraper.page7()
    scraper.page8()
    scraper.page9()
    scraper.page10()
    scraper.page11()

finally:
    scraper.close_browser()

