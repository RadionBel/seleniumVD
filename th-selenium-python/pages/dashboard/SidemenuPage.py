from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class Sidemenu():
    def __init__(self, driver):
        self.driver = driver

        # locators
        # self.sidebarDiv = self.driver.find_element(By.XPATH, '//nav[@class="aside-menu"]')
        self.sidebarDiv = '//nav[@class="aside-menu"]'
        # self.userRole = self.driver.find_element(By.XPATH, '//div[@class="page-name"]')
        self.seeNewViewLink = self.driver.find_element(By.XPATH, '//redirect-to-new-app')
        self.userRole = '//div[@class="page-name"]'

        # methods

    def is_sidebar_exists(self):
        try:
            self.driver.find_element(By.XPATH, self.sidebarDiv)
        except NoSuchElementException:
            return False
        return True

    def is_user_role_exists(self):
        try:
            self.driver.find_element(By.XPATH, self.userRole)
        except NoSuchElementException:
            return False
        return True

    def click_see_new_view_link(self):
        self.seeNewViewLink.click()
