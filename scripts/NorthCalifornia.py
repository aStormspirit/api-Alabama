from seleniumbase import BaseCase

class NorthCalifornia(BaseCase):
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
        "email": "kevinedwards435",
        "password": "Graftio234!"
    }

    def test(self):
        self.login()
        self.page1()
        self.page2()
        self.page3()
        self.page4()
        

    def setUp(self):
        super().setUp()
        self.open("https://www.sosnc.gov/Online_Services/Account/Sign_In?ReturnUrl=%2Fonline_services%2Fbusiness_creation")

    def login(self):
        self.type("/html/body/div[4]/main/article/section/section/form/div/div[1]/input", self.LOGIN['email'], by='xpath')
        self.type("/html/body/div[4]/main/article/section/section/form/div/div[2]/input", self.LOGIN['password'], by='xpath')
        self.click('/html/body/div[4]/main/article/section/section/form/button', by='xpath')
        self.sleep(10)

    def page1(self):
        self.click_chain(['/html/body/div[3]/main/article/section/form/div[1]/div[1]/select', '//*[@id="FilingType_Foreign"]/option[3]'], by='xpath')
        self.click_chain(['//*[@id="FilingType_ProfileTypeId"]', '//*[@id="FilingType_ProfileTypeId"]/option[3]'])
        self.click('//*[@id="next-step"]')

    def page2(self):
        self.type('/html/body/div[3]/main/article/section/form/div[5]/div[2]/input',self.USER_DATA['name'], by='xpath')
        self.click('/html/body/div[3]/main/article/section/form/div[30]/div/button', by='xpath')

    def page3(self):
        self.click_chain(['/html/body/div[3]/main/article/section/form/div[6]/div[2]/div[1]/select', '/html/body/div[3]/main/article/section/form/div[6]/div[2]/div[1]/select/option[10]'], by='xpath')
        self.click_chain(['/html/body/div[3]/main/article/section/form/div[6]/div[2]/div[2]/select', '/html/body/div[3]/main/article/section/form/div[6]/div[2]/div[2]/select/option[2]'], by='xpath')
        self.click('/html/body/div[3]/main/article/section/form/div[30]/div/button')

    def page4(self):
        self.click('/html/body/div[3]/main/article/section/form/div[7]/div[1]/fieldset/ul/li[1]/label')
        self.click('/html/body/div[3]/main/article/section/form/div[30]/div/button')

    def page5(self):
        self.type('/html/body/div[3]/main/article/section/form/div[8]/div[1]/input')
    



if __name__ == "__main__":
    BaseCase.main(__name__, __file__, '--headed', '--proxy=user210318:u9bkcx@166.0.176.151:6493')