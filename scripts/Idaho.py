from seleniumbase import BaseCase

class Idaho(BaseCase):
    USER_DATA = {
        'name': 'The instruction LLC',
        'firstName': 'John',
        'lastName': 'Doe',
        'address': '10565 W Silvercity Ct',
        'city': 'Boise',
        'state': 'Idaho',
        'zip': '83704',
    }

    LOGIN = {
        "email": "ddgkevinedwards435@gmail.com",
        "password": "Graftio234"
    }

    def test(self):
        self.login()
        self.page_1()
        self.page_2()
        self.page_3()
        self.page_4()
        self.page_5()

    def setUp(self):
        super().setUp()
        self.open("https://sosbiz.idaho.gov/forms/new/290")

    def login(self):
        self.sleep(5)
        self.type("#username", self.LOGIN['email'])
        self.type("#password", self.LOGIN['password'])
        self.click('.submit')

    def page_1(self):
        self.sleep(5)
        self.click('//*[@id="field-HkZzf6SaN"]/div[1]/label', by='xpath')
        self.type('#field-field1-undefined', self.USER_DATA['name'])
        self.type('#field-field2-undefined', self.USER_DATA['name'])
        self.click('.next')

    def page_2(self):
        self.sleep(5)
        # street address
        self.type('#field-address1-r1lfZGRIgX', self.USER_DATA['address'])
        self.type('#field-addr-city-r1lfZGRIgX', self.USER_DATA['city'])
        self.type('#field-addr-zip-r1lfZGRIgX', self.USER_DATA['zip'])
        # PO Box
        self.type('#field-address1-HJzMbzRIxm', self.USER_DATA['address'])
        self.type('#field-addr-city-HJzMbzRIxm', self.USER_DATA['city'])
        self.type('#field-addr-zip-HJzMbzRIxm', self.USER_DATA['zip'])
        self.click('.next')

    def page_3(self):
        self.sleep(5)
        self.click('//*[@id="field-TYPE_ID"]/div[2]/label', by='xpath')
        self.click('//*[@id="wizard-body-scroll-container"]/form/div[2]/div[3]/div/div[1]/div/div/div[3]/div/button', by='xpath')
        self.type('input[name="FIRST_NAME"]', self.USER_DATA['firstName'])
        self.type('input[name="LAST_NAME"]', self.USER_DATA['lastName'])
        self.type('//*[@id="field-address1-SJBKrsl8M_PRIMARY"]', self.USER_DATA['address'], by='xpath')
        self.type('//*[@id="field-addr-city-SJBKrsl8M_PRIMARY"]', self.USER_DATA['city'], by='xpath')
        self.type('//*[@id="field-addr-zip-SJBKrsl8M_PRIMARY"]', self.USER_DATA['zip'], by='xpath')
        self.type('//*[@id="field-address1-SJBKrsl8M_MAIL"]', self.USER_DATA['address'], by='xpath')
        self.type('//*[@id="field-addr-city-SJBKrsl8M_MAIL"]', self.USER_DATA['city'], by='xpath')
        self.type('//*[@id="field-addr-zip-SJBKrsl8M_MAIL"]', self.USER_DATA['zip'], by='xpath')
        self.click('/html/body/div[3]/div/div[1]/div[2]/div[5]/button', by='xpath')
        self.sleep(2)
        self.click('//*[@id="label-SJZTVExQI"]', by='xpath')
        self.click('//*[@id="wizard-body-scroll-container"]/div[2]/div/button[2]', by='xpath')
        
    def page_4(self):
        self.sleep(5)
        self.click('//*[@id="wizard-body-scroll-container"]/form/div[2]/div[2]/div/div/div[2]/div/button', by='xpath')
        self.type('//*[@id="field-firstname-Hy1LFYzqX"]', self.USER_DATA['firstName'], by='xpath')
        self.type('//*[@id="field-lastname-Hy1LFYzqX"]', self.USER_DATA['lastName'], by='xpath')
        self.type('//*[@id="field-address1-ByOoRiT-f"]', self.USER_DATA['address'], by='xpath')
        self.type('//*[@id="field-addr-city-ByOoRiT-f"]', self.USER_DATA['city'], by='xpath')
        self.type('//*[@id="field-addr-zip-ByOoRiT-f"]', self.USER_DATA['zip'], by='xpath')
        self.click('/html/body/div[3]/div/div[1]/div[2]/div[2]/button', by='xpath')
        self.click('//*[@id="wizard-body-scroll-container"]/div[2]/div/button[2]', by='xpath')
        self.click('//*[@id="wizard-body-scroll-container"]/div[2]/div/button[2]', by='xpath')

    def page_5(self):
        self.click('//*[@id="label-BJq3U6IZM"]', by='xpath')
        self.click('//*[@id="label-HJNp8TUbM"]', by='xpath')
        self.click('//*[@id="label-HyuaLa8Wf"]', by='xpath')
        self.type('//*[@id="wizard-body-scroll-container"]/form/div[4]/div[2]/div/div[2]/div/div[1]/div/input', self.USER_DATA['firstName'] + ' ' + self.USER_DATA['lastName'])
        self.click('//*[@id="wizard-body-scroll-container"]/form/div[4]/div[2]/div/div[2]/div/div[2]/div/button[1]', by='xpath')
        self.click('//*[@id="wizard-body-scroll-container"]/div[2]/div/button[2]', by='xpath')
        self.sleep(5)
        self.click('//*[@id="sliding-panel-scrollable"]/div/div[2]/div/fieldset/form[1]/button[1]/div/span', by='xpath')
        self.sleep(50)








    



if __name__ == "__main__":
    BaseCase.main(__name__, __file__, '--headed', '--proxy=user210318:u9bkcx@166.0.176.151:6493')