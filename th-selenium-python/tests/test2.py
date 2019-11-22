from tests.base import BaseTest
from pages.login.LoginPage import LoginPage
from pages.dashboard.SidemenuPage import Sidemenu


class MyTestCase(BaseTest):

    def test1(self):
        driver = self.driver
        login = LoginPage(driver)
        login.login_as_user("", "OLS46J25ZQ0fns0Oq6")
        side_menu = Sidemenu(driver)
        assert not side_menu.is_sidebar_exists()

    def test21(self):
        driver = self.driver
        login = LoginPage(driver)
        login.login_as_user("root", "OLS46J25ZQ0fns0Oq6")
        side_menu = Sidemenu(driver)
        assert side_menu.is_user_role_exists()
