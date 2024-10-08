from seleniumbase import BaseCase

class California(BaseCase):
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
        self.open("https://bot.sannysoft.com/")

    def login(self):
        self.sleep(100)
        self.click('//*[@id="root"]/div/div[1]/div/main/div[2]/div[1]/div[2]/div[1]/div/h3/span', by='xpath')
        self.click('//*[@id="root"]/div/div[1]/div/main/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/button', by='xpath')
        self.type('/html/body/div[2]/main/div[2]/div/div/div[2]/form/div[1]/div[3]/div[1]/div[2]/span/input', self.LOGIN['email'], by='xpath')
        self.type('/html/body/div[2]/main/div[2]/div/div/div[2]/form/div[1]/div[3]/div[2]/div[2]/span/input', self.LOGIN['password'], by='xpath')
        self.click('/html/body/div[2]/main/div[2]/div/div/div[2]/form/div[2]/input', by='xpath')
        self.sleep(100)
    



if __name__ == "__main__":
    BaseCase.main(__name__, __file__, '--headed', '--proxy=user210318:u9bkcx@181.215.152.137:8403')