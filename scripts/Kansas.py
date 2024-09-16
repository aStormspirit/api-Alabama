from seleniumbase import BaseCase

class Kansas(BaseCase):
    USER_DATA = {
        'name': 'The instruction LLC',
        'firstName': 'John',
        'lastName': 'Doe',
        'address': '123 Main St',
        'city': 'Kansas City',
        'state': 'Wyoming',
        'zip': '67801',
        "email": "ddgkevinedwards435@gmail.com"
    }

    LOGIN = {
        "login": "ddgkevinedwards435@gmail.com",
        "password": "Graftio234!Graftio234"
    }

    def test(self):
        self.login()
        self.page1()

    def setUp(self):
        super().setUp()
        self.open("https://www.sos.ks.gov/eforms/user_login.aspx?frm=BS")

    def login(self):
        self.type("#MainContent_txtUserAccount", self.LOGIN['login'])
        self.type("#MainContent_txtPassword", self.LOGIN['password'])
        self.click("#MainContent_btnSignIn")
        self.sleep(10)

    def page1(self):
        self.click("#MainContent_lnkbtnFormations")
        self.click("#MainContent_rblFilingTypes_2")
        self.click("#MainContent_btnSelectEntityTypeContinue")
        self.sleep(2)
        self.type("#MainContent_txtBusinessName", self.USER_DATA['name'])
        self.click("#MainContent_btnCheckName")
        self.sleep(2)
        self.click("#MainContent_btnNameContinue")
        self.sleep(2)
        self.click("#MainContent_rblRAType_0")
        self.click("#MainContent_btnResidentAgentSubmit")
        self.sleep(2)
        self.type("#MainContent_txtRAEntityName", self.USER_DATA['firstName'] + " " + self.USER_DATA['lastName'])
        self.type("#MainContent_txtRAAddress1", self.USER_DATA['address'])
        self.type("#MainContent_txtRAZip", self.USER_DATA['zip'])
        self.type("#MainContent_txtRACity", self.USER_DATA['city'])
        self.click_chain(["#MainContent_ddlRAStates", "option[value='KS']"])
        self.click("#MainContent_btnResidentAgentSubmit")
        self.click("#MainContent_btnSubmit")
        self.type("#MainContent_gvEmailAddresses_txtEmailAddress", self.USER_DATA['email'])
        self.click("#MainContent_gvEmailAddresses_lbAddNew")
        self.type("#MainContent_gvSignatures_txtSignature", self.USER_DATA['firstName'] + " " + self.USER_DATA['lastName'])
        self.click("#MainContent_gvSignatures_lbAddNew")
        self.click("#MainContent_btnSubmit")


if __name__ == "__main__":
    BaseCase.main(__name__, __file__, '--headed', '--proxy=user210318:u9bkcx@181.215.152.137:8403')