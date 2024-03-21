from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from common.const import ELE_ACT
from selenium.webdriver.common.by import By
import time

class PageBase:
    page_name = ''
    driver = None

    def _get_driver(self):
        if not PageBase.driver:
            PageBase.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        return PageBase.driver

    def open_url(self, url, sleep_time=0):
        self._get_driver().get(url)
        self._wait_second(sleep_time)

    def ele_exist(self, *loc):
        try:
            self._get_driver().find_element(*loc)
            return True
        except:
            return False

    def ele_click(self, *loc, sleep_time=0):
        self._ele_act(*loc, act=ELE_ACT.CLICK.value)
        self._wait_second(sleep_time)

    def ele_send_str(self, *loc, send_str, sleep_time=0):
        self._ele_act(*loc, act=ELE_ACT.SEND_KEY.value, send_str=send_str)
        self._wait_second(sleep_time)

    def _ele_act(self, *loc, act, send_str=""):
        element = self._get_driver().find_element(*loc)
        if act == ELE_ACT.CLICK.value:
            element.click()
        elif act == ELE_ACT.SEND_KEY.value:
            element.send_keys(send_str)

    def _wait_second(self, second):
        time.sleep(second)
