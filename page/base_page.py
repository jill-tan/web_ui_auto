from common.const import ELE_ACT
from common.selenium_act import SeleniumAct
from page.pages_ele_loc import PagesEleLoc
import time
from common.const import PageName

class PageBase:
    page_name: PageName
    driver = SeleniumAct()
    pages_ele_loc = PagesEleLoc()

    def get_ele_loc(self, ele_name, page_name: PageName=None):
        if not page_name:
            page_name = self.page_name

        return self.pages_ele_loc.get_ele_loc(
            page_name,
            ele_name
        )
    def open_url(self, url, sleep_time=0):
        self.driver.open_url(url)
        self._wait_second(sleep_time)
    def ele_exist(self, *loc):
        return self.driver.ele_exist(*loc)

    def ele_click(self, *loc, sleep_time=0):
        self.driver.ele_act(*loc, act=ELE_ACT.CLICK.value)
        self._wait_second(sleep_time)

    def ele_send_str(self, *loc, send_str, sleep_time=0):
        self.driver.ele_act(*loc, act=ELE_ACT.SEND_KEY.value, send_str=send_str)
        self._wait_second(sleep_time)

    def _wait_second(self, second):
        time.sleep(second)

    def close(self):
        self.driver.close()

    def print_pagename(self):
        print(self.page_name.value)