from seleniumbase import BaseCase

class Connecticut(BaseCase):
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
        self.open("https://login.ct.gov/ctidentity/login?goto=https://service.ct.gov/business/s/AccountDashboard")

    def login(self):
        self.sleep(10)
    



if __name__ == "__main__":
    BaseCase.main(__name__, __file__, '--headed', '--proxy=user210318:u9bkcx@181.215.152.137:8403')