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
        "email": "StanSmith20",
        "password": "Graftio234!"
    }

    def test(self):
        self.login()

    def setUp(self):
        super().setUp()
        self.open("https://ecorp.sos.ga.gov/Account")

    def login(self):
        self.click('/html/body/div[4]/div[3]/div/button', by='xpath')
        self.type("#txtUserId", self.LOGIN['email'])
        self.type("#txtPassword", self.LOGIN['password'])
        self.click('#btnLogin')
        self.sleep(10)
    



if __name__ == "__main__":
    BaseCase.main(__name__, __file__, '--headed', '--proxy=user210318:u9bkcx@181.215.152.137:8403')