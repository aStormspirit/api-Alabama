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
        # self.open("https://bizfilings.vermont.gov/online/Registration")
        self.open("https://bizfilings.vermont.gov/online/BusinessFormation")

    def test(self):
        # self.registration()
        self.login()
        self.page1()
        self.page2()
        self.page3()

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

    def login(self):
        self.type('#txtUsername', self.USER_DATA['firstName'] + '1234')
        self.type('#txtPassword', self.USER_DATA['firstName'] + '234!')
        self.click('#btnSave')

    def page1(self):
        self.open("https://bizfilings.vermont.gov/online/BusinessFormation")
        self.click('#rdbDomestic')
        self.click_chain(['#typestock', 'option[value="LLC-1"]'])
        self.click_chain(['#domesticLLC', 'option[value="DLLC"]'])
        self.type('#BusinessName', self.USER_DATA['name'])
        self.click_chain(['#ddlBusinessPurpose', 'option[value="Any Legal Purpose"]'])
        self.type('#PrincipalOfficeAddress_StreetAddress1', self.USER_DATA['address'])
        self.type('#PrincipalOfficeAddress_City', self.USER_DATA['city'])
        self.type('#PrincipalOfficeAddress_Zip', self.USER_DATA['zip'])
        self.click('#isSameAsPrincipalAddr')
        self.click('#btnContinue')
        self.sleep(10)

    def page2(self):
        self.type('#BusinessEmail', self.USER_DATA['email'])
        self.click('#btnCreateAgent')
        self.type('#txtagentName', self.USER_DATA['firstName'] + ' ' + self.USER_DATA['lastName'])
        self.click_chain(['#ddlagentType', 'option[value="I"]'])
        self.type('#txtbusinessAddressStreet1', self.USER_DATA['address'])
        self.type('#txtbusinessAddressCity', self.USER_DATA['city'])
        self.type('#txtbusinessAddressZip5', self.USER_DATA['zip'])
        self.click('#chkSameAsPrinc')
        self.click('#btnAssignAgent')
        self.sleep(5)
        self.type('#ChangedAgentEmail', self.USER_DATA['email'])
        self.type('#AuthorizerSignature', self.USER_DATA['firstName'] + ' ' + self.USER_DATA['lastName'])
        self.type('#AuthorizerTitle', 'CEO')
        self.click('#btnAuthContinue')
        self.sleep(10)

    def page3(self):
        self.click('input[value="Proceed to pay"]')
        self.sleep(10)

if __name__ == "__main__":
    BaseCase.main(__name__, __file__, '--headed', '--proxy=user210318:u9bkcx@181.215.152.137:8403')