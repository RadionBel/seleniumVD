import unittest

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from tests.base import BaseTest
from pages.login.LoginPage import LoginPage


class TempTest(unittest.TestCase):

    @classmethod
    def setup(self):
        # self.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        self.driver = WebDriver(executable_path='chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://panel-demo.t4u-ho.team/v3/auth/#/a/login")

    def test1(self):
        driver = self.driver
        base = BaseTest(driver)
        base.setUp()
        login = LoginPage(driver)
        login.login_as_user(self, "root", "OLS46J25ZQ0fns0Oq6")

    @classmethod
    def teardown(self):
        self.driver.quit()


