from selenium.webdriver.common.by import By
import re
import requests


class AffCampaignView():
    def __init__(self, driver):
        self.driver = driver

# Locators

        self.tracking_link_first = '(//*[@qa_id="link_tracking-link"])[1]'

# Methods

    def click_tracking_link_first(self):
        self.driver.find_element(By.XPATH, self.tracking_link_first).click()

        # # switch to new browser tab
        # handles = self.driver.window_handles
        # size = len(handles)
        # parent_handle = self.driver.current_window_handle
        # for x in range(size):
        #     if handles[x] != parent_handle:
        #         self.driver.switch_to.window(handles[x])
        #         self.send_ftd()
        #         self.driver.close()
        #         break

    def get_click_id_from_url(self):
        url1 = self.driver.current_url
        # make an array from current url, each element of which is divided by "&"
        url_array = re.split("&", url1)
        # create a variable for click id parameter (click_id={some_value})
        click_id_param = ""
        for i in range(len(url_array)):
            # find element of array, that contains "click_id" text
            if "click_id" in url_array[i]:
                click_id_param = url_array[i]

        # make an array from click_id parameter, divided by "=" (ex. ['click_id','sfdfd454534']
        click_id_array = click_id_param.split("=")
        # assign the 2nd element of array ('sfdfd454534') to variable
        click_id_value = click_id_array[1]
        return click_id_value

    def send_ftd(self):
        click_id = self.get_click_id_from_url()
        ftd_callback_url = "https://venom-callback.t4u-ho.team" + "/tracker/callback?secret=" + "8qUSPZlnEA" + "&u=" + click_id + "&t=ftd"
        requests.post(ftd_callback_url)


