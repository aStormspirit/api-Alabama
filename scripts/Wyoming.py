from selenium import webdriver
from seleniumbase import BaseCase
import time

class Wyoming(BaseCase):
    # Вынесем данные в отдельный словарь для удобства
    USER_DATA = {
        'name': 'The instruction LLC',
        'firstName': 'John',
        'lastName': 'Doe',
        'address': '123 Main St',
        'city': 'Cody',
        'state': 'Wyoming',
        'zip': '82001',
        'phone': '11234567890',
        'email': 'john19doe19@gmail.com',
    }

    def setUp(self):
        super().setUp()
        self.open("https://wyobiz.wyo.gov/Business/RegistrationType.aspx")

    def test(self):
        self.page1()
        self.page2()
        self.page3()
        self.page4()
        self.page5()
        self.page6()
        self.page7()
        self.page8()
        self.page9()
        self.page10()

    def page1(self):
        self.hover_and_click('#MainContent_slctBusType', "[value='RegistrationLLC.aspx']", hover_by="css selector", click_by="css selector")
        self.click("#MainContent_chkAgree")
        self.click("#MainContent_ContinueButton")
        self.wait_and_log("Page 1 complete")

    def page2(self):
        self.type("#txtName", self.USER_DATA['name'])
        self.type('#txtNameConfirm', self.USER_DATA['name'])
        self.click('#ContinueButton')
        self.wait_and_log("Page 2 complete")

    def page3(self):
        self.click('#ContinueButton')
        self.wait_and_log("Page 3 complete")

    def page4(self):
        self.type("#txtFirstName", self.USER_DATA['firstName'])
        self.type("#txtLastName", self.USER_DATA['lastName'])
        self.type("#txtAddr1", self.USER_DATA['address'])
        self.type("#txtCity", self.USER_DATA['city'])
        self.type("#txtPhone", self.USER_DATA['phone'])
        self.type("#txtEmail", self.USER_DATA['email'])
        self.click('#chkRAConsent')
        self.click('#ContinueButton')
        self.sleep(5)
        self.click('#ContinueButton')
        self.wait_and_log("Page 4 complete")


    def page5(self):
        self.type('#txtAddr1', self.USER_DATA['address'])
        self.type('#txtCity', self.USER_DATA['city'])
        self.type('#txtState', self.USER_DATA['state'])
        self.type('#txtPostal', self.USER_DATA['zip'])
        self.type('#txtPhone', self.USER_DATA['phone'])
        self.type('#txtEmail', self.USER_DATA['email'])
        self.type('#txtAddr1Mail', self.USER_DATA['address'])
        self.type('#txtCityMail', self.USER_DATA['city'])
        self.type('#txtStateMail', self.USER_DATA['state'])
        self.type('#txtPostalMail', self.USER_DATA['zip'])
        self.click('#ContinueButton')
        self.wait_and_log("Page 5 complete")

    def page6(self):
        self.type('#txtFirstName', self.USER_DATA['firstName'])
        self.type('#txtLastName', self.USER_DATA['lastName'])
        try:
            self.type('#txtOrgName', self.USER_DATA['name'])
        except:
            pass
        self.type('#txtMail1', f"{self.USER_DATA['address']} {self.USER_DATA['city']} {self.USER_DATA['state']} {self.USER_DATA['zip']}")
        self.click('#SaveButton')
        self.sleep(5)
        self.click('#ContinueButton')
        self.sleep(5)
        self.wait_and_log("Page 6 complete")

    def page7(self):
        self.click('#ContinueButton')
        self.wait_and_log("Page 7 complete")

    def page8(self):
        self.click('#ContinueButton')
        self.wait_and_log("Page 8 complete")

    def page9(self):
        self.click('#chk1')
        self.click('#chk2')
        self.click('#chk3')
        self.click('#chk4')
        self.click('#chk5')
        self.click('#chk7')
        self.click('#chkFalseFiling')
        self.click('#chkFilerIsInd')

        self.type('#txtFirstName', self.USER_DATA['firstName'])
        self.type('#txtLastName', self.USER_DATA['lastName'])
        self.type('#txtTitle', self.USER_DATA['name'])
        self.type('#txtPhone', self.USER_DATA['phone'])
        self.type('#txtPhoneConfirm', self.USER_DATA['phone'])
        self.type('#txtEmail', self.USER_DATA['email'])
        self.type('#txtEmailConfirm', self.USER_DATA['email'])
        self.click('#ContinueButton')
        self.wait_and_log("Page 9 complete")

    def page10(self):
        self.click('#PaymentLink')
        self.wait_and_log("Page 10 complete")

    def wait_and_log(self, message, wait_time=3):
        self.sleep(wait_time)
        print(message)

if __name__ == "__main__":
    BaseCase.main(__name__, __file__, '--headed', '--proxy=user210318:u9bkcx@181.215.152.137:8403')