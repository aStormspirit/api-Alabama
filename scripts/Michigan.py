from seleniumbase import BaseCase

class Nevada(BaseCase):
    USER_DATA = {
        'name': 'The instruction LLC',
        'firstName': 'John',
        'lastName': 'Doe',
        'address': '20 Barton st.',
        'city': 'Detroid',
        'state': 'Wyoming',
        'phone': '11234567890',
        'zip': '48086',
        'email': 'john19doe19@gmail.com',
    }

    def test(self):
        self.page1()

    def setUp(self):
        super().setUp()
        self.open("https://cofs.lara.state.mi.us/corpweb/LoginSystem/ListNewFilings.aspx")

    def page1(self):
        self.click('#MainContent_parentRepeater_childRepeater_0_link_0')
        self.sleep(5)
        self.type('#MainContent_EntityNameMI1_txtEntityName', self.USER_DATA['name'])
        self.type("#MainContent_ResidentAgentControl1_txtAgentName", self.USER_DATA['firstName'] + " " + self.USER_DATA['lastName'])
        self.type('#MainContent_ResidentAgentControl1_txtAgentAddr1', self.USER_DATA['address'])
        self.type('#MainContent_ResidentAgentControl1_txtAgentCity', self.USER_DATA['city'])
        self.type('#MainContent_ResidentAgentControl1_txtAgentPostalCode', self.USER_DATA['zip'])
        self.type('#MainContent_ResidentAgentControl1_PrincipalOfficeControl_MI1_txtAddr1', self.USER_DATA['address'])
        self.type('#MainContent_ResidentAgentControl1_PrincipalOfficeControl_MI1_txtCity', self.USER_DATA['city'])
        self.type('#MainContent_ResidentAgentControl1_PrincipalOfficeControl_MI1_txtPostalCode', self.USER_DATA['zip'])
        self.click('#MainContent_SignatureControl1_grdSignature_btnAddSignature')
        self.sleep(3)
        self.type('#MainContent_SignatureControl1_txtSignature', self.USER_DATA['firstName'] + " " + self.USER_DATA['lastName'])
        self.click('#MainContent_SignatureControl1_rdoAccept')
        self.click('#MainContent_SignatureControl1_btnSave')
        self.type('#MainContent_FilingFormContactInfoControl1_txtContactName', self.USER_DATA['firstName'] + " " + self.USER_DATA['lastName'])
        self.type('#MainContent_FilingFormContactInfoControl1_txtBusName', self.USER_DATA['name'])
        self.type("#MainContent_FilingFormContactInfoControl1_txtStreetNo", self.USER_DATA['address'])
        self.type("#MainContent_FilingFormContactInfoControl1_txtCity", self.USER_DATA['city'])
        self.type('#MainContent_FilingFormContactInfoControl1_txtPhone', self.USER_DATA['phone'])
        self.type("#MainContent_FilingFormContactInfoControl1_txtContactEmail", self.USER_DATA['email'])
        self.type('#MainContent_FilingFormContactInfoControl1_txtNotificationEmail', self.USER_DATA['email'])
        self.click("#MainContent_ButtonsControlMI1_btnSubmitExternal")


if __name__ == "__main__":
    BaseCase.main(__name__, __file__, '--headed', '--proxy=user210318:u9bkcx@181.215.152.137:8403')