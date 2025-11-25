from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class WebDriverConfig:
    """Конфигурация WebDriver"""

    @staticmethod
    def setup_driver():
        """Настройка и запуск WebDriver"""
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        return driver

    @staticmethod
    def teardown_driver(driver):
        """Завершение работы WebDriver"""
        if driver:
            driver.quit()