from seleniumbase import BaseCase

class Nevada(BaseCase):
    USER_DATA = {
        'name': 'The instruction LLC',
        'firstName': 'John',
        'lastName': 'Doe',
        'address': '123 Main St',
        'city': 'Cody',
        'state': 'Wyoming',
        'zip': '82001',
    }

    def test(self):
        self.login()

    def setUp(self):
        super().setUp()
        self.open("https://www.nvsilverflume.gov/login")

    def login(self):
        self.type("#email", self.LOGIN['email'])
        self.type("#password", self.LOGIN['password'])
        self.click('#submit')
        self.sleep(10)
    



if __name__ == "__main__":
    BaseCase.main(__name__, __file__, '--headed', '--proxy=user210318:u9bkcx@181.215.152.137:8403')