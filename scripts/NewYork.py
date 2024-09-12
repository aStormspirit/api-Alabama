from seleniumbase import BaseCase

class NewYork(BaseCase):
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
        "login": "JohnDoe789",
        "password": "Agent007Agent007"
    }

    def test(self):
        self.login()

    def setUp(self):
        super().setUp()
        self.open("https://www.businessexpress.ny.gov/app")

    def login(self):
        self.click('a[href="/app/loginregister?p_next_page=/app/dashboard/recentActivity"]')
        self.click('button.btn.btn-lg.btn-primary.btn-call-to-action-primary[name="primary"][type="button"]')
        self.sleep(2)
        self.refresh_page()
        self.sleep(10)  # Даем странице время для полной перезагрузки
        self.assert_element_present('div.inputContainer')
        self.sleep(10)  # Даем странице время для полной перезагрузки
        self.type('#loginform\\:username', self.LOGIN['login'])
        self.type('#loginform\\:password', self.LOGIN['password'])
        self.click('#loginform\\:signinButton')
        self.sleep(100)
    



if __name__ == "__main__":
    BaseCase.main(__name__, __file__, '--headed', '--proxy=user210318:u9bkcx@181.215.152.137:8403')