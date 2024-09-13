from seleniumbase import BaseCase

class Kentucky(BaseCase):
    USER_DATA = {
        'name': 'The instruction',
        'firstName': 'John',
        'lastName': 'Doe',
        'address': '123 Main St',
        'city': 'Frankfort',
        'state': 'KY',
        'zip': '40601',
        'email': 'test@test.com',
    }

    def test(self):
        self.page1()

    def setUp(self):
        super().setUp()
        self.open("https://web.sos.ky.gov/fasttrack/(S(xd4eipwpc2nvh0boaf4wma54))/NewBusiness.aspx")

    def page1(self):
        self.click('#ctl00_MainContent_dombutt')
        self.sleep(5)
        self.click('#ctl00_MainContent_LLClink')
        self.sleep(5)
        self.type("#ctl00_MainContent_TName", self.USER_DATA['name'])
        self.type("#ctl00_MainContent_email", self.USER_DATA['email'])
        self.click("#ctl00_MainContent_managermanaged")
        self.sleep(5)
        self.type("#ctl00_MainContent_POAddr1", self.USER_DATA['address'])
        self.type("#ctl00_MainContent_POCity", self.USER_DATA['city'])
        self.type("#ctl00_MainContent_POState", self.USER_DATA['state'])
        self.type("#ctl00_MainContent_POZip", self.USER_DATA['zip'])
        self.type("#ctl00_MainContent_txtOrgName", self.USER_DATA['firstName'] + " " + self.USER_DATA['lastName'])
        self.click("#ctl00_MainContent_btnAdd")
        self.click("#ctl00_MainContent_rbIndividual")
        self.sleep(5)
        self.type("#ctl00_MainContent_RAFName", self.USER_DATA['firstName'])
        self.type("#ctl00_MainContent_RALName", self.USER_DATA['lastName'])
        self.type("#ctl00_MainContent_RAAddr1", self.USER_DATA['address'])
        self.type("#ctl00_MainContent_RACity", self.USER_DATA['city'])
        self.type("#ctl00_MainContent_RAZip", self.USER_DATA['zip'])
        self.type("#ctl00_MainContent_RAsignFname", self.USER_DATA['firstName'])
        self.type("#ctl00_MainContent_RAsignLname", self.USER_DATA['lastName'])
        self.click("#ctl00_MainContent_CbStandard")
        self.click("#ctl00_MainContent_bFile")
        self.sleep(5)
        self.click("#ctl00_MainContent_good")
        self.sleep(5)





if __name__ == "__main__":
    BaseCase.main(__name__, __file__, '--headed', '--proxy=user210318:u9bkcx@181.215.152.137:8403')