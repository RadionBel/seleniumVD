from selenium.webdriver.chrome.webdriver import WebDriver
from allure_commons.types import Severity
from selenium.webdriver.support.wait import WebDriverWait
import time
import allure


@allure.title('Результат поиска равна 12')
@allure.severity(Severity.BLOCKER)
def test_google():
    driver = WebDriver(executable_path='C://chromDriver//chromedriver.exe')
    with allure.step('Открываем браузер'):
        driver.get('https://panel-dev.t4u-ho.team/v2/#/auth/sign-in')

    with allure.step('Логин пользователя'):
        search_input = driver.find_element_by_xpath('//*[@id="mat-input-0"]')
        search_input.send_keys('root')
        search_input = driver.find_element_by_xpath('//*[@id="mat-input-1"]')
        search_input.send_keys('OLS46J25ZQ0fns0Oq6')
        search_input = driver.find_element_by_xpath('/html/body/ho-root/div/ho-sign-in-layout/div/div/div/ho-login/div/form/button/span')
        search_input.click()                                                                                                                 # login
        time.sleep(10)

    with allure.step('Проверяем правильность Title'):
        assert driver.title == "Huge Offers"
        time.sleep(2)                                                                                                                         # проверка Title

    with allure.step('Поиск количества пунктов меню'):
        search_results = driver.find_elements_by_xpath('//li[@routerlinkactive="active"]')                                                    # проверка количества пунктов меню
        assert len(search_results) == 12
        time.sleep(2)
        search_input = driver.find_element_by_xpath('/html/body/app/aff-admin-root/div/aff-sidebar/aff-sidebar-wrapper/div/div/div/nav/ul/li[3]/a/span')
        search_input.click()
        time.sleep(5)

    with allure.step('Вылогинюемся'):
        search_input = driver.find_element_by_xpath('/html/body/app/aff-admin-root/div/aff-sidebar/aff-sidebar-wrapper/div/div/div/aff-sidebar-user/div/div/div[3]/aff-logout-button/a')
        search_input.click()

    with allure.step('Логинимся с неправильным паролем'):
        search_input = driver.find_element_by_xpath('//*[@id="mat-input-0"]')
        search_input.send_keys('root')
        search_input = driver.find_element_by_xpath('//*[@id="mat-input-1"]')
        search_input.send_keys('OLS46J25ZQ0fwns0Oq6')
        search_input = driver.find_element_by_xpath('/html/body/ho-root/div/ho-sign-in-layout/div/div/div/ho-login/div/form/button/span')
        search_input.click()
        search_input = driver.find_element_by_xpath('//*[@id="mat-input-1"]')
        search_input.clear()
        time.sleep(3)
        search_input.send_keys('OLS46J25ZQ0fns0Oq6')
        time.sleep(3)
        search_input = driver.find_element_by_xpath('/html/body/ho-root/div/ho-sign-in-layout/div/div/div/ho-login/div/form/button/span')
        search_input.click()

    time.sleep(10)

    ...