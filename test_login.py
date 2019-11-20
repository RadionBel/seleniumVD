from selenium.webdriver.chrome.webdriver import WebDriver
from allure_commons.types import Severity
import time
import allure
@allure.title('Результат поиска равна 11')
@allure.severity(Severity.BLOCKER)
def test_login():
    driver = WebDriver(executable_path="C://chromDriver//chromedriver.exe")
    with allure.step('Открываем браузер'):
        driver.get('https://panel-dev.t4u-ho.team/v3/affiliate-team-lead/#/a/login')

    with allure.step('Логин пользователя'):
        search_input = driver.find_element_by_xpath('//*[@qa_id="input_username"]')
        search_input.send_keys('root')
        search_input = driver.find_element_by_xpath('//*[@qa_id="input_pw"]')
        search_input.send_keys('OLS46J25ZQ0fns0Oq6')
        search_input = driver.find_element_by_xpath('//*[@qa_id="button_login"]').click()                                                                                                                 # login
        time.sleep(10)

    with allure.step('Проверяем правильность Title'):
        assert driver.title == "Huge Offers"
        time.sleep(2)                                                                                                                         # проверка Title
    with allure.step('Поиск количества пунктов меню'):
        search_results = driver.find_elements_by_xpath('//li[@routerlinkactive="active"]')                                                    # проверка количества пунктов меню
        assert len(search_results) == 11
        time.sleep(2)

    with allure.step('Переход на новый фронт'):
        search_input = driver.find_element_by_xpath('/html/body/app/aff-admin-root/div/aff-header/aff-header-wrapper/div/div/div[2]/redirect-to-new-app/div/span').click()
        time.sleep(5)

    with allure.step('Вылогинюемся'):
        search_input = driver.find_element_by_xpath('//*[@qa_id="button_current-user"]')
        search_input.click()
        search_input = driver.find_element_by_xpath('//*[@qa_id="link_menu_log-out"]')
        driver.execute_script("arguments[0].click();", search_input)


    time.sleep(10)

    ...