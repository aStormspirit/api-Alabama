from seleniumbase import BaseCase

class Texas(BaseCase):
    # при выполнение 3 запросов в минуту просиходит проверка
    USER_DATA = {
        'name': 'The instruction LLC',
        'firstName': 'Stan',
        'lastName': 'Smith',
        'address': '1022 McDaniel St SW',
        'city': 'Atlanta',
        'state': 'Georgia',
        'zip': '30310',
        'phone': '8632792045'
    }

    LOGIN = {
        "email": "StanSmith20",
        "password": "Graftio234!"
    }

    def test(self):
        self.page1()
        self.page2()

    def setUp(self):
        super().setUp()
        self.open("https://direct.sos.state.tx.us/acct/acct-subscribe.asp")

    def page1(self):
        self.type('/html/body/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table/tbody/tr[1]/td[1]/font/input', self.USER_DATA['lastName'], by='xpath')
        self.type('/html/body/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table/tbody/tr[1]/td[2]/font/input', self.USER_DATA['firstName'], by='xpath')

    def page2(self):
        self.type('/html/body/table[2]/tbody/tr[2]/td/table/tbody/tr[2]/td/font/input', self.USER_DATA['address'], by='xpath')
        self.type('/html/body/table[2]/tbody/tr[2]/td/table/tbody/tr[4]/td/table/tbody/tr/td[1]/font/input', self.USER_DATA['city'], by='xpath')
        self.type('/html/body/table[2]/tbody/tr[2]/td/table/tbody/tr[4]/td/table/tbody/tr/td[3]/font/input', self.USER_DATA['zip'], by='xpath')
        self.type('/html/body/table[2]/tbody/tr[2]/td/table/tbody/tr[6]/td/table/tbody/tr/td[1]/font/input', self.USER_DATA['phone'], by='xpath')
        self.type('/html/body/table[2]/tbody/tr[2]/td/table/tbody/tr[6]/td/table/tbody/tr/td[4]/font/input', self.USER_DATA['email'], by='xpath')
        self.click('/html/body/table[2]/tbody/tr[3]/td/input', by='xpath')


    



if __name__ == "__main__":
    BaseCase.main(__name__, __file__, '--headed', '--proxy=user210318:u9bkcx@166.0.176.151:6493')