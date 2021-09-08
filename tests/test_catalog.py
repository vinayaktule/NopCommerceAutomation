import time

from pages.CatlogPage import CatalogPage
from pages.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
import logging
import utilities.custom_logger as cl

class Test_003_CatalogTest:

    baseURL = ReadConfig.getApplicationURL()
    USERNAME = ReadConfig.getUsername()
    PASSWORD = ReadConfig.getPassword()

    log = cl.customLogger(logging.DEBUG)

    log.info("#"*15+'Test_001_LoginTest'+"#"*15)
    def test_product_search(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.login(self.USERNAME, self.PASSWORD)
        #self.lp.verifyLoginSuccessful()

        self.cp= CatalogPage(self.driver)
        self.cp.clickCatalogLink()
        self.cp.clickProductLink()
        self.cp.enterProductName("Apple MacBook Pro 13-inch")
        self.cp.clickOnSearchButton()
        assert  self.cp.SingleItemSearchResult("Apple MacBook Pro 13-inch") == True

        self.driver.quit()

    def test_update_product_details(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.login(self.USERNAME, self.PASSWORD)
        self.cp= CatalogPage(self.driver)
        self.cp.clickCatalogLink()
        self.cp.clickProductLink()
        self.cp.enterProductName("Apple MacBook Pro 13-inch")
        self.cp.clickOnSearchButton()
        self.cp.editSingleItem()

        self.cp.updateProductName("Apple MacBook Pro 13-inches")
        self.cp.enterAdminComment("Apple MacBook Pro 13-inch name is updated")
        self.cp.saveUpdate()
        result = self.cp.checkUpdateSuccess()
        self.log.info("Product is updated")
        if result:
            #self.cp.clickCatalogLink()
            self.cp.clickProductLink()
            self.cp.enterProductName("Apple MacBook Pro 13-inches")
            self.cp.clickOnSearchButton()
            time.sleep(5)
            result = self.cp.SingleItemSearchResult("Apple MacBook Pro 13-inches")
            assert result == True
        else:
            assert False
        self.driver.quit()






