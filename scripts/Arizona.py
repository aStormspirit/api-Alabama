from seleniumbase import BaseCase

class Arizona(BaseCase):
    USER_DATA = {
        'name': 'The instruction LLC',
        'firstName': 'John',
        'lastName': 'Doe',
        'address': '123 Main St',
        'city': 'Cody',
        'state': 'Wyoming',
        'zip': '82001',
    }

    LOGIN = {
        "email": "ddgkevinedwards435@gmail.com",
        "password": "Graftio234!",
    }

    def test(self):
        self.login()
        self.page1()
        self.page2()
        self.page3()
        self.page4()
        self.page5()

    def setUp(self):
        super().setUp()
        self.open("https://ecorp.azcc.gov/AzAccount?sessionExpired=False")

    def login(self):
        self.type("#txtEmail", self.LOGIN['email'])
        self.type("#txtPassword", self.LOGIN['password'])
        self.click('#Login')
        self.sleep(10)

    def page1(self):
        self.click('/html/body/div[1]/div[2]/table/tbody/tr/td[2]/a', by='xpath')

    def page2(self):
        self.click('/html/body/div[1]/div[1]/div[1]/div[2]/table/tbody/tr[1]/td[1]/div/div/label', by='xpath')
        self.click('#btnSubmit')

    def page3(self):
        self.type('#BusinessName', self.USER_DATA['name'])
        self.click('#btnSearch')
        self.wait_for_element_clickable('#btnNext')
        self.click('#btnNext')

    def page4(self):
        self.wait_for_element_clickable('#btnNext')
        self.type('#EntityEmailAddress', self.LOGIN['email'])
        self.click_chain(['/html/body/div[1]/div/div[2]/table/tbody/tr[2]/td/div/div[2]/div[1]/div/table/tbody/tr[8]/td/select', '/html/body/div[1]/div/div[2]/table/tbody/tr[2]/td/div/div[2]/div[1]/div/table/tbody/tr[8]/td/select/option[2]'], by='xpath')
        self.click('/html/body/div[1]/div/div[2]/div/div[2]/button', by='xpath')
        self.sleep(5)
        self.click('/html/body/div[4]/div[7]/div/button')
        self.click('#btnNext')

    def page5(self):
        self.click('/html/body/div[1]/div/div[2]/table/tbody/tr[2]/td/div/div[3]/div[1]/div[1]/table[1]/tbody/tr[3]/td/input[2]')
        self.type('#FirstName', self.USER_DATA['firstName'])
        self.type('#LastName', self.USER_DATA['lastName'])
    



if __name__ == "__main__":
    BaseCase.main(__name__, __file__, '--headed', '--proxy=user210318:u9bkcx@166.0.176.151:6493')