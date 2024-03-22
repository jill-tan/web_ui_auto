# Notifications
# Direct Messages
# Avatar Marketplace
# Profile -> logout

from common.const import PageName
from page.base_page import PageBase


class MainPage(PageBase):
    def __init__(self):
        self.page_name = PageName.MAIN

    def _click_profile_tab(self, sleep_time=2):
        self.ele_click(*self.get_ele_loc("profile_tab_loc"), sleep_time=sleep_time)

    def open_edit_profile(self, sleep_time=2):
        self._click_profile_tab()
        self.ele_click(*self.get_ele_loc("edit_profile_btn_loc"), sleep_time=sleep_time)

    def logout_act(self):
        self._click_profile_tab()
        self.ele_click(*self.get_ele_loc("logout_btn"))
        self.ele_click(*self.get_ele_loc("logout_yes_btn"))

        # check
        if not self.ele_exist(*self.get_ele_loc("logout_check")):
            print('Log Out Fail')
            return False
        return True