from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc

service = Service(ChromeDriverManager().install())
driver = uc.Chrome(service=service)

# Navigate to url
driver.get("https://googlechromelabs.github.io/chrome-for-testing/#stable")

# Get all available cookies
print(driver.get_cookies())
