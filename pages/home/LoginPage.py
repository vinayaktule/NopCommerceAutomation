import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from base.seleniumDriver import SeleniumDriver


class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""
    _username_field  = "Email"
    _password_field = "Password"
    _login_button = "button[type='submit']"
    _logout_link = "a[href='/logout']"
    _login_fail = "ul>li:first-of-type"

    # def getLoginButton(self):
    #     return self.driver.find_element(By.CSS_SELECTOR, self._login_button)
    #
    # def getUsernameField(self):
    #     return self.driver.find_element(By.ID, self._username_field)
    #
    # def getPasswordField(self):
    #     return self.driver.find_element(By.ID, self._password_field)

    def enterUsername(self, username):
        self.sendKeys(username, self._username_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType='css')

    def login(self, username="", password=""):
        self.enterUsername(username)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent(self._logout_link, locatorType='css')
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(self._login_fail, locatorType='css')
        return result
