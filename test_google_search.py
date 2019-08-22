from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

def test_google():
    driver = WebDriver(executable_path='C://chromDriver//chromedriver.exe')
    driver.get('https://panel-dev.t4u-ho.team/v2/#/auth/sign-in')
    search_input = driver.find_element_by_xpath('//*[@id="mat-input-0"]')
    search_input.send_keys('root')
    search_input = driver.find_element_by_xpath('//*[@id="mat-input-1"]')
    search_input.send_keys('OLS46J25ZQ0fns0Oq6')
    search_input = driver.find_element_by_xpath('/html/body/ho-root/div/ho-sign-in-layout/div/div/div/ho-login/div/form/button/span')
    search_input.click()
    print(None)
    time.sleep(60)
    ...