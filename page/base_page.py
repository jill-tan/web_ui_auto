from common.const import ELE_ACT
from common.selenium_act import SeleniumAct
from page.pages_ele_loc import PagesEleLoc
import time
from common.const import PageName
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    NoSuchFrameException,
    NoSuchElementException
)

class PageBase:
    page_name: PageName
    driver = SeleniumAct()
    pages_ele_loc = PagesEleLoc()

    def get_ele_loc(self, ele_name, page_name: PageName=None):
        if not page_name:
            page_name = self.page_name

        result = (
            ele_name,
            self.pages_ele_loc.get_ele_loc(
                page_name,
                ele_name
            )
        )
        return result

    def open_url(self, url, sleep_time=0):
        self.driver.open_url(url)
        self._wait_second(sleep_time)

    def ele_exist(self, *loc):
        def _func(*loc):
            return self.driver.ele_exist(*loc)

        return self.exe_ele_act(_func, *loc)

    def ele_click(self, *loc, sleep_time=0):
        def _func(*loc):
            self.driver.ele_act(*loc, act=ELE_ACT.CLICK.value)
            self._wait_second(sleep_time)

        self.exe_ele_act(_func, *loc)

    def ele_click_loc(self, *loc, sleep_time=0):
        def _func(*loc):
            self.driver.ele_act(*loc, act=ELE_ACT.CLICL_LOCATION.value)
            self._wait_second(sleep_time)

        self.exe_ele_act(_func, *loc)

    def ele_move(self, *loc, sleep_time=0):
        def _func(*loc):
            self.driver.ele_act(*loc, act=ELE_ACT.MOVE.value)
            self._wait_second(sleep_time)

        self.exe_ele_act(_func, *loc)

    def ele_send_str(self, *loc, send_str, sleep_time=0):
        def _func(*loc):
            self.driver.ele_act(*loc, act=ELE_ACT.SEND_KEY.value, send_str=send_str)
            self._wait_second(sleep_time)

        self.exe_ele_act(_func, *loc)

    def get_eles(self, *loc):
        def _func(*loc):
            self.driver.ele_act(*loc, act=ELE_ACT.ELES.value)

        self.exe_ele_act(_func, *loc)

    def switch_frame(self, *loc, contain=False):
        def _func(*loc):
            self.driver.ele_act(*loc, act=ELE_ACT.SWITCH_FRAME.value, contain=contain)

        self.exe_ele_act(_func, *loc)

    def exe_ele_act(self, func, *loc):
        ele_name, loc = loc
        msg = f'{self.page_name} / {ele_name}'
        try:
            return func(*loc)
        except ElementClickInterceptedException as e:
            raise Exception(f"ElementClickInterceptedException -> {msg} \n---- \n{e.msg}")
        except NoSuchFrameException as e:
            raise Exception(f"NoSuchFrameException -> {msg} \n---- \n{e.msg}")
        except NoSuchElementException as e:
            raise Exception(f"NoSuchElementException -> {msg} \n---- \n{e.msg}")
        except Exception as e:
            raise

    def _wait_second(self, second):
        time.sleep(second)

    def close(self):
        self.driver.close()

    def close_pop(self):
        self.driver.close_pop()

    def switch_window(self):
        self.driver.switch_window()

    def print_pagename(self):
        # print(self.page_name.value)
        self.driver.print_out_ele()