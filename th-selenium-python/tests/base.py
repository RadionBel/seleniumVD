import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from utilities.Urls import Urls
from utilities.Helper import Helper


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        # self.driver = WebDriver(executable_path='chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        urls = Urls()
        helper = Helper(self.driver)
        self.driver.get("https://t4u:CH0KWMBHPXHRMH7B@venom-bcp.t4u-ho.team/site/login")
        self.driver.get(urls.domain_dev + urls.login)

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
