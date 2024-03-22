from page.base_page import PageBase
from common.const import PageName

class LoginPage(PageBase):
    def __init__(self):
        self.page_name = PageName.LOG_IN

    def login_act(self, username, password, sleep_time=10):
        self.ele_send_str(*self.get_ele_loc("username_text_loc"), send_str=username)
        self.ele_send_str(*self.get_ele_loc("pwd_text_loc"), send_str=password)
        self.ele_click(*self.get_ele_loc("login_btn_loc"), sleep_time=sleep_time)

        if not self.ele_exist(
                *self.get_ele_loc("profile_tab_loc", page_name=PageName.MAIN)
        ):
            print('Log In Fail')
            return False
        return True

    def signup_act(self, username, password, sleep_time=10):
        self.ele_send_str(*self.get_ele_loc("email_text_loc"), send_str=username)
        self.ele_send_str(*self.get_ele_loc("pwd_text_loc"), send_str=password)
        self.ele_click(*self.get_ele_loc("login_btn_loc"), sleep_time=sleep_time)
        if not self.ele_exist(*self.get_ele_loc("profile_tab_loc", page_name=PageName.MAIN)):
            print('Sign Up Fail')
            return False
        return True