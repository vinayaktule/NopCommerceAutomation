import unittest
import pytest
from selenium import webdriver
from pages.home.LoginPage import LoginPage


class LoginTest(unittest.TestCase):
    CHROME_EXECUTABLE_PATH = "D:/Professional/driverexe/chromedriver.exe"
    baseURL = "https://admin-demo.nopcommerce.com/login"
    USERNAME = "admin@yourstore.com"
    PASSWORD = "admin"
    driver = webdriver.Chrome(executable_path=CHROME_EXECUTABLE_PATH)
    driver.implicitly_wait(10)
    driver.maximize_window()
    lp = LoginPage(driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.lp.login(self.USERNAME, self.PASSWORD)
        result = self.lp.verifyLoginSuccessful()
        assert result == True
        self.driver.quit()

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.driver.get(self.baseURL)
        self.lp.login(self.USERNAME, 'admin1')
        result = self.lp.verifyLoginFailed()
        assert result == True