from seleniumbase import BaseCase
import json
import os

class Kansas(BaseCase):
    def read_user_data(self):
        with open(f'./data/{os.environ.get("DATA_ID")}.json', 'r') as file:
            return json.load(file)

    def set_user_data(self):
        data = self.read_user_data()
        self.log = data['credentials']['login']
        self.password = data['credentials']['password']
        self.name = data['data']['company']['name']
        self.firstName = data['data']['contact']['firstName']
        self.lastName = data['data']['contact']['lastName']
        self.address = data['data']['company']['address']['street']
        self.city = data['data']['company']['address']['city']
        self.state = data['data']['company']['address']['state']
        self.zip = data['data']['company']['address']['zipCode']
        self.email = data['data']['contact']['email']

    def test(self):
        self.sleep(60)
        self.set_user_data()
        print(self.log)
        print(self.password)
        print(self.name)
        print(self.firstName)
        print(self.lastName)
        print(self.address)
        print(self.city)
        print(self.state)
        print(self.zip)
        print(self.email)
        self.login()

    def setUp(self):
        super().setUp()
        self.open("https://www.google.com")

    def login(self):
        self.sleep(60)


if __name__ == "__main__":
    BaseCase.main(__name__, __file__)