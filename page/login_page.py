from page.base_page import PageBase
from common.const import PageName
from selenium.webdriver.common.by import By

class LoginPage(PageBase):
    _username_text_loc = (By.ID, "username")
    _pwd_text_loc = (By.ID, "password")
    _login_btn_loc = (By.NAME, "action")
    _email_text_loc = (By.ID, "email")
    # main_page
    _login_check_loc = (By.CSS_SELECTOR, "div.css-1kxonj9:nth-child(4)")

    def __init__(self):
        self.page_name = PageName.LOG_IN

    def login_act(self, username, password, sleep_time=10):
        self.ele_send_str(*self._username_text_loc, send_str=username)
        self.ele_send_str(*self._pwd_text_loc, send_str=password)
        self.ele_click(*self._login_btn_loc, sleep_time=sleep_time)
        if not self.ele_exist(*self._login_check_loc):
            print('Log In Fail')
            return False
        return True

    def signup_act(self, username, password, sleep_time=10):
        self.ele_send_str(*self._email_text_loc, send_str=username)
        self.ele_send_str(*self._pwd_text_loc, send_str=password)
        self.ele_click(*self._login_btn_loc, sleep_time=sleep_time)
        if not self.ele_exist(*self._login_check_loc):
            print('Sign Up Fail')
            return False
        return True