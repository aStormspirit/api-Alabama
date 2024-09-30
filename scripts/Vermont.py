from seleniumbase import BaseCase
import json
import os

class Vermont(BaseCase):
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

    def setUp(self):
        super().setUp()
        self.open("https://bizfilings.vermont.gov/online/BusinessFormation")

    def test(self):
        self.set_user_data()
        self.login()
        self.page1()
        self.page2()
        self.page3()

    def login(self):
        self.type('#txtUsername', self.log)
        self.type('#txtPassword', self.password)
        self.click('#btnSave')

    def page1(self):
        self.open("https://bizfilings.vermont.gov/online/BusinessFormation")
        self.click('#rdbDomestic')
        self.click_chain(['#typestock', 'option[value="LLC-1"]'])
        self.click_chain(['#domesticLLC', 'option[value="DLLC"]'])
        self.type('#BusinessName', self.name)
        self.click_chain(['#ddlBusinessPurpose', 'option[value="Any Legal Purpose"]'])
        self.type('#PrincipalOfficeAddress_StreetAddress1', self.address)
        self.type('#PrincipalOfficeAddress_City', self.city)
        self.type('#PrincipalOfficeAddress_Zip', self.zip)
        self.click('#isSameAsPrincipalAddr')
        self.click('#btnContinue')
        self.sleep(10)

    def page2(self):
        self.type('#BusinessEmail', self.email)
        self.click('#btnCreateAgent')
        self.type('#txtagentName', self.firstName + ' ' + self.lastName)
        self.click_chain(['#ddlagentType', 'option[value="I"]'])
        self.type('#txtbusinessAddressStreet1', self.address)
        self.type('#txtbusinessAddressCity', self.city)
        self.type('#txtbusinessAddressZip5', self.zip)
        self.click('#chkSameAsPrinc')
        self.click('#btnAssignAgent')
        self.sleep(5)
        self.type('#ChangedAgentEmail', self.email)
        self.type('#AuthorizerSignature', self.firstName + ' ' + self.lastName)
        self.type('#AuthorizerTitle', 'CEO')
        self.click('#btnAuthContinue')
        self.sleep(10)

    def page3(self):
        self.click('input[value="Proceed to pay"]')
        self.sleep(10)

if __name__ == "__main__":
    BaseCase.main(__name__, __file__, '--headed', '--proxy=user210318:u9bkcx@181.215.152.137:8403')