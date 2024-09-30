from seleniumbase import BaseCase
import json
import os

class Kentucky(BaseCase):
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

    def test(self):
        self.set_user_data()
        self.page1()

    def setUp(self):
        super().setUp()
        self.open("https://web.sos.ky.gov/fasttrack/(S(xd4eipwpc2nvh0boaf4wma54))/NewBusiness.aspx")

    def page1(self):
        self.click('#ctl00_MainContent_dombutt')
        self.sleep(5)
        self.click('#ctl00_MainContent_LLClink')
        self.sleep(5)
        self.type("#ctl00_MainContent_TName", self.name)
        self.type("#ctl00_MainContent_email", self.email)
        self.click("#ctl00_MainContent_managermanaged")
        self.sleep(5)
        self.type("#ctl00_MainContent_POAddr1", self.address)
        self.type("#ctl00_MainContent_POCity", self.city)
        self.type("#ctl00_MainContent_POState", self.state)
        self.type("#ctl00_MainContent_POZip", self.zip)
        self.type("#ctl00_MainContent_txtOrgName", self.firstName + " " + self.lastName)
        self.click("#ctl00_MainContent_btnAdd")
        self.click("#ctl00_MainContent_rbIndividual")
        self.sleep(5)
        self.type("#ctl00_MainContent_RAFName", self.firstName)
        self.type("#ctl00_MainContent_RALName", self.lastName)
        self.type("#ctl00_MainContent_RAAddr1", self.address)
        self.type("#ctl00_MainContent_RACity", self.city)
        self.type("#ctl00_MainContent_RAZip", self.zip)
        self.type("#ctl00_MainContent_RAsignFname", self.firstName)
        self.type("#ctl00_MainContent_RAsignLname", self.lastName)
        self.click("#ctl00_MainContent_CbStandard")
        self.click("#ctl00_MainContent_bFile")
        self.sleep(5)
        self.click("#ctl00_MainContent_good")
        self.sleep(5)





if __name__ == "__main__":
    BaseCase.main(__name__, __file__, '--headed', '--proxy=user210318:u9bkcx@181.215.152.137:8403')