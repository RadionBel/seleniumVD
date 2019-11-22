import time

from selenium.webdriver.common.by import By


class BasePage:
    PAGE_SELECTOR_MAP = {}

    def __init__(self, driver):
        self.driver = driver

    def navigate(self, selector):
        time.sleep(3)
        self.driver.find_elements(By.XPATH, selector)[0].click()

        if selector in self.PAGE_SELECTOR_MAP:
            return self.PAGE_SELECTOR_MAP[selector](self.driver)