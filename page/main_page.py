# Notifications
# Direct Messages
# Avatar Marketplace
# Profile -> logout

from common.const import PageName
from page.base_page import PageBase
from selenium.webdriver.common.by import By


class MainPage(PageBase):
    _profile_tab_loc = (By.CSS_SELECTOR, "div.css-1kxonj9:nth-child(4)")
    _edit_profile_btn_loc = (By.CLASS_NAME, "em-button-base")
    _logout_btn = (By.XPATH, "//span[.='Log Out']")
    _logout_yes_btn = (By.XPATH, "//button[.='Yes']")
    # logout_page
    _logout_check = (By.XPATH, "//div[.='Login']")

    def __init__(self):
        self.page_name = PageName.MAIN

    def _click_profile_tab(self, sleep_time=2):
        self.ele_click(*self._profile_tab_loc, sleep_time=sleep_time)

    def open_edit_profile(self, sleep_time=2):
        self._click_profile_tab()
        self.ele_click(*self._edit_profile_btn_loc, sleep_time=sleep_time)

    def logout_act(self):
        self._click_profile_tab()
        self.ele_click(*self._logout_btn)
        self.ele_click(*self._logout_yes_btn)

        # check
        if not self.ele_exist(*self._logout_check):
            print('Log Out Fail')
            return False
        return True