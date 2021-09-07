from pages.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
import logging
import utilities.custom_logger as cl

class Test_001_LoginTest:

    baseURL = ReadConfig.getApplicationURL()
    USERNAME = ReadConfig.getUsername()
    PASSWORD = ReadConfig.getPassword()

    log = cl.customLogger(logging.DEBUG)
    log.info("#"*15+'Test_001_LoginTest'+"#"*15)
    def test_valid_login(self, setup):
        self.log.info("*"*15+'test_valid_login'+"*"*15)
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.login(self.USERNAME, self.PASSWORD)
        result = self.lp.verifyLoginSuccessful()
        assert result == True
        self.driver.quit()
        self.log.info('='*15+"Test Passed"+'='*15)
        self.log.info('+'*15+"Completed Test_001_LoginTest"+'+'*15)

    # def test_invalid_login(self, setup):
    #     self.log.info("*"*15+'test_invalid_login'+"*"*15)
    #     self.driver = setup
    #     self.lp = LoginPage(self.driver)
    #     self.driver.get(self.baseURL)
    #     self.lp.login(self.USERNAME, 'admin1')
    #     result = self.lp.verifyLoginFailed()
    #     assert result == True
    #     self.driver.quit()
    #     self.log.info('='*15+"Test Passed"+'='*15)