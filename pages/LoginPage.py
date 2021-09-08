from base.seleniumDriver import SeleniumDriver


class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""
    _username_field  = "Email"
    _password_field = "Password"
    _login_button_css = "button[type='submit']"
    _logout_link_css = "a[href='/logout']"
    _login_fail_css = "ul>li:first-of-type"

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
        self.elementClick(self._login_button_css, locatorType='css')

    def clickLogout(self):
        self.elementClick(self._logout_link_css, locatorType='css')

    def login(self, username="", password=""):
        self.enterUsername(username)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent(self._logout_link_css, locatorType='css')
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(self._login_fail_css, locatorType='css')
        if not result:
            self.driver.save_screenshot(".\\screenshots\\"+"verifyLoginFailed"+".png")
        return result
