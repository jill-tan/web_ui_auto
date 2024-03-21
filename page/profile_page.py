from common.const import PageName
from page.base_page import PageBase
from selenium.webdriver.common.by import By

class ProfilePage(PageBase):
    date_text_loc = (By.XPATH, "//input[@readonly='']")
    date_picker_loc = (By.XPATH, By.TAG_NAME, 'h5')

    def __init__(self):
        self.page_name = PageName.PROFILE

    def set_up_birthday(self):
        self.ele_click(*self.date_text_loc)
        self.ele_click(*self.date_picker_loc)

        datefield = driver.find_element(By.TAG_NAME, 'h5')
        datefield.click()
        datefield.send_keys("01012011")