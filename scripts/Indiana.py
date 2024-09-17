from seleniumbase import BaseCase
from selenium import webdriver
import undetected_chromedriver as uc

class Indiana(BaseCase):
    USER_DATA = {
        'name': 'The instruction LLC',
        'firstName': 'John',
        'lastName': 'Doe',
        'address': '123 Main St',
        'city': 'Cody',
        'state': 'Wyoming',
        'zip': '82001',
    }

    LOGIN = {
        "login": "ddgkevinedwards435@gmail.com",
        "password": "Graftio234!"
    }


    # def get_new_driver(self, *args, **kwargs):
    #     """ This method overrides get_new_driver() from BaseCase. """
    #     driver = webdriver.Chrome()
    #     return driver

    def test(self):
        self.login()

    def setUp(self):
        super().setUp()
        self.open("https://inbiz.in.gov/")

    def login(self):
        print(self.driver.get_cookies())
        self.sleep(50)


if __name__ == "__main__":
    BaseCase.main(__name__, __file__, '--headed', '--proxy=user210318:u9bkcx@181.215.152.137:8403')