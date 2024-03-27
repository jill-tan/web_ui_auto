from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from common.const import ELE_ACT
from selenium.common.exceptions import NoSuchFrameException
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


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
        except Exception as e:
            print(e)
            return False

    def ele_act(self, *loc, act, send_str="", contain=False):
        if act == ELE_ACT.CLICK.value:
            element = self._get_driver().find_element(*loc)
            element.click()
        elif act == ELE_ACT.SEND_KEY.value:
            element = self._get_driver().find_element(*loc)
            element.send_keys(send_str)
        elif act == ELE_ACT.SWITCH_FRAME.value:
            self.switch_frame(*loc, contain=contain)
        elif act == ELE_ACT.CLICL_LOCATION.value:
            self.click_location(*loc)
        elif act == ELE_ACT.MOVE.value:
            element = self._get_driver().find_element(*loc)
            action = ActionChains(self._get_driver())
            action.move_to_element(element).click().perform()

    def click_location(self, *loc):
        element = self._get_driver().find_element(*loc)
        action = ActionChains(self._get_driver())
        action.move_to_element_with_offset(element, element.location['y'], element.location['x'])
        action.click()
        action.perform()
        
    def close_pop(self):
        self._get_driver().switch_to.alert.dismiss()

    def switch_frame(self, *loc, contain=False):
        attr_name, values = loc

        iframes = self._get_driver().find_elements(By.TAG_NAME, 'iframe')

        for iframe in iframes:
            value = iframe.get_attribute(attr_name)
            if contain:
                if value and value in values:
                    self._get_driver().switch_to.frame(iframe)
                    return True
            else:
                if not value or value not in values:
                    self._get_driver().switch_to.frame(iframe)
                    return True
        raise NoSuchFrameException()

    def switch_window(self):
        self._get_driver().switch_to.default_content()

    def close(self):
        self._get_driver().close()
        SeleniumAct.driver = None