from seleniumbase import BaseCase

class Ohio(BaseCase):
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
        "password": "Graftio234!Graftio23",
        "es": 'NSCH'
    }

    def test(self):
        self.login()

    def setUp(self):
        super().setUp()
        self.open("https://bsportal.ohiosos.gov/login.aspx")

    def login(self):
        self.sleep(10)
        self.type("#email", self.LOGIN['email'])
        self.type("#password", self.LOGIN['password'])
        self.click('#submit')
        self.sleep(10)
    



if __name__ == "__main__":
    BaseCase.main(__name__, __file__, '--headed', '--proxy=user210318:u9bkcx@166.0.176.151:6493')