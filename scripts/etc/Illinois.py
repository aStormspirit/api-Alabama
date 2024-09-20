from seleniumbase import BaseCase

class Illinois(BaseCase):
    USER_DATA = {
        'name': 'The instruction LLC',
        'firstName': 'John',
        'lastName': 'Doe',
        'address': '123 Main St',
        'city': 'Kansas City',
        'state': 'Wyoming',
        'zip': '67801',
        "email": "ddgkevinedwards435@gmail.com"
    }

    def test(self):
        self.page1()

    def setUp(self):
        super().setUp()
        self.open("https://www.ilsos.gov/departments/business_services/incorporation/home.html")

    def page1(self):
        self.sleep(2000)
        self.click("a[href='https://apps.ilsos.gov/llcarticles/index.jsp']")
        self.sleep(200)
        self.click("#llcNo")
        self.click("input[class='formbutton']")
        self.sleep(2)
        self.click("input[value='y']")
        self.click("input[value='Continue']")
        self.sleep(2)
        self.type("input[name='llcName']", self.USER_DATA['name'])
        self.click("input[value='Continue']")
        self.sleep(5)


if __name__ == "__main__":
    BaseCase.main(__name__, __file__, '--headed', '--proxy=daje5N:byBFuv@45.145.57.234:12451')