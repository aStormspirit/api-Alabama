from seleniumbase import BaseCase

class Vermont(BaseCase):
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
        self.open("https://bizfilings.vermont.gov/online/Registration")

    def test(self):
        self.registration()

    def registration(self):
        self.click_chain(["#lstRole", "[value='BO']"])
        self.type('#CustomerName', f"{self.USER_DATA['firstName']} {self.USER_DATA['lastName']}")
        self.type('#StreetAddress1', self.USER_DATA['address'])
        self.type('#City', self.USER_DATA['city'])
        self.click_chain(["#ddlState", "[value='VT']"])
        self.type('#ZipCode5', self.USER_DATA['zip'])
        self.type('#EmailId', self.USER_DATA['email'])
        self.click('#btnSave')
        self.sleep(1)
        self.type('#UserName', self.USER_DATA['firstName'] + '1234')
        self.type('#password', self.USER_DATA['firstName'] + '234!')
        self.type('#txtRepassword', self.USER_DATA['firstName'] + '234!')
        self.click_chain(['#ddlSecurityQuestion', 'option[value="10"]'])
        self.type('#SecurityAnswer', 'tortila')
        self.click('#btnSave')
        self.sleep(3)
        self.click('input[type="submit"]')
        self.sleep(10)

    def page1(self):
        self.open_new_window()
        self.switch_to_window(1)
        self.open("https://https://bizfilings.vermont.gov/online/BusinessFormation")
        self.click('#isDomesticORForeign')
        self.click_chain(['#BusinessTypeID', 'option[value="LLC-1"]'])



if __name__ == "__main__":
    BaseCase.main(__name__, __file__, '--headed', '--proxy=user210318:u9bkcx@181.215.152.137:8403')