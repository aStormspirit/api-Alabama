from selenium import webdriver
from seleniumbase import BaseCase
import time

class Wyoming(BaseCase):
    name = 'The instruction LLC'
    firstName = 'John'
    lastName = 'Doe'
    address = '123 Main St'
    city = 'Cody'
    state = 'Wyoming'
    zip = '82001'
    phone = '11234567890'
    email = 'john19doe19@gmail.com'
    

    def setUp(self):
        super().setUp()
        self.open("https://wyobiz.wyo.gov/Business/RegistrationType.aspx")

    def test(self):
        self.hover_and_click('#MainContent_slctBusType', "[value='RegistrationLLC.aspx']", hover_by="css selector", click_by="css selector")
        self.click("#MainContent_chkAgree")
        self.click("#MainContent_ContinueButton")
        self.sleep(5)
        print("Page 1 complete")
        self.type("#txtName", self.name)
        self.type('#txtNameConfirm', self.name)
        self.click('#ContinueButton')
        self.sleep(5)
        print("Page 2 complete")
        self.click('#ContinueButton')
        self.sleep(5)
        print("Page 3 complete")
        self.type("#txtFirstName", self.firstName)
        self.type("#txtLastName", self.lastName)
        self.type("#txtAddr1", self.address)
        self.type("#txtCity", self.city)
        self.click('#chkRAConsent')
        self.click('#ContinueButton')
        

if __name__ == "__main__":
    BaseCase.main(__name__, __file__, '--headed', '--proxy=user210318:u9bkcx@181.215.152.137:8403')