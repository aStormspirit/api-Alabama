from seleniumbase import BaseCase

class Florida(BaseCase):
    USER_DATA = {
        'name': 'The instruction LLC',
        'firstName': 'John',
        'lastName': 'Doe',
        'address': '123 Main St',
        'city': 'Cody',
        'state': 'FL',
        'zip': '82001',
        'country': 'BC'
    }

    LOGIN = {
        "email": "ddgkevinedwards435@gmail.com",
        "password": "Graftio234!Graftio234"
    }

    def test(self):
        self.page1()
        self.page2()
        self.page3()
        self.page4()
        self.page5()

    def setUp(self):
        super().setUp()
        self.open("https://dos.fl.gov/sunbiz/start-business/efile/")

    def page1(self):
        self.click('/html/body/div[3]/div/div[1]/div/ul/li[1]/div/h2/a', by='xpath')

    def page2(self):
        self.click('/html/body/div[3]/div[1]/div[1]/div[1]/p[5]/strong/a', by='xpath')

    def page3(self):
        self.click('/html/body/div[1]/div[1]/div[2]/div/div[2]/form/p/input', by='xpath')
        self.click('/html/body/div[1]/div[1]/div[2]/div/div[2]/form/div/input', by='xpath')

    def page4(self):
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[4]/td/table/tbody/tr/td[2]/input[1]', 10)
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[4]/td/table/tbody/tr/td[2]/input[2]', 17)
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[4]/td/table/tbody/tr/td[2]/input[3]', 2024)
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[7]/td/table[1]/tbody/tr/td[2]/input', self.USER_DATA['name'])
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[9]/td/table/tbody/tr[1]/td[2]/input', self.USER_DATA['address'])
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[9]/td/table/tbody/tr[3]/td[2]/input[1]', self.USER_DATA['city'])
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[12]/td/table/tbody/tr[3]/td[2]/input[2]', self.USER_DATA['state'])
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[9]/td/table/tbody/tr[4]/td[2]/input[1]', self.USER_DATA['zip'])
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[9]/td/table/tbody/tr[4]/td[2]/input[2]', self.USER_DATA['country'])
        self.click('/html/body/div[1]/div/div[2]/form/table/tbody/tr[11]/td/table/tbody/tr[2]/td/label')
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[12]/td/table/tbody/tr[1]/td[2]/input', self.USER_DATA['address'])
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[12]/td/table/tbody/tr[3]/td[2]/input[1]', self.USER_DATA['city'])
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[12]/td/table/tbody/tr[3]/td[2]/input[2]', self.USER_DATA['state'])
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[12]/td/table/tbody/tr[4]/td[2]/input[1]', self.USER_DATA['zip'])
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[12]/td/table/tbody/tr[4]/td[2]/input[2]', self.USER_DATA['country'])
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[14]/td/table/tbody/tr[1]/td[2]/input', self.USER_DATA['lastName'])
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[14]/td/table/tbody/tr[1]/td[3]/input', self.USER_DATA['firstName'])
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[15]/td/table/tbody/tr[4]/td[2]/input', self.USER_DATA['address'])
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[15]/td/table/tbody/tr[6]/td[2]/input', self.USER_DATA['city'])
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[15]/td/table/tbody/tr[7]/td[2]/input', self.USER_DATA['zip'])
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[16]/td/table/tbody/tr[2]/td[2]/input', self.USER_DATA['firstName'] + ' ' + self.USER_DATA['lastName'])
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[23]/td/table/tbody/tr[1]/td[2]/input', self.USER_DATA['firstName'] + ' ' + self.USER_DATA['lastName'])
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[23]/td/table/tbody/tr[2]/td[2]/input', self.LOGIN['email'])
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[23]/td/table/tbody/tr[3]/td[2]/input', self.LOGIN['email'])
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[24]/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/input', self.USER_DATA['firstName'] + ' ' + self.USER_DATA['lastName'])
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[27]/td/table/tbody/tr[2]/td[2]/input', 'AP')
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[27]/td/table/tbody/tr[4]/td[2]/input', self.USER_DATA['firstName'])
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[27]/td/table/tbody/tr[4]/td[3]/input', self.USER_DATA['lastName'])
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[28]/td/table/tbody/tr[3]/td[2]/input', self.USER_DATA['address'])
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[28]/td/table/tbody/tr[4]/td[2]/input[1]', self.USER_DATA['city'])
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[28]/td/table/tbody/tr[4]/td[2]/input[2]', self.USER_DATA['state'])
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[28]/td/table/tbody/tr[5]/td[2]/input[1]', self.USER_DATA['zip'])
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[28]/td/table/tbody/tr[5]/td[2]/input[1]', self.USER_DATA['country'])
        self.click('/html/body/div[1]/div/div[2]/form/table/tbody/tr[40]/td/table/tbody/tr/td[1]/input')

    def page5(self):
        self.click('/html/body/div[1]/div[1]/div[2]/form/table/tbody/tr[21]/td/table/tbody/tr/td/input')
        try:
            self.accept_alert(timeout=None)
        except:
            pass
        self.click('/html/body/div[1]/div[1]/div[2]/table[1]/tbody/tr[4]/td/table/tbody/tr[3]/td/form/input[15]')



if __name__ == "__main__":
    BaseCase.main(__name__, __file__, '--headed', '--proxy=user210318:u9bkcx@166.0.176.151:6493')