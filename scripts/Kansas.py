from seleniumbase import BaseCase
import json
from model import RootModel

class Kansas(BaseCase):
    def read_user_data(self) -> RootModel:
        with open('./data.json', 'r') as file:
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
        self.login()
        self.page1()

   
    def setUp(self):
        super().setUp()
        self.open("https://www.sos.ks.gov/eforms/user_login.aspx?frm=BS")

    def login(self):
        self.type("#MainContent_txtUserAccount", self.log)
        self.type("#MainContent_txtPassword", self.password)
        self.click("#MainContent_btnSignIn")
        self.sleep(10)

    def page1(self):
        self.click("#MainContent_lnkbtnFormations")
        self.click("#MainContent_rblFilingTypes_2")
        self.click("#MainContent_btnSelectEntityTypeContinue")
        self.sleep(2)
        self.type("#MainContent_txtBusinessName", self.name)
        self.click("#MainContent_btnCheckName")
        self.sleep(2)
        self.click("#MainContent_btnNameContinue")
        self.sleep(2)
        self.click("#MainContent_rblRAType_0")
        self.click("#MainContent_btnResidentAgentSubmit")
        self.sleep(2)
        self.type("#MainContent_txtRAEntityName", self.firstName + " " + self.lastName)
        self.type("#MainContent_txtRAAddress1", self.address)
        self.type("#MainContent_txtRAZip", self.zip)
        self.type("#MainContent_txtRACity", self.city)
        self.click_chain(["#MainContent_ddlRAStates", "option[value='KS']"])
        self.click("#MainContent_btnResidentAgentSubmit")
        self.click("#MainContent_btnSubmit")
        self.type("#MainContent_gvEmailAddresses_txtEmailAddress", self.email)
        self.click("#MainContent_gvEmailAddresses_lbAddNew")
        self.type("#MainContent_gvSignatures_txtSignature", self.firstName + " " + self.lastName)
        self.click("#MainContent_gvSignatures_lbAddNew")
        self.click("#MainContent_btnSubmit")


if __name__ == "__main__":
    BaseCase.main(__name__, __file__, '--headed', '--proxy=user210318:u9bkcx@181.215.152.137:8403')