from selenium import  webdriver
import pytest


CHROME_EXECUTABLE_PATH = "D:/Professional/driverexe/chromedriver.exe"

@pytest.fixture()
def setup():
    driver = webdriver.Chrome(executable_path=CHROME_EXECUTABLE_PATH)
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver