from page.page_manager import(
  pre_page,
  login_page,
)
from test_data.yaml_data import YamlData
from test_case.test_base import BaseTest

class TestCase(BaseTest):
    def test_act(self, yaml_data: YamlData):
        pre_page.click_signup()
        login_page.signup_act(yaml_data.email, yaml_data.pwd)
        login_page.close()
