from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from common.const import ELE_ACT

class SeleniumAct:
    driver = None

    def _get_driver(self):
        if not SeleniumAct.driver:
            SeleniumAct.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        return SeleniumAct.driver

    def open_url(self, url):
        self._get_driver().get(url)

    def ele_exist(self, *loc):
        try:
            self._get_driver().find_element(*loc)
            return True
        except:
            return False

    def ele_act(self, *loc, act, send_str=""):
        element = self._get_driver().find_element(*loc)
        if act == ELE_ACT.CLICK.value:
            element.click()
        elif act == ELE_ACT.SEND_KEY.value:
            element.send_keys(send_str)

    def close(self):
        self._get_driver().close()
        SeleniumAct.driver = None