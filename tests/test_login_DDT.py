from pages.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities import XLUtils as xl
import logging
import utilities.custom_logger as cl

class Test_002_DDT_LoginTest:

    baseURL = ReadConfig.getApplicationURL()
    # USERNAME = ReadConfig.getUsername()
    # PASSWORD = ReadConfig.getPassword()
    XLFilePath = "C://NopCommerceAutomation//TestData//LoginData.xlsx"
    log = cl.customLogger(logging.DEBUG)
    log.info("#"*15+'Test_001_LoginTest'+"#"*15)
    def test_DDT_login(self, setup):
        self.log.info("*"*15+'test_valid_login'+"*"*15)
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = xl.getRowCount(self.XLFilePath, sheetName='Sheet1')
        list_status = []
        for r in range(2, self.rows+1):
            self.USERNAME = xl.readData(self.XLFilePath, sheetName='Sheet1', rownum=r, columnnum=1)
            self.PASSWORD = xl.readData(self.XLFilePath, sheetName='Sheet1', rownum=r, columnnum=2)
            self.expected_result = xl.readData(self.XLFilePath, sheetName='Sheet1', rownum=r, columnnum=3)

            self.lp.login(self.USERNAME, self.PASSWORD)
            result = self.lp.verifyLoginSuccessful()
            self.boolean_result = True if self.expected_result=='Pass' else False

            if self.boolean_result:
                if result:
                    self.log.info('='*15+"Test passed"+'='*15)
                    self.lp.clickLogout()
                    list_status.append("PASS")
                else:
                    self.log.info('='*15+"Test Failed"+'='*15)
                    self.driver.refresh()
                    list_status.append("Fail")
            elif not self.boolean_result:
                if result:
                    self.log.info('=' * 15 + "Test Failed" + '=' * 15)
                    self.lp.clickLogout()
                    list_status.append("Fail")
                else:
                    self.log.info('=' * 15 + "Test passed" + '=' * 15)
                    self.driver.refresh()
                    list_status.append("PASS")

        if 'Fail' not in list_status:
            self.log.info("DDT Login test is passed")
        else:
            self.log.info("DDT Login test is failed")
        self.driver.quit()
        self.log.info('+'*15+"Completed Test_002_DDT_LoginTest"+'+'*15)