from seleniumbase import BaseCase

class Georgia(BaseCase):
    # при выполнение 3 запросов в минуту просиходит проверка
    USER_DATA = {
        'name': 'The instruction LLC',
        'firstName': 'Stan',
        'lastName': 'Smith',
        'address': '1022 McDaniel St SW',
        'city': 'Atlanta',
        'state': 'Georgia',
        'zip': '30310',
    }

    LOGIN = {
        "email": "ddgkevinedwards435@gmail.com",
        "password": "Graftio234!"
    }

    def test(self):
        self.login()

    def setUp(self):
        super().setUp()
        self.open("https://geauxbiz.sos.la.gov/Dashboard")

    def login(self):
        self.type('/html/body/form/div[3]/div[3]/div[3]/div/div/div[3]/div/div[2]/div[1]/div[2]/input', self.LOGIN['email'], by='xpath')
        self.type('/html/body/form/div[3]/div[3]/div[3]/div/div/div[3]/div/div[2]/div[2]/div[2]/input', self.LOGIN['password'], by='xpath')
        self.click('/html/body/form/div[3]/div[3]/div[3]/div/div/div[3]/div/div[2]/div[3]/div/div[2]/span/input', by='xpath')

    def page1(self):
        self.click('/html/body/div[3]/div/div/div[1]/div[3]/div/div/div[1]/div[2]/div[2]/div[1]/div/div/button', by='xpath')

    def page2(self):
        pass
    



if __name__ == "__main__":
    BaseCase.main(__name__, __file__, '--headed', '--proxy=user210318:u9bkcx@166.0.176.151:6493')