from common.const import PageName
from page.base_page import PageBase
from common.const import AHA_URL

class PrePage(PageBase):
    def __init__(self):
        self.page_name = PageName.PRE

    def _open_url(self):
        self.open_url(AHA_URL, sleep_time=5)
        if self.ele_exist(*self.get_ele_loc("have_google_frame_loc")):
            self.switch_frame(*self.get_ele_loc("google_frame_loc"), contain=False)
            self.ele_click(
                *self.get_ele_loc("close_google_loc")
            )
            self.switch_window()

    def click_signup(self):
        self._open_url()
        self.ele_click(
            *self.get_ele_loc("signup_btn_loc"),
            sleep_time=2
        )

    def click_login(self):
        self._open_url()
        self.ele_click(
            *self.get_ele_loc("login_btn_loc"),
            sleep_time=5
        )

