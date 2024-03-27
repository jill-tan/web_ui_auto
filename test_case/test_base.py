from abc import abstractmethod
from test_data.yaml_data import YamlData
from common.const import TestResult
from selenium.common.exceptions import ElementClickInterceptedException

class BaseTest:
    test_result: TestResult

    def run_case(self, yaml_data: YamlData):
        try:
            self.test_act(yaml_data)
        except ElementClickInterceptedException as e:
            print(e.msg)
        except Exception as e:
            print(e)

    @abstractmethod
    def test_act(self, yaml_data: YamlData):
        pass
