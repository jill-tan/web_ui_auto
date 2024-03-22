from abc import abstractmethod
from test_data.yaml_data import YamlData
from common.const import TestResult

class BaseTest:
    test_result: TestResult

    def run_case(self, yaml_data: YamlData):
        self.test_act(yaml_data)

    @abstractmethod
    def test_act(self, yaml_data: YamlData):
        pass
