from seleniumbase import BaseCase

class NorthCalifornia(BaseCase):

    USER_DATA = {
        'name': 'The instruction LLC',
        'firstName': 'Stan',
        'lastName': 'Smith',
        'address': '2941 23rd St',
        'city': 'Sacramento',
        'state': 'California',
        'zip': '95818',
        "email": "ddgkevinedwards435@gmail.com",
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
        self.page5()
        self.page6()
        self.page7()
        self.page8()
        self.page9()
        self.page10()
        self.page11()
        self.page12()
        self.page13()
        self.page14()
        self.page15()
        

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
        self.click('/html/body/div[3]/main/article/section/form/div[7]/div[1]/fieldset/ul/li[1]/label', by='xpath')
        self.click('/html/body/div[3]/main/article/section/form/div[30]/div/button', by='xpath')

    def page4(self):
        self.type('/html/body/div[3]/main/article/section/form/div[8]/div[1]/input', self.USER_DATA['email'], by='xpath')
        self.click_chain(['/html/body/div[3]/main/article/section/form/div[8]/div[2]/select', '/html/body/div[3]/main/article/section/form/div[8]/div[2]/select/option[3]'], by='xpath')
        self.type('/html/body/div[3]/main/article/section/form/div[8]/div[5]/div/div[1]/input', self.USER_DATA['firstName'], by='xpath')
        self.type('/html/body/div[3]/main/article/section/form/div[8]/div[5]/div/div[3]/input', self.USER_DATA['lastName'], by='xpath')
        self.click('/html/body/div[3]/main/article/section/form/div[30]/div/button', by='xpath')

    def page5(self):
        self.type('/html/body/div[3]/main/article/section/form/div[9]/section/div[1]/textarea', self.USER_DATA['address'], by='xpath')
        self.type('/html/body/div[3]/main/article/section/form/div[9]/section/div[2]/div[1]/input', self.USER_DATA['city'], by='xpath')
        self.type('/html/body/div[3]/main/article/section/form/div[9]/section/div[2]/div[3]/input', self.USER_DATA['zip'], by='xpath')
        self.type('/html/body/div[3]/main/article/section/form/div[9]/section/div[3]/div[1]/input', self.USER_DATA['state'], by='xpath')
        self.click('/html/body/div[3]/main/article/section/form/div[9]/section/div[4]/fieldset/ul/li[1]/label', by='xpath')
        self.click('/html/body/div[3]/main/article/section/form/div[30]/div/button', by='xpath')

    def page6(self):
        self.click_chain(['/html/body/div[3]/main/article/section/form/div[11]/div[1]/select', '/html/body/div[3]/main/article/section/form/div[11]/div[1]/select/option[3]'], by='xpath')
        self.click('/html/body/div[3]/main/article/section/form/div[30]/div/button', by='xpath')

    def page7(self):
        #user Agent form
        self.click('/html/body/div[3]/main/article/section/form/div[14]/section/div[5]/div[2]/span[1]/button', by='xpath')
        self.click_chain(['/html/body/div[3]/main/article/section/form/div[14]/div/div/div[2]/select', '/html/body/div[3]/main/article/section/form/div[14]/div/div/div[2]/select/option[2]'], by='xpath')
        self.click_chain(['/html/body/div[3]/main/article/section/form/div[14]/div/div/div[3]/div[1]/div[1]/select', '/html/body/div[3]/main/article/section/form/div[14]/div/div/div[3]/div[1]/div[1]/select/option[3]'], by='xpath')
        self.type('/html/body/div[3]/main/article/section/form/div[14]/div/div/div[3]/div[3]/div[1]/input', self.USER_DATA['firstName'], by='xpath')
        self.type('/html/body/div[3]/main/article/section/form/div[14]/div/div/div[3]/div[3]/div[3]/input', self.USER_DATA['lastName'], by='xpath')
        self.type('/html/body/div[3]/main/article/section/form/div[14]/div/div/div[3]/div[4]/input', self.USER_DATA['address'], by='xpath')
        self.type('/html/body/div[3]/main/article/section/form/div[14]/div/div/div[3]/div[5]/div[1]/input', self.USER_DATA['city'], by='xpath')
        self.type('/html/body/div[3]/main/article/section/form/div[14]/div/div/div[3]/div[5]/div[3]/input', self.USER_DATA['zip'], by='xpath')
        self.click('/html/body/div[3]/main/article/section/form/div[14]/div/div/div[4]/button[2]', by='xpath')
        self.click('/html/body/div[3]/main/article/section/form/div[14]/section/div[5]/div[1]/fieldset/ul/li/label', by='xpath')
        self.click('/html/body/div[3]/main/article/section/form/div[30]/div/button', by='xpath')

    def page8(self):
        self.sleep(2)
        self.click('/html/body/div[3]/main/article/section/form/div[30]/div/button', by='xpath')
    
    def page9(self):
        self.sleep(2)
        self.click_chain(['/html/body/div[3]/main/article/section/form/div[20]/div[7]/select', '/html/body/div[3]/main/article/section/form/div[20]/div[7]/select/option[2]'], by='xpath')
        self.click('/html/body/div[3]/main/article/section/form/div[30]/div/button', by='xpath')

    def page10(self):
        self.sleep(5)
        self.click('/html/body/div[3]/main/article/section/form/div[30]/div/button', by='xpath')

    def page11(self):
        self.type('/html/body/div[3]/main/article/section/form/div[22]/div[2]/input', '10/14/2024', by='xpath')
        self.click_chain(['/html/body/div[3]/main/article/section/form/div[22]/div[5]/table/tbody/tr[1]/td[1]/select', '/html/body/div[3]/main/article/section/form/div[22]/div[5]/table/tbody/tr[1]/td[1]/select/option[2]'], by='xpath')
        self.click('/html/body/div[3]/main/article/section/form/div[30]/div/button', by='xpath')

    def page12(self):
        self.click_chain(['/html/body/div[3]/main/article/section/form/div[23]/div[2]/select', '/html/body/div[3]/main/article/section/form/div[23]/div[2]/select/option[3]'], by='xpath')

    def page13(self):
        self.sleep(2)
        self.click('/html/body/div[3]/main/article/section/form/div[30]/div/button', by='xpath')

    def page14(self):
        self.sleep(2)
        self.click('/html/body/div[3]/main/article/section/form/div[30]/div/button', by='xpath')

    def page15(self):
        self.sleep(2)
        self.click('/html/body/div[3]/main/article/section/form/div[30]/div/button', by='xpath')  


if __name__ == "__main__":
    BaseCase.main(__name__, __file__, '--headed', '--proxy=user210318:u9bkcx@166.0.176.151:6493')