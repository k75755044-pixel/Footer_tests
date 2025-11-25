from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class WebDriverConfig:

    @staticmethod
    def setup_driver():
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        return driver

    @staticmethod
    def teardown_driver(driver):
        if driver:
            driver.quit()