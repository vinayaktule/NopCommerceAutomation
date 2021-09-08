import time

from base.seleniumDriver import SeleniumDriver

class CatalogPage(SeleniumDriver):
    #PRODUCT DETAILS PAGE
    _catalog_link_css = "i[class='nav-icon fas fa-book']"
    _productlist_link_css = "a[href='/Admin/Product/List']"
    _searchProductName_field = "SearchProductName"
    _searchproducts_button = "search-products"
    _singleSearchedProduct_xpath = "//*[@id='products-grid']/tbody/tr[1]/td[3]"
    _selectSingleItem_radioButton_css = "input[name='checkbox_products']"
    _editSingleItem_link_css = "a[href='Edit/4']"
    _num_rows_xpath = "//*[@id='products-grid']/tbody/tr"
    _num_column_xpath = "//*[@id='products-grid']/tbody/tr/td"
    _addNewProduct_link_css = "a[href='/Admin/Product/Create']"
    _webTable_css = ""
    #EDIT PRODUCT PAGE
    _updateProductName_field_css = "button[type='submit'][name='save']"
    _updateSave_button_name = "save"
    _adminComment_field_css = "[name='AdminComment']"
    _updateSuccessAlert_css = "[class='alert alert-success alert-dismissable']"


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def clickCatalogLink(self):
        self.elementClick(self._catalog_link_css, locatorType='css')

    def clickProductLink(self):
        self.elementClick(self._productlist_link_css, locatorType='css')

    def enterProductName(self, product_name):
        self.sendKeys(product_name, self._searchProductName_field)

    def clickOnSearchButton(self):
        self.elementClick(self._searchproducts_button)

    def SingleItemSearchResult(self, searchedText):
        searchElement = self.getElement(self._singleSearchedProduct_xpath, locatorType= 'xpath')
        time.sleep(5)
        searchElementText = searchElement.text
        print(searchElementText)
        if searchElementText == searchedText:
            return True
        else:
            return False

    def selectSingleItem(self):
        self.elementClick(self._selectSingleItem_radioButton_css, locatorType='css')

    def editSingleItem(self):
        self.elementClick(self._editSingleItem_link_css, locatorType='css')

    def updateProductName(self, productName):
        self.sendKeys(productName, self._updateProductName_field_css, locatorType='css')

    def enterAdminComment(self, adminComment):
        self.sendKeys(adminComment, self._adminComment_field_css, locatorType='css')

    def saveUpdate(self):
        self.elementClick(self._updateSave_button_name, locatorType='name')

    def checkUpdateSuccess(self):
        return self.isElementPresent(self._updateSuccessAlert_css, 'css')



