from seleniumbase import BaseCase
import json
import os

class Wyoming(BaseCase):
    def read_user_data(self):
        with open(f'./data/{os.environ.get("DATA_ID")}.json', 'r') as file:
            return json.load(file)

    def set_user_data(self):
        data = self.read_user_data()
        self.log = data['credentials']['login']
        self.password = data['credentials']['password']
        self.name = data['data']['company']['name']
        self.firstName = data['data']['contact']['firstName']
        self.lastName = data['data']['contact']['lastName']
        self.address = data['data']['company']['address']['street']
        self.city = data['data']['company']['address']['city']
        self.state = data['data']['company']['address']['state']
        self.zip = data['data']['company']['address']['zipCode']
        self.email = data['data']['contact']['email']
        self.phone = data['data']['contact']['phone']
    def setUp(self):
        super().setUp()
        self.open("https://wyobiz.wyo.gov/Business/RegistrationType.aspx")

    def test(self):
        self.set_user_data()
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
        self.type("#txtName", self.name)
        self.type('#txtNameConfirm', self.name)
        self.click('#ContinueButton')
        self.wait_and_log("Page 2 complete")

    def page3(self):
        self.click('#ContinueButton')
        self.wait_and_log("Page 3 complete")

    def page4(self):
        self.type("#txtFirstName", self.firstName)
        self.type("#txtLastName", self.lastName)
        self.type("#txtAddr1", self.address)
        self.type("#txtCity", self.city)
        self.type("#txtPhone", self.phone)
        self.type("#txtEmail", self.email)
        self.click('#chkRAConsent')
        self.click('#ContinueButton')
        self.sleep(5)
        self.click('#ContinueButton')
        self.wait_and_log("Page 4 complete")


    def page5(self):
        self.type('#txtAddr1', self.address)
        self.type('#txtCity', self.city)
        self.type('#txtState', self.state)
        self.type('#txtPostal', self.zip)
        self.type('#txtPhone', self.phone)
        self.type('#txtEmail', self.email)
        self.type('#txtAddr1Mail', self.address)
        self.type('#txtCityMail', self.city)
        self.type('#txtStateMail', self.state)
        self.type('#txtPostalMail', self.zip)
        self.click('#ContinueButton')
        self.wait_and_log("Page 5 complete")

    def page6(self):
        self.type('#txtFirstName', self.firstName)
        self.type('#txtLastName', self.lastName)
        try:
            self.type('#txtOrgName', self.name)
        except:
            pass
        self.type('#txtMail1', f"{self.address} {self.city} {self.state} {self.zip}")
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

        self.type('#txtFirstName', self.firstName)
        self.type('#txtLastName', self.lastName)
        self.type('#txtTitle', self.name)
        self.type('#txtPhone', self.phone)
        self.type('#txtPhoneConfirm', self.phone)
        self.type('#txtEmail', self.email)
        self.type('#txtEmailConfirm', self.email)
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