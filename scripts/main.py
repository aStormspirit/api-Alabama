from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time

class WebScraper:
    def __init__(self, url, name, lastName, firstName, streetAddress, city, zipCode, email, phone):
        self.url = url
        self.driver = webdriver.Chrome()
        self.name = name
        self.lastName = lastName
        self.firstName = firstName
        self.streetAddress = streetAddress
        self.city = city
        self.zipCode = zipCode
        self.email = email
        self.phone = phone

    def open_page(self):
        self.driver.get(self.url)

    def page1(self):
        # Находим ссылку с id "nonSubscriber"
        non_subscriber_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "nonSubscriber"))
        )
        # Нажимаем на ссылку
        non_subscriber_link.click()

    def page2(self):
        # получаем формы
        contactName = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "contactName"))
        )
        primaryPhone = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "primaryPhone"))
        )
        emailAddress = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "emailAddress"))
        )
        confirmEmailAddress = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "confirmEmailAddress"))
        )
        streetAddress = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "streetAddress"))
        )
        zipCode = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "zipCode"))
        )
        city = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "city"))
        )
        #заполняем формы
        contactName.send_keys(self.firstName + " " + self.lastName)
        primaryPhone.send_keys(self.phone)
        emailAddress.send_keys(self.email)
        confirmEmailAddress.send_keys(self.email)
        streetAddress.send_keys(self.streetAddress)
        zipCode.send_keys(self.zipCode)
        city.send_keys(self.city)

        #находим и нажимаем кнопку continue
        continueButton = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "contactInformation_action_0"))
        )
        continueButton.click()

    def page3(self):
        businessName = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "businessName"))
        )
        businessName.send_keys(self.name)

        continueButton = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "reservation_action_0"))
        )
        continueButton.click()

    def page4(self):
        reservationTypeDOMESTIC = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "reservationTypeDOMESTIC"))
        )
        reservationTypeDOMESTIC.click()
        entityTypeLLC = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "entityTypeLLC"))
        )
        entityTypeLLC.click()

        #находим и нажимаем кнопку continue
        continueButton = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "entityInformation_action_0"))
        )
        continueButton.click()

    def page5(self):
        # Находим ссылку с указанным атрибутом href
        link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/sos/entityInformation_file.action']"))
        )
        # Нажимаем на найденную ссылку
        link.click()

    def page6(self):
        Individual = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "requestorTypeINDIVIDUAL"))
        )
        Individual.click()

        Name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "name"))
        )
        StreetAddress = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "mailingAddress"))
        )
        City = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "city"))
        )
        ZipCode = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "zipCode"))
        )

        Name.send_keys(self.name)
        StreetAddress.send_keys(self.streetAddress)
        City.send_keys(self.city)
        ZipCode.send_keys(self.zipCode)

        ContinueButton = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "requestorInformation_action_0"))
        )
        ContinueButton.click()

    def page7(self):
        review = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "review"))
        )
        review.click()

        ContinueButton = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "reviewReservation_action_0"))
        )
        ContinueButton.click()

    def page8(self):
        # Ожидаем появления элемента select
        select_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "countyOfFormation"))
        )
        select = Select(select_element)
        select.select_by_value("AUTAUGA")
        time.sleep(1)

        llcTypeLL = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "llcTypeLL"))
        )
        llcTypeLL.click()
        continueButton = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "filingOptions_action_0"))
        )
        continueButton.click()

    def page9(self):
        AgentType = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "registeredAgentTypeINDIVIDUAL"))
        )
        lastName = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "lastName"))
        )
        firstName = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "firstName"))
        )
        suffix = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "suffix"))
        )
        officeAddressStreet = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "officeAddressStreet"))
        )
        officeAddressCity = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "officeAddressCity"))
        )
        officeAddressZip = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "officeAddressZipCode"))
        )
        certifyPhysicalAddress = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "certifyPhysicalAddress"))
        )
        mailingAddressStreet = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "mailingAddressStreet"))
        )
        mailingAddressCity = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "mailingAddressCity"))
        )
        mailingAddressZip = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "mailingAddressZipCode"))
        )
        certifyRegisteredAgent = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "certifyRegisteredAgent"))
        )
        # Ожидаем появления элемента select
        select_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "mailingAddressCounty"))
        )
        select = Select(select_element)
        select.select_by_value("AUTAUGA")
        time.sleep(1)

        certifyRegisteredAgent.click()
        AgentType.click()
        certifyPhysicalAddress.click()

        lastName.send_keys(self.lastName)
        firstName.send_keys(self.firstName)
        suffix.send_keys(self.lastName)
        officeAddressStreet.send_keys(self.streetAddress)
        officeAddressCity.send_keys(self.city)
        officeAddressZip.send_keys(self.zipCode)
        mailingAddressStreet.send_keys(self.streetAddress)
        mailingAddressCity.send_keys(self.city)
        mailingAddressZip.send_keys(self.zipCode)

        ContinueButton = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "registeredAgent_action_0"))
        )
        ContinueButton.click()

    def page10(self):
        # Находим ссылку с указанным атрибутом href
        link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/sos/organizers_skip.action']"))
        )
        # Нажимаем на найденную ссылку
        link.click()

    def page11(self):
        doc = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "documentUploads_action_0"))
        )
        doc.click()
    
    def page12(self):
        other = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "other"))
        )
        other.click()
        continueButton = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "cpoQuestions_action_0"))
        )
        continueButton.click()

    def page13(self):
        electronicSignature = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "electronicSignature"))
        )
        title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "title"))
        )
        title.send_keys("president")
        review = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "review"))
        )
        review.click()
        electronicSignature.send_keys(self.firstName + " " + self.lastName)

        continueButton = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "summary_action_0"))
        )
        continueButton.click()

    def page14(self):
        firstName = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "CustomerInfo_FirstName"))
        )
        lastName = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "CustomerInfo_LastName"))
        )
        Address1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "CustomerInfo_Address1"))
        )
        City = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "CustomerInfo_City"))
        )
        Zip = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "CustomerInfo_Zip"))
        )
        phone = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "Phone"))
        )
        email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "Email"))
        )

        select_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "CustomerInfo_State"))
        )
        select = Select(select_element)
        select.select_by_value("AL")

        firstName.send_keys(self.firstName)
        lastName.send_keys(self.lastName)
        Address1.send_keys(self.streetAddress)
        City.send_keys(self.city)
        Zip.send_keys(self.zipCode)
        phone.send_keys(self.phone)
        email.send_keys(self.email)

        continueButton = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "bntNextCustomerInfo"))
        )
        continueButton.click()


    

    def close_browser(self):
        self.driver.quit()

# Использование класса
scraper = WebScraper("https://www.alabamainteractive.org/sos/introduction_input.action", "The football LLC", "Smith", "Stan", "20 Barton St.", "Auburn", "89145", "stan.smith@example.com", "1234567890")


try:
    scraper.open_page()
    scraper.page1()
    scraper.page2()
    scraper.page3()
    scraper.page4()
    scraper.page5()
    scraper.page6()
    scraper.page7()
    scraper.page8()
    scraper.page9()
    scraper.page10()
    scraper.page11()
    scraper.page12()
    scraper.page13()
    scraper.page14()
    print("Первый результат:")
finally:
    scraper.close_browser()

