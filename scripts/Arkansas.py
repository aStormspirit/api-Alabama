from seleniumbase import BaseCase

class Arkansas(BaseCase):
    USER_DATA = {
        'name': 'The instruction LLC',
        'firstName': 'John',
        'lastName': 'Doe',
        'address': '918 Watkins St',
        'city': 'Conway',
        'state': 'Arkansas',
        'zip': '72034',
        'phone': '8632792045'
    }

#104 Garden Rd, River Ridge, LA 70123, США

    LOGIN = {
        "email": "ddgkevinedwards435@gmail.com",
        "password": "Graftio234!Graftio234"
    }

    def test(self):
        self.page1()

    def setUp(self):
        super().setUp()
        self.open("https://www.ark.org/sos/corpfilings/index.php")

    def page1(self):
        self.click('//*[@id="home_container"]/table/tbody/tr[32]/td[2]/a', by='xpath')
        self.click('/html/body/div[2]/div/div[2]/div/div/form/div[2]/table/tbody/tr[33]/td[3]/form/input[3]', by='xpath')
        self.sleep(2)
        self.type('#entity_name', self.USER_DATA['name'])
        self.type('#principal_first_name', self.USER_DATA['firstName'])
        self.type('#principal_last_name', self.USER_DATA['lastName'])
        self.type('#principal_address_1', self.USER_DATA['address'])
        self.type("#principal_city", self.USER_DATA['city'])
        self.type("#principal_zip_code", self.USER_DATA['zip'])
        #agent
        self.type("#agent_first_name", self.USER_DATA['firstName'])
        self.type("#agent_last_name", self.USER_DATA['lastName'])
        self.type("#agent_address_1", self.USER_DATA['address'])
        self.type("#agent_zip_code", self.USER_DATA['zip'])
        self.type("#agent_city", self.USER_DATA['city'])
        #oficier
        self.type('#officer_first_name', self.USER_DATA['firstName'])
        self.type('#officer_last_name', self.USER_DATA['lastName'])
        self.click_chain(['#officer_title', 'option[value="IncorporatorOrganizer"]'])
        self.type('#officer_address_1', self.USER_DATA['address'])
        self.type('#officer_city', self.USER_DATA['city'])
        self.type('#officer_zip_code', self.USER_DATA['zip'])
        self.click('//*[@id="officer_input"]/p[14]/input[2]', by='xpath')
        #oficier2
        self.type('#officer_first_name', self.USER_DATA['firstName'])
        self.type('#officer_last_name', self.USER_DATA['lastName'])
        self.click_chain(['#officer_title', 'option[value="Manager"]'])
        self.type('#officer_address_1', self.USER_DATA['address'])
        self.type('#officer_city', self.USER_DATA['city'])
        self.type('#officer_zip_code', self.USER_DATA['zip'])
        self.click('//*[@id="officer_input"]/p[14]/input[2]', by='xpath')
        #submitter
        self.type('#contact_first_name', self.USER_DATA['firstName'])
        self.type("#contact_last_name", self.USER_DATA['lastName'])
        self.type("#contact_address_1", self.USER_DATA['address'])
        self.type("#contact_city", self.USER_DATA['city'])
        self.type("#contact_zip_code", self.USER_DATA['zip'])
        self.type("#contact_phone_number", self.USER_DATA['phone'])
        self.type("#contact_email", self.LOGIN['email'])
        #tax
        self.type("#tax_contact_first_name", self.USER_DATA['firstName'])
        self.type("#tax_contact_last_name", self.USER_DATA['lastName'])
        self.type("#tax_contact_address_1", self.USER_DATA['address'])
        self.type('#tax_contact_city', self.USER_DATA['city'])
        self.type('#tax_contact_zip_code', self.USER_DATA['zip'])
        self.type('#tax_contact_phone_number', self.USER_DATA['phone'])
        self.type('#tax_contact_email', self.LOGIN['email'])
        self.type('#tax_contact_signature', self.USER_DATA['firstName'] + ' ' + self.USER_DATA['lastName'])
        self.click('#agreement')
        self.type('#filing_signature', self.USER_DATA['firstName'] + ' ' + self.USER_DATA['lastName'])
        self.click('#save_form')
        self.sleep(2)
        self.click('//*[@id="app_form"]/fieldset/p[7]/input', by='xpath')
        self.sleep(2)
        self.click('//*[@id="app_form"]/p[2]/input', by='xpath')
        self.sleep(2)
        self.click('#payMethodCC')
        #!
        self.click('#start.continue')


    



if __name__ == "__main__":
    BaseCase.main(__name__, __file__, '--headed', '--proxy=user210318:u9bkcx@181.215.152.137:8403')