class Helper():
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, driver, url):
        self.driver = driver
        self.driver.get(url)

    def switch_to_new_tab(self):
        handles = self.driver.window_handles
        size = len(handles)
        parent_handle = self.driver.current_window_handle
        for x in range(size):
            if handles[x] != parent_handle:
                self.driver.switch_to.window(handles[x])
                break

    def close_current_browser_tab(self):
        self.driver.close()

    def wait_for_page_load(self):
        page_state = self.driver.execute_script('return document.readyState;')
        return page_state == 'complete'
