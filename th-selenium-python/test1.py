from selenium.webdriver.chrome.webdriver import WebDriver


def test11():
    driver = WebDriver(executable_path='chromedriver.exe')
    driver.maximize_window()
    driver.get('https://panel-dev.t4u-ho.team/v3/auth/#/a/login')
    # search_input=driver.find_element_by_id()
    print('new dri')