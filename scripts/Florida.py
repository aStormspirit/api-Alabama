from seleniumbase import BaseCase
import json
import os
from datetime import datetime


class Florida(BaseCase):
    def read_user_data(self):
        with open(f'./data/{os.environ.get("DATA_ID")}.json', 'r') as file:
            return json.load(file)

    def test(self):
        self.page1()
        self.page2()
        self.page3()
        self.page4()
        self.page5()

    def setUp(self):
        super().setUp()
        self.open("https://dos.fl.gov/sunbiz/start-business/efile/")
        self.data = self.read_user_data()

    def page1(self):
        self.click('/html/body/div[3]/div/div[1]/div/ul/li[1]/div/h2/a', by='xpath')

    def page2(self):
        self.click('/html/body/div[3]/div[1]/div[1]/div[1]/p[5]/strong/a', by='xpath')

    def page3(self):
        self.click('/html/body/div[1]/div[1]/div[2]/div/div[2]/form/p/input', by='xpath')
        self.click('/html/body/div[1]/div[1]/div[2]/div/div[2]/form/div/input', by='xpath')

    def page4(self):
        # Filing Information
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[4]/td/table/tbody/tr/td[2]/input[1]', datetime.now().month)
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[4]/td/table/tbody/tr/td[2]/input[2]', datetime.now().day)
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[4]/td/table/tbody/tr/td[2]/input[3]', datetime.now().year)
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[7]/td/table[1]/tbody/tr/td[2]/input', self.data.get('data').get('company').get('name'))

        #Principal Place of Business
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[9]/td/table/tbody/tr[1]/td[2]/input', self.data.get('data').get('company').get('address').get('street'))
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[9]/td/table/tbody/tr[3]/td[2]/input[1]', self.data.get('data').get('company').get('address').get('city'))
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[12]/td/table/tbody/tr[3]/td[2]/input[2]', self.data.get('data').get('company').get('address').get('state'))
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[9]/td/table/tbody/tr[4]/td[2]/input[1]', self.data.get('data').get('company').get('address').get('zipCode'))
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[9]/td/table/tbody/tr[4]/td[2]/input[2]', self.data.get('state'))

        #Mailing Address
        self.click('/html/body/div[1]/div/div[2]/form/table/tbody/tr[11]/td/table/tbody/tr[2]/td/label')
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[12]/td/table/tbody/tr[1]/td[2]/input', self.data.get('data').get('company').get('address').get('street'))
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[12]/td/table/tbody/tr[3]/td[2]/input[1]', self.data.get('data').get('company').get('address').get('city'))
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[12]/td/table/tbody/tr[3]/td[2]/input[2]', self.data.get('data').get('company').get('address').get('state'))
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[12]/td/table/tbody/tr[4]/td[2]/input[1]', self.data.get('data').get('company').get('address').get('zipCode'))
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[12]/td/table/tbody/tr[4]/td[2]/input[2]', self.data.get('state'))
        
        # Name And Address of Registered Agent
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[14]/td/table/tbody/tr[1]/td[2]/input', self.data.get('data').get('agent').get('lastName'))
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[14]/td/table/tbody/tr[1]/td[3]/input', self.data.get('data').get('agent').get('firstName'))
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[15]/td/table/tbody/tr[4]/td[2]/input', self.data.get('data').get('agent').get('address').get('street'))
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[15]/td/table/tbody/tr[6]/td[2]/input', self.data.get('data').get('agent').get('address').get('city'))
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[15]/td/table/tbody/tr[7]/td[2]/input', self.data.get('data').get('agent').get('address').get('zipCode'))
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[16]/td/table/tbody/tr[2]/td[2]/input', self.data.get('data').get('agent').get('lastName') + ' ' + self.data.get('data').get('agent').get('firstName'))

        #Correspondence Name And E-mail Address
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[23]/td/table/tbody/tr[1]/td[2]/input', self.data.get('data').get('contact').get('lastName') + ' ' + self.data.get('data').get('contact').get('firstName'))
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[23]/td/table/tbody/tr[2]/td[2]/input', self.data.get('data').get('contact').get('email'))
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[23]/td/table/tbody/tr[3]/td[2]/input', self.data.get('data').get('contact').get('email'))
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[24]/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/input', self.data.get('data').get('contact').get('lastName') + ' ' + self.data.get('data').get('contact').get('firstName'))

        #Name And Address of Person(s) Authorized to Manage LLC
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[27]/td/table/tbody/tr[2]/td[2]/input', 'AP')
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[27]/td/table/tbody/tr[4]/td[2]/input', self.data.get('data').get('agent').get('firstName'))
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[27]/td/table/tbody/tr[4]/td[3]/input', self.data.get('data').get('agent').get('firstName'))
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[28]/td/table/tbody/tr[3]/td[2]/input', self.data.get('data').get('agent').get('address').get('street'))
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[28]/td/table/tbody/tr[4]/td[2]/input[1]', self.data.get('data').get('agent').get('address').get('city'))
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[28]/td/table/tbody/tr[4]/td[2]/input[2]', self.data.get('data').get('agent').get('address').get('state'))
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[28]/td/table/tbody/tr[5]/td[2]/input[1]', self.data.get('data').get('agent').get('address').get('zipCode'))
        self.type('/html/body/div[1]/div/div[2]/form/table/tbody/tr[28]/td/table/tbody/tr[5]/td[2]/input[1]', self.data.get('state'))
        self.click('/html/body/div[1]/div/div[2]/form/table/tbody/tr[40]/td/table/tbody/tr/td[1]/input')

    def page5(self):
        self.click('/html/body/div[1]/div[1]/div[2]/form/table/tbody/tr[21]/td/table/tbody/tr/td/input')
        try:
            self.accept_alert(timeout=None)
        except:
            pass
        text = self.get_text('/html/body/div[1]/div[1]/div[2]/form/table/tbody/tr[3]/td/table/tbody/tr/td[2]')
        print('&',text,'&')



if __name__ == "__main__":
    BaseCase.main(__name__, __file__, '--proxy=user210318:u9bkcx@166.0.176.151:6493')