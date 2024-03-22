from common.const import PageName
from page.base_page import PageBase
from common.const import AHA_URL

class PrePage(PageBase):
    def __init__(self):
        self.page_name = PageName.PRE

    def click_signup(self):
        self.open_url(AHA_URL, sleep_time=5)
        self.ele_click(
            *self.get_ele_loc("signup_btn_loc"),
            sleep_time=2
        )

    def click_login(self):
        self.open_url(AHA_URL, sleep_time=5)
        self.ele_click(
            *self.get_ele_loc("login_btn_loc"),
            sleep_time=2
        )

