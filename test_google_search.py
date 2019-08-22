from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
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
    time.sleep(10)
    search_input = driver.find_element_by_xpath('/html/body/app/aff-admin-root/div/aff-sidebar/aff-sidebar-wrapper/div/div/div/nav/ul/li[3]/a/span')
    search_input.click()
    time.sleep(5)
    search_input = driver.find_element_by_xpath('/html/body/app/aff-admin-root/div/aff-sidebar/aff-sidebar-wrapper/div/div/div/aff-sidebar-user/div/div/div[3]/aff-logout-button/a')
    search_input.click()
    search_input = driver.find_element_by_xpath('//*[@id="mat-input-0"]')
    search_input.send_keys('root')
    search_input = driver.find_element_by_xpath('//*[@id="mat-input-1"]')
    search_input.send_keys('OLS46J25ZQ0fn44s0Oq6')
    search_input = driver.find_element_by_xpath('/html/body/ho-root/div/ho-sign-in-layout/div/div/div/ho-login/div/form/button/span')
    search_input.click()
    time.sleep(60)

    ...