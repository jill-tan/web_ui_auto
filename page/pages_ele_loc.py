from selenium.webdriver.common.by import By
from common.const import PageName


class EleLoc:
    def __init__(self, pageName: PageName):
        func_name = f'add_{pageName.value.lower()}_ele'
        if hasattr(self, func_name):
            func = getattr(self, func_name)
            func()
        else:
            return None

    def add_pre_ele(self):
        self.__dict__["_login_btn_loc"] = (By.LINK_TEXT, "Log In")
        self.__dict__["_signup_btn_loc"] = (By.LINK_TEXT, "Sign Up")

    def add_login_ele(self):
        self.__dict__["_username_text_loc"] = (By.ID, "username")
        self.__dict__["_pwd_text_loc"] = (By.ID, "password")
        self.__dict__["_login_btn_loc"] = (By.NAME, "action")
        self.__dict__["_email_text_loc"] = (By.ID, "email")

    def add_main_ele(self):
        self.__dict__["_profile_tab_loc"] = (By.CSS_SELECTOR, "div.css-1kxonj9:nth-child(4)")
        self.__dict__["_edit_profile_btn_loc"] = (By.CLASS_NAME, "em-button-base")
        self.__dict__["_logout_btn"] = (By.XPATH, "//span[.='Log Out']")
        self.__dict__["_logout_yes_btn"] = (By.XPATH, "//button[.='Yes']")

        # logout_page
        self.__dict__["_logout_check"] = (By.XPATH, "//div[.='Login']")

    def get_loc(self, key):
        key = f'_{key}'
        if key in self.__dict__.keys():
            return self.__dict__[key]
        return None

class PagesEleLoc:
    def __init__(self):
        for page_name in PageName:
            name = self._get_preperty_name(page_name)
            self.__dict__[name] = EleLoc(page_name)

    def _get_preperty_name(self, page_name: PageName):
        return f'_{page_name.value}_loc_dict'


    def _get_property_value(self, key):
        if key in self.__dict__.keys():
            return self.__dict__[key]
        return None

    def get_ele_loc(self, page_name: PageName, ele_name):
        property_name = self._get_preperty_name(page_name)
        page_ele_loc:EleLoc = self._get_property_value(property_name)
        return page_ele_loc.get_loc(ele_name)