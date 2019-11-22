from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class AffCampaigns():
    def __init__(self, driver):
        self.driver = driver

# Locators

        self.searchInput = '(//input)[2]'
        self.refreshButton = '(//button[contains(@class, "btn_success")])[2]'
        self.affCampName = '//a[@title="View Campaign"]'

# Methods

    def fill_search_input(self, text):
        self.driver.find_element(By.XPATH, self.searchInput).clear()
        self.driver.find_element(By.XPATH, self.searchInput).send_keys(text)

    def click_apply_button(self):
        self.driver.find_element(By.XPATH, self.refreshButton).click()

    def click_aff_camp_name(self):
        self.driver.find_elements(By.XPATH, self.affCampName)[0].click()

    def is_aff_camp_name_exists(self):
        try:
            self.driver.find_elements(By.XPATH, self.affCampName)
            print("Exists!")
        except NoSuchElementException:
            print("Not exists!")
            return False
        return True

    def get_aff_camp_names_len(self):
        return len(self.affCampName)

    def get_aff_camp_name_text(self):
        return self.driver.find_elements(By.XPATH, self.affCampName)[0].text




