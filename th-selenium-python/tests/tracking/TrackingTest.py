import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from tests.base import BaseTest
from utilities.Credentials import Credentials
from utilities.Helper import Helper
from utilities.Urls import Urls
from pages.login.LoginPage import LoginPage
from pages.dashboard.SidemenuPage import Sidemenu
from pages.aff_campaigns.AffCampaignsPage import AffCampaigns
from pages.aff_campaigns.AffCampaignViewPage import AffCampaignView
from selenium.webdriver.support import expected_conditions as ec


class MyTestCase(BaseTest):

    def test_tracking_link_with_referrer(self):
        driver = self.driver
        wait = WebDriverWait(self.driver, 10)
        # TODO: как вынести объявления классов отдельно (в BaseTest)
        login = LoginPage(driver)
        creds = Credentials()
        helper = Helper(driver)
        urls = Urls()
        login.login_as_user(creds.admin_login, creds.admin_pw)
        # TODO: перенести wait.until отдельно (в пейдж обджект?)
        wait.until(ec.visibility_of_element_located((By.XPATH, '//redirect-to-new-app')))
        side_menu = Sidemenu(driver)
        # side_menu.click_see_new_view_link()
        # time.sleep(3)
        helper.open_url(driver, urls.domain_dev + urls.atl + urls.aff_campaigns)
        # time.sleep(5)
        wait.until(ec.visibility_of_element_located((By.XPATH, '(//input)[2]')))
        aff_campaigns = AffCampaigns(driver)
        aff_campaigns.fill_search_input("AutoTest - affiliateAuto - tracking")
        aff_campaigns.click_apply_button()
        wait.until(ec.visibility_of_element_located((By.XPATH, '//a[@title="View Campaign"]')))
        # TODO:
        time.sleep(5)
        # helper.wait_for_page_load()
        # aff_campaigns.is_aff_camp_name_exists()
        # print("len is " + str(aff_campaigns.get_aff_camp_names_len()) + " " + aff_campaigns.get_aff_camp_name_text())
        aff_campaigns.click_aff_camp_name()
        wait.until(ec.visibility_of_element_located((By.XPATH, '(//*[@qa_id="link_tracking-link"])[1]')))
        # time.sleep(2)
        # helper.wait_for_page_load()
        aff_camp_view = AffCampaignView(driver)
        aff_camp_view.click_tracking_link_first()
        helper.switch_to_new_tab()
        aff_camp_view.send_ftd()
        helper.close_current_browser_tab()
