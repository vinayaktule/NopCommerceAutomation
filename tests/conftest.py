from selenium import  webdriver
import pytest


CHROME_EXECUTABLE_PATH = "D:/Professional/driverexe/chromedriver.exe"
GECKO_EXECUTABLE_PATH = "D:/Professional/driverexe/geckodriver.exe"
IE_EXECUTABLE_PATH = "D:/Professional/driverexe/IEDriverServer.exe"

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path=CHROME_EXECUTABLE_PATH)
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GECKO_EXECUTABLE_PATH)
    else:
        driver = webdriver.Ie(executable_path=IE_EXECUTABLE_PATH)

    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_configure(config):
    config._metadata['Project Name'] = 'nopCommerce Report'
    config._metadata['Module name'] = 'Test Module for login and Customer'
    config._metadata['Tester'] = 'VT'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)