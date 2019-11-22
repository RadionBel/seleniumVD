from selenium.webdriver.chrome.webdriver import WebDriver
from allure_commons.types import Severity
import time
import allure


@allure.severity(Severity.BLOCKER)
def test_login():
    driver = WebDriver(executable_path="C://chromDriver//chromedriver.exe")
    with allure.step('Открываем браузер'):
        driver.get('https://marvel-panel.t4u-ho.team/v3/auth/#/a/login')
        driver.maximize_window()

    with allure.step('Логин admin old app'):
        search_input = driver.find_element_by_xpath('//*[@qa_id="input_username"]')
        search_input.send_keys('root')
        search_input = driver.find_element_by_xpath('//*[@qa_id="input_pw"]')
        search_input.send_keys('OLS46J25ZQ0fns0Oq6')
        search_input = driver.find_element_by_xpath('//*[@qa_id="button_login"]').click()                                                                                                                 # login
        time.sleep(10)

    with allure.step('Вылогинюемся'):
        search_input = driver.find_element_by_xpath('/html/body/app/aff-admin-root/div/aff-sidebar/aff-sidebar-wrapper/div/div/div/aff-sidebar-user/div/div/div[3]/aff-logout-button/a').click()
        time.sleep(10)

    with allure.step('Логин admin new app'):
        search_input = driver.find_element_by_xpath('//*[@qa_id="input_username"]')
        search_input.send_keys('root')
        search_input = driver.find_element_by_xpath('//*[@qa_id="input_pw"]')
        search_input.send_keys('OLS46J25ZQ0fns0Oq6')
        search_input = driver.find_element_by_xpath('//*[@qa_id="button_login"]').click()                                                                                                                 # login
        time.sleep(15)

    with allure.step('Переход на новый фронт'):
        search_input = driver.find_element_by_xpath('/html/body/app/aff-admin-root/div/aff-header/aff-header-wrapper/div/div/div[2]/redirect-to-new-app/div/span').click()
        time.sleep(5)

    with allure.step('Вылогинюемся'):
        search_input = driver.find_element_by_xpath('//*[@qa_id="button_current-user"]')
        search_input.click()
        search_input = driver.find_element_by_xpath('//*[@qa_id="link_menu_log-out"]')
        driver.execute_script("arguments[0].click();", search_input)
        time.sleep(10)

    with allure.step('Логин manager old app'):
        search_input = driver.find_element_by_xpath('//*[@qa_id="input_username"]')
        search_input.send_keys('manager')
        search_input = driver.find_element_by_xpath('//*[@qa_id="input_pw"]')
        search_input.send_keys('111111')
        search_input = driver.find_element_by_xpath('//*[@qa_id="button_login"]').click()                                                                                                                 # login
        time.sleep(30)

    with allure.step('Вылогинюемся'):
        search_input = driver.find_element_by_xpath('/html/body/app/aff-manager-root/div/aff-sidebar/aff-sidebar-wrapper/div/div/div/aff-sidebar-user/div/div/div[3]/aff-logout-button/a').click()
        time.sleep(10)

    with allure.step('Логин manager new app'):
        search_input = driver.find_element_by_xpath('//*[@qa_id="input_username"]')
        search_input.send_keys('manager')
        search_input = driver.find_element_by_xpath('//*[@qa_id="input_pw"]')
        search_input.send_keys('111111')
        search_input = driver.find_element_by_xpath('//*[@qa_id="button_login"]').click()                                                                                                                 # login
        time.sleep(30)                                                                                                                     # проверка Title

    with allure.step('Переход на новый фронт'):
        search_input = driver.find_element_by_xpath('/html/body/app/aff-manager-root/div/aff-header/aff-header-wrapper/div/div/div[2]/redirect-to-new-app/div/span').click()
        time.sleep(5)

    with allure.step('Вылогинюемся'):
        search_input = driver.find_element_by_xpath('//*[@qa_id="button_current-user"]')
        search_input.click()
        search_input = driver.find_element_by_xpath('//*[@qa_id="link_menu_log-out"]')
        driver.execute_script("arguments[0].click();", search_input)
        time.sleep(10)
    ...