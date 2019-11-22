from selenium.webdriver.common.by import By


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

        # self.usernameInput = '//*[@qa_id="input_username"]'
        # self.passwordInput = '//*[@qa_id="input_pw"]'
        # self.loginButton = '//*[@qa_id="button_login"]'
        self.usernameInput = self.driver.find_element(By.XPATH, '//*[@qa_id="input_username"]')
        self.passwordInput = self.driver.find_element(By.XPATH, '//*[@qa_id="input_pw"]')
        self.loginButton = self.driver.find_element(By.XPATH, '//*[@qa_id="button_login"]')

    def login_as_user(self, login, password):
        # self.driver.find_element(By.XPATH, self.usernameInput).clear()
        # self.driver.find_element(By.XPATH, self.usernameInput).send_keys(login)
        # self.driver.find_element(By.XPATH, self.passwordInput).clear()
        # self.driver.find_element(By.XPATH, self.passwordInput).send_keys(password)
        # self.driver.find_element(By.XPATH, self.loginButton).click()

        self.usernameInput.clear()
        self.usernameInput.send_keys(login)
        self.passwordInput.clear()
        self.passwordInput.send_keys(password)
        self.loginButton.click()



